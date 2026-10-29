"""Named factories, hidden constructor inputs and field pipelines."""
from yidl_dataclass import asdict, dataclass, field, initvar, local_store


def total_for(quantity, price):
    return quantity * price


def reference_for(prefix, cls):
    return f"{prefix}-{cls.__name__}"


@dataclass
class Order:
    quantity: int = field(converter=int, validator=lambda value: value > 0)
    price: int = field(converter=int, validator=lambda value: value >= 0)
    prefix: str = initvar(default="WEB")
    total: int = field(init=False, default_factory=total_for)
    reference: str = field(init=False, default_factory=reference_for)
    cache: dict = local_store(default_factory=dict)


def main():
    order = Order("2", "15")
    assert order.total == 30
    assert order.reference == "WEB-Order"
    assert not hasattr(order, "prefix")
    assert "cache" not in asdict(order)
    order.quantity = "3"
    assert order.quantity == 3
    assert order.total == 30  # Factories initialize; they are not reactive formulas.
    print("named-providers; converted-input; hidden-initvar; independent-cache")


if __name__ == "__main__":
    main()
