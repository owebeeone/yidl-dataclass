"""Untimed model/case preparation and identical benchmark loop sources."""

import dataclasses as std


def model(api, count, *, slots=True, frozen=False, factory=False, **options):
    namespace = {
        "__annotations__": {f"f{i}": int for i in range(count)},
        "__module__": __name__,
    }
    namespace.update(
        {
            f"f{i}": api.field(default_factory=int) if factory else i
            for i in range(count)
        }
    )
    cls = type(f"Fields{count}", (), namespace)
    return api.dataclass(slots=slots, frozen=frozen, order=True, **options)(cls)


def extension_cases(product, count):
    """Extension cases with setup outside each clock."""
    result = {}
    for label, options in (
        ("pipeline_plain", {}),
        ("pipeline_converted", {"converter": int}),
        ("pipeline_validated", {"validator": lambda value: value >= 0}),
        ("pipeline_both", {"converter": int, "validator": lambda value: value >= 0}),
    ):
        namespace = {
            "__annotations__": {f"f{i}": int for i in range(count)},
            "__module__": __name__,
        }
        namespace.update({f"f{i}": i for i in range(count)})
        namespace["f0"] = product.field(default=0, **options)
        cls = product.dataclass(type("Pipeline", (), namespace))
        rhs = "7.4" if "converter" in options else "7"
        run, source = runner(f"obj.f0 = {rhs}", {"obj": cls()})
        result[label] = {
            "run": run,
            "source": source,
            "prepare": None,
            "classification": "extension policy cost; no std parity target",
        }
    lazy_cls = product.dataclass(
        type(
            "Lazy",
            (),
            {
                "__annotations__": {
                    "value": int,
                    **{f"f{i}": int for i in range(1, count)},
                },
                "__module__": __name__,
                "value": product.lazy(default_factory=lambda: 7),
                **{f"f{i}": i for i in range(1, count)},
            },
        )
    )
    run, source = runner("result = prepared[index].value", {})
    result["lazy_first"] = {
        "run": run,
        "source": source,
        "prepare": lambda n: [lazy_cls() for _ in range(n)],
        "classification": "fresh unready instance per operation; preparation outside clock",
    }

    def prepare_ready(n):
        pool = [lazy_cls() for _ in range(n)]
        for item in pool:
            item.value
        return pool

    run, source = runner("result = prepared[index].value", {})
    result["lazy_cached"] = {
        "run": run,
        "source": source,
        "prepare": prepare_ready,
        "classification": "separate ready instance per operation; pool initialization outside clock",
    }
    dependent_namespace = {
        "__annotations__": {"quantity": int, "price": int, "total": int},
        "__module__": __name__,
        "quantity": 2,
        "price": 3,
        "total": product.field(
            init=False, default_factory=lambda quantity, price: quantity * price
        ),
    }
    for index in range(3, count):
        name = f"f{index}"
        dependent_namespace["__annotations__"][name] = int
        dependent_namespace[name] = index
    dependent = product.dataclass(type("Dependent", (), dependent_namespace))
    run, source = runner("result = Cls()", {"Cls": dependent})
    result["construct_dependent"] = {
        "run": run,
        "source": source,
        "prepare": None,
        "classification": "extension; named factory plus ordinary fields",
    }
    return result


def readonly_cases(api, count, slots):
    obj = model(api, count, slots=slots, frozen=True)()
    result = {}
    for label, statement in (
        ("readonly_read", "result = obj.f0"),
        (
            "readonly_reject",
            "try:\n    obj.f0 = 7\nexcept FrozenInstanceError:\n    result = index",
        ),
    ):
        run, source = runner(
            statement, {"obj": obj, "FrozenInstanceError": std.FrozenInstanceError}
        )
        result[label] = {
            "run": run,
            "source": source,
            "prepare": None,
            "classification": "frozen implementation differs; no numerical parity target",
        }
    return result


def generation_cases(api, count, slots):
    def prepare(n):
        return [
            type(
                "RepeatedFields",
                (),
                {
                    "__module__": __name__,
                    "__annotations__": {f"f{i}": int for i in range(count)},
                    **{f"f{i}": i for i in range(count)},
                },
            )
            for _ in range(n)
        ]

    run, source = runner(
        "result = decorate(prepared[index])",
        {"decorate": api.dataclass(slots=slots, order=True)},
    )
    return {
        "decorate_repeated": {
            "run": run,
            "source": source,
            "prepare": prepare,
            "classification": "fresh declarations prepared outside each clock; in-process compiler caches may be warm",
        }
    }


def source_emission_case(product, count):
    # Capture the owned build result once during untimed setup. Do not modify SDKs.
    from yidl_dataclass import _generated_dataclass_base as generated

    original = generated.build_DataclassModule
    captures = []

    def capture(facts):
        piece = original(facts)
        captures.append(piece)
        return piece

    generated.build_DataclassModule = capture
    try:
        model(product, count)
    finally:
        generated.build_DataclassModule = original
    if len(captures) != 1:
        raise AssertionError(
            "expected one owned builder result during source-emission setup"
        )
    run, source = runner("result = piece.emit_commented()", {"piece": captures[0]})
    return {
        "run": run,
        "source": source,
        "prepare": None,
        "classification": "actual existing composable.emit_commented; build/decoration untimed; owned builder temporarily captured and restored during setup",
    }


def memory_models(product, count):
    """Memory inventory; values and classes prepared before allocation clock."""
    result = {
        "ordinary": {
            "cls": model(product, count),
            "inputs": "shared immutable integer defaults",
        },
        "frozen": {
            "cls": model(product, count, frozen=True),
            "inputs": "shared immutable integer defaults",
        },
        "weakref": {
            "cls": model(product, count, weakref_slot=True),
            "inputs": "shared immutable integer defaults",
        },
    }

    class Seed:
        def __init__(self):
            self.payload = bytearray(16)

    shared_seed = Seed()
    for label in (
        "local",
        "lazy_unready",
        "lazy_ready",
        "retained_shared",
        "retained_unique",
    ):
        namespace = {
            "__annotations__": {f"f{i}": int for i in range(count)},
            "__module__": __name__,
        }
        namespace.update({f"f{i}": i for i in range(count)})
        if label == "local":
            namespace["__annotations__"]["cache"] = dict
            namespace["cache"] = product.local_store(default_factory=dict)
        else:
            namespace["__annotations__"]["delayed"] = int
            if label.startswith("retained_"):
                namespace["__annotations__"]["seed"] = object
                namespace["seed"] = (
                    product.initvar(default=shared_seed)
                    if label == "retained_shared"
                    else product.initvar(default_factory=Seed)
                )
                namespace["delayed"] = product.lazy(
                    default_factory=lambda seed: seed.payload[0],
                    compare=False,
                    hash=False,
                    repr=False,
                )
            else:
                namespace["delayed"] = product.lazy(
                    default_factory=lambda: 7, compare=False, hash=False, repr=False
                )
        cls = product.dataclass(type("Memory", (), namespace))
        result[label] = {
            "cls": cls,
            "initialize_ready": label == "lazy_ready",
            "inputs": (
                "unique seed and bytearray per instance"
                if label == "retained_unique"
                else (
                    "shared seed prepared outside measurement"
                    if label == "retained_shared"
                    else (
                        "unique cache dict per instance"
                        if label == "local"
                        else "shared integer defaults"
                    )
                )
            ),
        }
    return result


def runner(statement, namespace, result="result"):
    body = "\n".join("        " + line for line in statement.splitlines())
    source = f"def measured(count, prepared):\n    result = None\n    for index in range(count):\n{body}\n    return {result}\n"
    exec(compile(source, "<benchmark-loop>", "exec"), namespace)
    return namespace["measured"], source


def ordinary_cases(api, count, slots):
    cls = model(api, count, slots=slots)
    factory_cls = model(api, count, slots=slots, factory=True)
    frozen_cls = model(api, count, slots=slots, frozen=True)
    obj = cls()
    equal = cls()
    early = cls()
    late = cls()
    larger = cls()
    early.f0 = -1
    setattr(late, f"f{count-1}", -1)
    larger.f0 = 1
    namespace = {
        "Cls": cls,
        "FactoryCls": factory_cls,
        "obj": obj,
        "equal": equal,
        "early": early,
        "late": late,
        "larger": larger,
        "frozen": frozen_cls(),
    }
    supplied = ",".join(map(str, range(count)))
    statements = {
        "slot_read": "result = obj.f0",
        "slot_write": "obj.f0 = 7",
        "construct_supplied": f"result = Cls({supplied})",
        "construct_defaults": "result = Cls()",
        "construct_factory": "result = FactoryCls()",
        "eq_equal": "result = obj == equal",
        "eq_early_mismatch": "result = obj == early",
        "eq_late_mismatch": "result = obj == late",
        "order": "result = obj < larger",
        "hash": "result = hash(frozen)",
        "repr": "result = repr(obj)",
    }
    # Each case receives separate instances: slot_write must not alter eq inputs.
    result = {}
    for name, statement in statements.items():
        local = namespace.copy()
        local["obj"] = cls()
        run, source = runner(statement, local)
        result[name] = {"run": run, "source": source, "prepare": None}
    return result
