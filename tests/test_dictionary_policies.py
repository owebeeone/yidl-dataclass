"""Test-first dictionary-mode declaration cleanup and private policy storage."""

from yidl_dataclass import dataclass, initvar, field, const


def test_dictionary_hidden_provider_has_no_declared_public_default():
    @dataclass(slots=False)
    class DictionaryProvider:
        seed: int = initvar(default=3)
        value: int = field(init=False, default_factory=lambda seed: seed * 2)

    instance = DictionaryProvider()
    assert instance.value == 6
    assert not hasattr(DictionaryProvider, "seed")
    assert not hasattr(instance, "seed")
    assert "seed" not in instance.__dict__


def test_dictionary_absent_field_does_not_fall_back_to_declaration_marker():
    @dataclass(slots=False)
    class Absent:
        value: int = field(init=False, repr=False, compare=False)

    assert not hasattr(Absent, "value")
    assert not hasattr(Absent(), "value")
