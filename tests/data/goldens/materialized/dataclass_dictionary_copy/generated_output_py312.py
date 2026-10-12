class Dictionary(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    pass

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_default_0):
        pass
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        self._y_dc_ready_3 = False
        self._y_dc_busy_3 = False
        pass
        _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        _y_dc_value_1 = self.source
        pass
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.source if True else None, self.first if True else None) == (other.source if True else None, other.first if True else None)
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
        pass
        return (1, _y_dc_state_values, self.__dict__.copy())

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (type(state[2]) is not dict):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        self.__dict__.clear()
        self.__dict__.update(state[2])
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
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2(source=self.source)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_2) from _y_dc_factory_error
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
    first = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

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
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_3) from _y_dc_factory_error
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
        pass
        pass
        self._y_dc_store_3 = value
        self._y_dc_ready_3 = True
        pass

    def _y_dc_del_3(self):
        if self._y_dc_busy_3:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_3)
        if self._y_dc_ready_3:
            del self._y_dc_store_3
        self._y_dc_ready_3 = False
    second = _y_dc_property(_y_dc_get_3, _y_dc_set_3, _y_dc_del_3)
