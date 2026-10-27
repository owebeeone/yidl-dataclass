class Lazy(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = (
        "units",
        "_y_dc_store_2",
        "_y_dc_store_3",
        "_y_dc_store_4",
        "_y_dc_ready_2",
        "_y_dc_busy_2",
        "_y_dc_ready_3",
        "_y_dc_busy_3",
        "_y_dc_ready_4",
        "_y_dc_busy_4",
    )

    def __init__(
        self,
        units: _y_dc_annotation_0 = _y_dc_default_0,
        seeded: _y_dc_annotation_4 = _y_dc_factory_sentinel,
    ):
        pass
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        self._y_dc_ready_3 = False
        self._y_dc_busy_3 = False
        self._y_dc_ready_4 = False
        self._y_dc_busy_4 = False
        pass
        _y_dc_value_0 = units
        pass
        pass
        self.units = _y_dc_value_0
        _y_dc_value_1 = _y_dc_type(self).rate
        pass
        pass
        if seeded is not _y_dc_factory_sentinel:
            _y_dc_value_4 = seeded
            pass
            pass
            self._y_dc_store_4 = _y_dc_value_4
            self._y_dc_ready_4 = True
            pass
        pass

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        _y_cmp_result = self.units == other.units
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.total == other.total

    pass
    pass
    pass
    pass
    __hash__ = None
    pass

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self.units
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_store_3
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_store_4
        except AttributeError:
            pass
        try:
            _y_dc_state_values[4] = self._y_dc_ready_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[5] = self._y_dc_busy_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[6] = self._y_dc_ready_3
        except AttributeError:
            pass
        try:
            _y_dc_state_values[7] = self._y_dc_busy_3
        except AttributeError:
            pass
        try:
            _y_dc_state_values[8] = self._y_dc_ready_4
        except AttributeError:
            pass
        try:
            _y_dc_state_values[9] = self._y_dc_busy_4
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
            self.units = _y_dc_state_values[0]
        else:
            try:
                del self.units
            except AttributeError:
                pass
        if 1 in _y_dc_state_values:
            self._y_dc_store_2 = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_store_2
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_store_3 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_store_3
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_store_4 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_store_4
            except AttributeError:
                pass
        if 4 in _y_dc_state_values:
            self._y_dc_ready_2 = _y_dc_state_values[4]
        else:
            try:
                del self._y_dc_ready_2
            except AttributeError:
                pass
        if 5 in _y_dc_state_values:
            self._y_dc_busy_2 = _y_dc_state_values[5]
        else:
            try:
                del self._y_dc_busy_2
            except AttributeError:
                pass
        if 6 in _y_dc_state_values:
            self._y_dc_ready_3 = _y_dc_state_values[6]
        else:
            try:
                del self._y_dc_ready_3
            except AttributeError:
                pass
        if 7 in _y_dc_state_values:
            self._y_dc_busy_3 = _y_dc_state_values[7]
        else:
            try:
                del self._y_dc_busy_3
            except AttributeError:
                pass
        if 8 in _y_dc_state_values:
            self._y_dc_ready_4 = _y_dc_state_values[8]
        else:
            try:
                del self._y_dc_ready_4
            except AttributeError:
                pass
        if 9 in _y_dc_state_values:
            self._y_dc_busy_4 = _y_dc_state_values[9]
        else:
            try:
                del self._y_dc_busy_4
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

    def _y_dc_get_2(self):
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2(
                    units=self.units, rate=_y_dc_type(self).rate, cls=_y_dc_type(self)
                )
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    _y_dc_factory_message_2
                ) from _y_dc_factory_error
            pass
            pass
            self._y_dc_store_2 = _y_dc_lazy_value
            self._y_dc_ready_2 = True
            pass
            return self._y_dc_store_2
        finally:
            self._y_dc_busy_2 = False

    def _y_dc_set_2(self, value):
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    def _y_dc_del_2(self):
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    total = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

    def _y_dc_get_3(self):
        if self._y_dc_ready_3:
            return self._y_dc_store_3
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        self._y_dc_busy_3 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_3(units=self.units)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    _y_dc_factory_message_3
                ) from _y_dc_factory_error
            try:
                _y_dc_lazy_processed = _y_dc_converter_3(_y_dc_lazy_value)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_conversion_error:
                raise _y_dc_FieldConversionError(
                    _y_dc_conversion_message_3
                ) from _y_dc_conversion_error
            try:
                _y_dc_validation_result = _y_dc_validator_3(_y_dc_lazy_processed)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_validation_error:
                raise _y_dc_FieldValidationError(
                    _y_dc_validation_message_3
                ) from _y_dc_validation_error
            try:
                if _y_dc_validation_result is False:
                    raise _y_dc_FieldValidationError(_y_dc_validation_rejected_3)
                if (
                    _y_dc_validation_result is not None
                    and _y_dc_validation_result is not True
                ):
                    raise _y_dc_TypeError(_y_dc_validation_contract_3)
            finally:
                del _y_dc_validation_result
            self._y_dc_store_3 = _y_dc_lazy_processed
            self._y_dc_ready_3 = True
            pass
            return self._y_dc_store_3
        finally:
            self._y_dc_busy_3 = False

    def _y_dc_set_3(self, value):
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        try:
            _y_dc_lazy_processed = _y_dc_converter_3(value)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(
                _y_dc_conversion_message_3
            ) from _y_dc_conversion_error
        try:
            _y_dc_validation_result = _y_dc_validator_3(_y_dc_lazy_processed)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_validation_error:
            raise _y_dc_FieldValidationError(
                _y_dc_validation_message_3
            ) from _y_dc_validation_error
        try:
            if _y_dc_validation_result is False:
                raise _y_dc_FieldValidationError(_y_dc_validation_rejected_3)
            if (
                _y_dc_validation_result is not None
                and _y_dc_validation_result is not True
            ):
                raise _y_dc_TypeError(_y_dc_validation_contract_3)
        finally:
            del _y_dc_validation_result
        self._y_dc_store_3 = _y_dc_lazy_processed
        self._y_dc_ready_3 = True
        pass

    def _y_dc_del_3(self):
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        if self._y_dc_ready_3:
            del self._y_dc_store_3
        self._y_dc_ready_3 = False

    cache = _y_dc_property(_y_dc_get_3, _y_dc_set_3, _y_dc_del_3)

    def _y_dc_get_4(self):
        if self._y_dc_ready_4:
            return self._y_dc_store_4
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_4)
        self._y_dc_busy_4 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_4(units=self.units)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    _y_dc_factory_message_4
                ) from _y_dc_factory_error
            pass
            pass
            self._y_dc_store_4 = _y_dc_lazy_value
            self._y_dc_ready_4 = True
            pass
            return self._y_dc_store_4
        finally:
            self._y_dc_busy_4 = False

    def _y_dc_set_4(self, value):
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_4)
        pass
        pass
        self._y_dc_store_4 = value
        self._y_dc_ready_4 = True
        pass

    def _y_dc_del_4(self):
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_4)
        if self._y_dc_ready_4:
            del self._y_dc_store_4
        self._y_dc_ready_4 = False

    seeded = _y_dc_property(_y_dc_get_4, _y_dc_set_4, _y_dc_del_4)


class Eager(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("result", "_y_dc_store_1", "base", "_y_dc_ready_1", "_y_dc_busy_1")

    def __init__(self, base: _y_dc_annotation_2 = _y_dc_default_2):
        pass
        self._y_dc_ready_1 = False
        self._y_dc_busy_1 = False
        pass
        _y_dc_value_2 = base
        pass
        pass
        self.base = _y_dc_value_2
        _y_dc_value_1 = self.delayed
        try:
            _y_dc_value_0 = _y_dc_factory_0(delayed=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Eager.result: factory failed"
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
        _y_cmp_result = self.delayed == other.delayed
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.base == other.base

    pass
    pass
    pass
    pass
    __hash__ = None
    pass

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self.result
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self.base
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_ready_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[4] = self._y_dc_busy_1
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
            self.result = _y_dc_state_values[0]
        else:
            try:
                del self.result
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
            self.base = _y_dc_state_values[2]
        else:
            try:
                del self.base
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_ready_1 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_ready_1
            except AttributeError:
                pass
        if 4 in _y_dc_state_values:
            self._y_dc_busy_1 = _y_dc_state_values[4]
        else:
            try:
                del self._y_dc_busy_1
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

    def _y_dc_get_1(self):
        if self._y_dc_ready_1:
            return self._y_dc_store_1
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        self._y_dc_busy_1 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_1(base=self.base)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    _y_dc_factory_message_1
                ) from _y_dc_factory_error
            pass
            pass
            self._y_dc_store_1 = _y_dc_lazy_value
            self._y_dc_ready_1 = True
            pass
            return self._y_dc_store_1
        finally:
            self._y_dc_busy_1 = False

    def _y_dc_set_1(self, value):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)

    def _y_dc_del_1(self):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)

    delayed = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)
