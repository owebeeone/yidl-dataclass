"""A failed freeze leaves earlier field transformations in place."""
from dataclasses import FrozenInstanceError
from yidl_dataclass import dataclass, field


attempts = []


def finish(value):
    attempts.append(value)
    if len(attempts) == 1:
        raise ValueError("try again")
    return value


@dataclass(freezable=True)
class Draft:
    tags: object = field(freeze=tuple)
    status: str = field(freeze=finish)


def main():
    draft = Draft(["one"], "ready")
    try:
        draft.freeze()
    except ValueError as error:
        assert str(error) == "try again"
    else:
        raise AssertionError("expected hook failure")
    assert draft.tags == ("one",)  # Earlier transformation was not rolled back.
    draft.status = "retry"  # The parent has not completed freezing.
    draft.freeze()  # tuple also accepts a tuple, so the earlier hook is retry-safe.
    assert attempts == ["ready", "retry"]
    try:
        draft.status = "changed"
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("freeze should block assignment")
    print("partial-transformation; mutable-parent-after-failure; successful-retry")


if __name__ == "__main__":
    main()
