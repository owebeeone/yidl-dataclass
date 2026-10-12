"""Introductory ordinary-field model; works from an installed consumer wheel."""

from yidl_dataclass import dataclass, field, fields, asdict, replace


@dataclass
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list, compare=False, repr=False)


def main():
    first = Inventory(3)
    second = Inventory(3)
    first.tags.append("reviewed")
    assert first == second and second.tags == []
    first.count = 4
    assert not hasattr(first, "__dict__")
    assert replace(first, count=5).count == 5
    assert [item.name for item in fields(first)] == ["count", "label", "tags"]
    assert asdict(first) == {"count": 4, "label": "stock", "tags": ["reviewed"]}
    print(
        "ordinary-slots; independent-factories; field-local-comparison; standard-helpers"
    )


if __name__ == "__main__":
    main()
