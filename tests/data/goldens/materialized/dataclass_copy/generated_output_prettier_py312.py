class CopyModel(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = (
        "values",
        "_y_dc_store_2",
        "_y_dc_store_3",
        "_y_dc_store_4",
        "management",
        "loop",
        "_y_dc_ready_3",
        "_y_dc_busy_3",
        "_y_dc_ready_4",
        "_y_dc_busy_4",
        "_y_dc_provider_0",
    )

    def __init__(
        self,
        seed: _y_dc_annotation_0 = _y_dc_factory_sentinel,
        values: _y_dc_annotation_1 = _y_dc_factory_sentinel,
        readonly: _y_dc_annotation_2 = _y_dc_default_2,
        loop: _y_dc_annotation_6 = _y_dc_default_6,
    ):
        pass
        self._y_dc_ready_3 = False
        self._y_dc_busy_3 = False
        self._y_dc_ready_4 = False
        self._y_dc_busy_4 = False
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    "CopyModel.seed: factory failed"
                ) from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        if values is _y_dc_factory_sentinel:
            try:
                _y_dc_value_1 = _y_dc_factory_1()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    "CopyModel.values: factory failed"
                ) from _y_dc_factory_error
        else:
            _y_dc_value_1 = values
        pass
        pass
        self.values = _y_dc_value_1
        _y_dc_value_2 = readonly
        pass
        pass
        self._y_dc_store_2 = _y_dc_value_2
        pass
        pass
        try:
            _y_dc_value_5 = _y_dc_factory_5()
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "CopyModel.management: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_5
        _y_dc_value_6 = loop
        pass
        pass
        self.loop = _y_dc_value_6

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.readonly if True else None,) == (other.readonly if True else None,)

    pass
    pass
    pass
    pass
    __hash__ = None
    pass

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self.values
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
            _y_dc_state_values[4] = self.management
        except AttributeError:
            pass
        try:
            _y_dc_state_values[5] = self.loop
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
        try:
            _y_dc_state_values[10] = self._y_dc_provider_0
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
            self.values = _y_dc_state_values[0]
        else:
            try:
                del self.values
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
            self.management = _y_dc_state_values[4]
        else:
            try:
                del self.management
            except AttributeError:
                pass
        if 5 in _y_dc_state_values:
            self.loop = _y_dc_state_values[5]
        else:
            try:
                del self.loop
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
        if 10 in _y_dc_state_values:
            self._y_dc_provider_0 = _y_dc_state_values[10]
        else:
            try:
                del self._y_dc_provider_0
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

    def _y_dc_get_2(self):
        return self._y_dc_store_2

    def _y_dc_set_2(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    def _y_dc_del_2(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    readonly = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

    def _y_dc_get_3(self):
        if self._y_dc_ready_3:
            return self._y_dc_store_3
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        self._y_dc_busy_3 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_3(seed=self._y_dc_provider_0)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    _y_dc_factory_message_3
                ) from _y_dc_factory_error
            pass
            pass
            self._y_dc_store_3 = _y_dc_lazy_value
            self._y_dc_ready_3 = True
            pass
            return self._y_dc_store_3
        finally:
            self._y_dc_busy_3 = False

    def _y_dc_set_3(self, value):
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_3)

    def _y_dc_del_3(self):
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_3)

    cache = _y_dc_property(_y_dc_get_3, _y_dc_set_3, _y_dc_del_3)

    def _y_dc_get_4(self):
        if self._y_dc_ready_4:
            return self._y_dc_store_4
        if self._y_dc_busy_4:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_4)
        self._y_dc_busy_4 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_4(seed=self._y_dc_provider_0)
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

    reset = _y_dc_property(_y_dc_get_4, _y_dc_set_4, _y_dc_del_4)
