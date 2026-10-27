"""Populate a model, then freeze it permanently without a transaction."""

from dataclasses import FrozenInstanceError
from yidl_dataclass import dataclass, field


@dataclass(freezable=True)
class Item:
    name: str


@dataclass(freezable=True)
class Catalog:
    title: str
    item: Item
    tags: object = field(default_factory=list, freeze=tuple)


def main():
    catalog = Catalog("draft", Item("initial"))
    catalog.title = "ready"
    catalog.item.name = "prepared"
    catalog.tags.append("release")
    catalog.freeze()
    assert catalog.tags == ("release",)
    # The resolved Item annotation infers freezing this same child object.
    for instance, name in ((catalog, "title"), (catalog.item, "name")):
        try:
            setattr(instance, name, "changed")
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("assignment succeeded after freeze")
    catalog.freeze()  # Repeating a completed freeze is a no-op.
    print("mutable-before; permanent-freeze; typed-child; immutable-container")


if __name__ == "__main__":
    main()
