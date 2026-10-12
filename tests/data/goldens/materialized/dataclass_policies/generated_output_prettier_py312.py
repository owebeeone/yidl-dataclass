class Processed(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("total", "_y_dc_store_1", "_y_dc_store_2", "management")

    def __init__(
        self,
        units: _y_dc_annotation_1 = _y_dc_default_1,
        token: _y_dc_annotation_2 = _y_dc_default_2,
    ) -> None:
        pass
        _y_dc_value_1 = units
        try:
            _y_dc_value_1 = _y_dc_converter_1(_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_1
            ) from _y_dc_conversion_error
        try:
            _y_dc_validation_result = _y_dc_validator_1(_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_validation_error:
            raise _y_dc_FieldValidationError(
                _y_dc_validation_message_1
            ) from _y_dc_validation_error
        try:
            if _y_dc_validation_result is False:
                raise _y_dc_FieldValidationError(_y_dc_validation_rejected_1)
            if (
                _y_dc_validation_result is not None
                and _y_dc_validation_result is not True
            ):
                raise _y_dc_TypeError(_y_dc_validation_contract_1)
        finally:
            del _y_dc_validation_result
        self._y_dc_store_1 = _y_dc_value_1
        try:
            _y_dc_value_0 = _y_dc_factory_0(units=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Processed.total: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.total = _y_dc_value_0
        _y_dc_value_2 = token
        pass
        pass
        self._y_dc_store_2 = _y_dc_value_2
        try:
            _y_dc_value_3 = _y_dc_factory_3(units=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Processed.management: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_3

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.total if True else None,
            self.units if True else None,
            self.token if True else None,
        ) == (
            other.total if True else None,
            other.units if True else None,
            other.token if True else None,
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
                (
                    "total" + "=" + repr(self.total),
                    "units" + "=" + repr(self.units),
                    "token" + "=" + repr(self.token),
                )
            )
            + ")"
        )

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self.total
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self.management
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
            self.total = _y_dc_state_values[0]
        else:
            try:
                del self.total
            except AttributeError:
                pass
        if 1 in _y_dc_state_values:
            self._y_dc_store_1 = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_store_1
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_store_2 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_store_2
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self.management = _y_dc_state_values[3]
        else:
            try:
                del self.management
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

    pass
    pass

    def _y_dc_get_1(self):
        return self._y_dc_store_1

    def _y_dc_set_1(self, value):
        try:
            _y_dc_lazy_processed = _y_dc_converter_1(value)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_1
            ) from _y_dc_conversion_error
        try:
            _y_dc_validation_result = _y_dc_validator_1(_y_dc_lazy_processed)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_validation_error:
            raise _y_dc_FieldValidationError(
                _y_dc_validation_message_1
            ) from _y_dc_validation_error
        try:
            if _y_dc_validation_result is False:
                raise _y_dc_FieldValidationError(_y_dc_validation_rejected_1)
            if (
                _y_dc_validation_result is not None
                and _y_dc_validation_result is not True
            ):
                raise _y_dc_TypeError(_y_dc_validation_contract_1)
        finally:
            del _y_dc_validation_result
        self._y_dc_store_1 = _y_dc_lazy_processed

    def _y_dc_del_1(self):
        del self._y_dc_store_1

    units = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

    def _y_dc_get_2(self):
        return self._y_dc_store_2

    def _y_dc_set_2(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    def _y_dc_del_2(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    token = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)


class Frozen(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("_y_dc_store_0", "cache", "management")

    def __init__(
        self,
        amount: _y_dc_annotation_0,
        cache: _y_dc_annotation_1 = _y_dc_factory_sentinel,
    ) -> None:
        pass
        _y_dc_value_0 = amount
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0
        if cache is _y_dc_factory_sentinel:
            try:
                _y_dc_value_1 = _y_dc_factory_1()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    "render_case.<locals>.Frozen.cache: factory failed"
                ) from _y_dc_factory_error
        else:
            _y_dc_value_1 = cache
        pass
        pass
        self.cache = _y_dc_value_1
        try:
            _y_dc_value_2 = _y_dc_factory_2()
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Frozen.management: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_2

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.amount if True else None,) == (other.amount if True else None,)

    pass
    pass
    pass
    pass

    def __hash__(self):
        return hash((self.amount if True else None,))

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("amount" + "=" + repr(self.amount),))
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
            _y_dc_state_values[1] = self.cache
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self.management
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
            self.cache = _y_dc_state_values[1]
        else:
            try:
                del self.cache
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self.management = _y_dc_state_values[2]
        else:
            try:
                del self.management
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

    pass
    pass

    def _y_dc_get_0(self):
        return self._y_dc_store_0

    def _y_dc_set_0(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)

    def _y_dc_del_0(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)

    amount = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)
