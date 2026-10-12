class Owned(*_y_dc_bases, metaclass=_y_dc_metaclass):
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
        except _y_dc_Exception as _y_dc_conversion_error:
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
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.value == other.value

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

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self.untouched
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if (
            type(state) is not tuple
            or len(state) != 3
            or type(state[0]) is not int
            or (state[0] != 1)
            or (type(state[1]) is not dict)
            or (state[2] is not None)
        ):
            raise ValueError("unsupported dataclass state schema")
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
            except AttributeError:
                pass
        if 1 in _y_dc_state_values:
            self.untouched = _y_dc_state_values[1]
        else:
            try:
                del self.untouched
            except AttributeError:
                pass

    def __copy__(self):
        _y_dc_clone = object.__new__(type(self))
        _y_dc_clone.__setstate__(self.__getstate__())
        return _y_dc_clone

    def __deepcopy__(self, memo):
        _y_dc_state = self.__getstate__()
        _y_dc_clone = object.__new__(type(self))
        memo[id(self)] = _y_dc_clone
        _y_dc_clone.__setstate__(_y_dc_deepcopy(_y_dc_state, memo))
        return _y_dc_clone

    def __reduce_ex__(self, protocol):
        return (_y_dc_restore, (type(self),), self.__getstate__())

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)

    pass

    def _y_dc_get_0(self):
        return self._y_dc_store_0

    def _y_dc_set_0(self, value):
        try:
            _y_dc_lazy_processed = _y_dc_converter_0(value)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_lazy_processed

    def _y_dc_del_0(self):
        del self._y_dc_store_0

    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)


class Owned(*_y_dc_bases, metaclass=_y_dc_metaclass):
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
        except _y_dc_Exception as _y_dc_conversion_error:
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
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.value == other.value

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

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self.untouched
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if (
            type(state) is not tuple
            or len(state) != 3
            or type(state[0]) is not int
            or (state[0] != 1)
            or (type(state[1]) is not dict)
            or (state[2] is not None)
        ):
            raise ValueError("unsupported dataclass state schema")
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
            except AttributeError:
                pass
        if 1 in _y_dc_state_values:
            self.untouched = _y_dc_state_values[1]
        else:
            try:
                del self.untouched
            except AttributeError:
                pass

    def __copy__(self):
        _y_dc_clone = object.__new__(type(self))
        _y_dc_clone.__setstate__(self.__getstate__())
        return _y_dc_clone

    def __deepcopy__(self, memo):
        _y_dc_state = self.__getstate__()
        _y_dc_clone = object.__new__(type(self))
        memo[id(self)] = _y_dc_clone
        _y_dc_clone.__setstate__(_y_dc_deepcopy(_y_dc_state, memo))
        return _y_dc_clone

    def __reduce_ex__(self, protocol):
        return (_y_dc_restore, (type(self),), self.__getstate__())

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)

    pass

    def _y_dc_get_0(self):
        return self._y_dc_store_0

    def _y_dc_set_0(self, value):
        try:
            _y_dc_lazy_processed = _y_dc_converter_0(value)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_0
            ) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_lazy_processed

    def _y_dc_del_0(self):
        del self._y_dc_store_0

    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)


class Different(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("quantity",)

    def __init__(self, quantity: _y_dc_annotation_0 = _y_dc_factory_sentinel) -> None:
        pass
        if quantity is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    "render_case.<locals>.Different.quantity: factory failed"
                ) from _y_dc_factory_error
        else:
            _y_dc_value_0 = quantity
        pass
        pass
        self.quantity = _y_dc_value_0

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.quantity == other.quantity

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
            + ", ".join(("quantity" + "=" + repr(self.quantity),))
            + ")"
        )

    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)

    pass


class Removed(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0 = _y_dc_default_0) -> None:
        pass
        self.value = value

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.value == other.value

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

    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)

    pass


class Fallback(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    pass

    def __init__(self) -> None:
        pass
        _y_dc_value_1 = self.source
        try:
            _y_dc_value_0 = _y_dc_factory_0(source=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Fallback.result: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.result = _y_dc_value_0

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        _y_cmp_result = self.result == other.result
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.source == other.source

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

    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)

    pass
