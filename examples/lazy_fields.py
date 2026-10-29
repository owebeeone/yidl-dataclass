"""Lazy values are computed on access, cached, and explicitly reset."""
from yidl_dataclass import dataclass, initvar, lazy


calls = []


def render(source, heading):
    calls.append(heading)
    return f"{heading}: {source}"


@dataclass
class Document:
    heading: str
    source: str = initvar()
    preview: str = lazy(default_factory=render, mutable=True, repr=False, compare=False)


def main():
    document = Document("Draft", "body")
    assert not calls
    document.heading = "Ready"
    assert document.preview == "Ready: body"
    assert document.preview == "Ready: body"
    assert calls == ["Ready"]
    document.heading = "Final"
    assert document.preview == "Ready: body"
    del document.preview
    assert document.preview == "Final: body"
    assert calls == ["Ready", "Final"]
    print("delayed-access; cached-value; explicit-reset; retained-initvar")


if __name__ == "__main__":
    main()
