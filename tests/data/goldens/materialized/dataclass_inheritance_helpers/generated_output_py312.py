class BaseDeclaration(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('units', '_y_dc_store_1')

    def __init__(self, units: _y_dc_annotation_0=_y_dc_default_0, token: _y_dc_annotation_1=_y_dc_default_1) -> None:
        pass
        _y_dc_value_0 = units
        pass
        pass
        self.units = _y_dc_value_0
        _y_dc_value_1 = token
        pass
        pass
        self._y_dc_store_1 = _y_dc_value_1

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.units if True else None, self.token if True else None) == (other.units if True else None, other.token if True else None)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('units' + '=' + repr(self.units), 'token' + '=' + repr(self.token))) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self.units
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_1
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
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
            self._y_dc_store_1 = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_store_1
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
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)

    def _y_dc_del_1(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)
    token = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

class Child(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('tag',)

    def __init__(self, units: _y_dc_annotation_0=_y_dc_default_0, token: _y_dc_annotation_1=_y_dc_default_1, tag: _y_dc_annotation_2=_y_dc_default_2) -> None:
        pass
        _y_dc_value_0 = units
        pass
        pass
        self.units = _y_dc_value_0
        _y_dc_value_1 = token
        pass
        pass
        self._y_dc_store_1 = _y_dc_value_1
        _y_dc_value_2 = tag
        pass
        pass
        self.tag = _y_dc_value_2

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.units if True else None, self.token if True else None, self.tag if True else None) == (other.units if True else None, other.token if True else None, other.tag if True else None)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('units' + '=' + repr(self.units), 'token' + '=' + repr(self.token), 'tag' + '=' + repr(self.tag))) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self.units
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self.tag
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
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
            self._y_dc_store_1 = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_store_1
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self.tag = _y_dc_state_values[2]
        else:
            try:
                del self.tag
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
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)

    def _y_dc_del_1(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)
    token = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

class LazyBase(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_1', '_y_dc_store_2', '_y_dc_ready_1', '_y_dc_busy_1', '_y_dc_ready_2', '_y_dc_busy_2', '_y_dc_provider_0')

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_factory_sentinel):
        pass
        self._y_dc_ready_1 = False
        self._y_dc_busy_1 = False
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('LazyBase.seed: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        pass
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return True
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
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_ready_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_busy_1
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
            _y_dc_state_values[6] = self._y_dc_provider_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_1 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_1
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
            self._y_dc_ready_1 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_ready_1
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_busy_1 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_busy_1
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
            self._y_dc_provider_0 = _y_dc_state_values[6]
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

    def _y_dc_get_1(self):
        if self._y_dc_ready_1:
            return self._y_dc_store_1
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        self._y_dc_busy_1 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_1(self=self, seed=self._y_dc_provider_0)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_1) from _y_dc_factory_error
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
        pass
        pass
        self._y_dc_store_1 = value
        self._y_dc_ready_1 = True
        pass

    def _y_dc_del_1(self):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        if self._y_dc_ready_1:
            del self._y_dc_store_1
        self._y_dc_ready_1 = False
    value = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

    def _y_dc_get_2(self):
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2()
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
    readonly = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

class LazyChild(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ()

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_factory_sentinel):
        pass
        self._y_dc_ready_1 = False
        self._y_dc_busy_1 = False
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('LazyChild.seed: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        pass
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return True
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
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_ready_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_busy_1
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
            _y_dc_state_values[6] = self._y_dc_provider_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_1 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_1
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
            self._y_dc_ready_1 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_ready_1
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_busy_1 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_busy_1
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
            self._y_dc_provider_0 = _y_dc_state_values[6]
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

    def _y_dc_get_1(self):
        if self._y_dc_ready_1:
            return self._y_dc_store_1
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        self._y_dc_busy_1 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_1(self=self, seed=self._y_dc_provider_0)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_1) from _y_dc_factory_error
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
        pass
        pass
        self._y_dc_store_1 = value
        self._y_dc_ready_1 = True
        pass

    def _y_dc_del_1(self):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        if self._y_dc_ready_1:
            del self._y_dc_store_1
        self._y_dc_ready_1 = False
    value = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

    def _y_dc_get_2(self):
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2()
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
    readonly = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

class LazyGrandchild(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ()

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_factory_sentinel):
        pass
        self._y_dc_ready_1 = False
        self._y_dc_busy_1 = False
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('LazyGrandchild.seed: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        pass
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return True
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
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_ready_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_busy_1
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
            _y_dc_state_values[6] = self._y_dc_provider_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_1 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_1
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
            self._y_dc_ready_1 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_ready_1
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_busy_1 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_busy_1
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
            self._y_dc_provider_0 = _y_dc_state_values[6]
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

    def _y_dc_get_1(self):
        if self._y_dc_ready_1:
            return self._y_dc_store_1
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        self._y_dc_busy_1 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_1(self=self, seed=self._y_dc_provider_0)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_1) from _y_dc_factory_error
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
        pass
        pass
        self._y_dc_store_1 = value
        self._y_dc_ready_1 = True
        pass

    def _y_dc_del_1(self):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        if self._y_dc_ready_1:
            del self._y_dc_store_1
        self._y_dc_ready_1 = False
    value = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

    def _y_dc_get_2(self):
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2()
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
    readonly = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

class LazyOverride(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ()

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_factory_sentinel):
        pass
        self._y_dc_ready_1 = False
        self._y_dc_busy_1 = False
        self._y_dc_ready_2 = False
        self._y_dc_busy_2 = False
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('LazyOverride.seed: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        self._y_dc_provider_0 = _y_dc_value_0
        pass
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return True
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
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_ready_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_busy_1
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
            _y_dc_state_values[6] = self._y_dc_provider_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_1 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_1
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
            self._y_dc_ready_1 = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_ready_1
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_busy_1 = _y_dc_state_values[3]
        else:
            try:
                del self._y_dc_busy_1
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
            self._y_dc_provider_0 = _y_dc_state_values[6]
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

    def _y_dc_get_1(self):
        if self._y_dc_ready_1:
            return self._y_dc_store_1
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        self._y_dc_busy_1 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_1(self=self, seed=self._y_dc_provider_0)
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(_y_dc_factory_message_1) from _y_dc_factory_error
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
        pass
        pass
        self._y_dc_store_1 = value
        self._y_dc_ready_1 = True
        pass

    def _y_dc_del_1(self):
        if self._y_dc_busy_1:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_1)
        if self._y_dc_ready_1:
            del self._y_dc_store_1
        self._y_dc_ready_1 = False
    value = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)

    def _y_dc_get_2(self):
        if self._y_dc_ready_2:
            return self._y_dc_store_2
        if self._y_dc_busy_2:
            raise _y_dc_LazyInitializationError(_y_dc_lazy_message_2)
        self._y_dc_busy_2 = True
        try:
            try:
                _y_dc_lazy_value = _y_dc_factory_2()
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
    readonly = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)
