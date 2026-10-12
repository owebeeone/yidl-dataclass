class Owned(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ("_y_dc_store_0", "untouched")

    def __init__(
        self,
        value: _y_dc_annotation_0 = _y_dc_default_0,
        untouched: _y_dc_annotation_1 = _y_dc_default_1,
    ) -> None:
        pass
        _y_dc_value_0 = value
        try:
            _y_dc_value_0 = _y_dc_converter_0(_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_value_0
        _y_dc_value_1 = untouched
        pass
        pass
        self.untouched = _y_dc_value_1

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.value if True else None,) == (other.value if True else None,)

    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )

    @property
    def value(self):
        return self._y_dc_store_0

    @value.setter
    def value(self, value):
        try:
            value = _y_dc_converter_0(value)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = value

    @value.deleter
    def value(self):
        del self._y_dc_store_0


class Owned(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ("_y_dc_store_0", "untouched")

    def __init__(
        self,
        value: _y_dc_annotation_0 = _y_dc_default_0,
        untouched: _y_dc_annotation_1 = _y_dc_default_1,
    ) -> None:
        pass
        _y_dc_value_0 = value
        try:
            _y_dc_value_0 = _y_dc_converter_0(_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_value_0
        _y_dc_value_1 = untouched
        pass
        pass
        self.untouched = _y_dc_value_1

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.value if True else None,) == (other.value if True else None,)

    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )

    @property
    def value(self):
        return self._y_dc_store_0

    @value.setter
    def value(self, value):
        try:
            value = _y_dc_converter_0(value)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = value

    @value.deleter
    def value(self):
        del self._y_dc_store_0


class Removed(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0 = _y_dc_default_0) -> None:
        pass
        self.value = value

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.value if True else None,) == (other.value if True else None,)

    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )


class Fallback(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    pass

    def __init__(self) -> None:
        pass
        _y_dc_value_1 = self.source
        try:
            _y_dc_value_0 = _y_dc_factory_0(source=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Fallback.result: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.result = _y_dc_value_0

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.result if True else None, self.source if True else None) == (
            other.result if True else None,
            other.source if True else None,
        )

    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(
                ("result" + "=" + repr(self.result), "source" + "=" + repr(self.source))
            )
            + ")"
        )
