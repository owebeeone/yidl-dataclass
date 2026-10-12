class type(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

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
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

class tuple(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

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
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

class dict(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

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
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

class int(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

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
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

class hash(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.value if True else None,) == (other.value if True else None,)
    pass
    pass
    pass
    pass

    def __hash__(self):
        return hash((self.value if True else None,))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

class _y_dc_converter_0(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0',)

    def __init__(self, value: _y_dc_annotation_0=_y_dc_default_0) -> None:
        pass
        _y_dc_value_0 = value
        try:
            _y_dc_value_0 = _y_dc_converter_0(_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(_y_dc_conversion_message_0) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_value_0

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
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self._y_dc_store_0 = _y_dc_state_values[0]
        else:
            try:
                del self._y_dc_store_0
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
        try:
            _y_dc_lazy_processed = _y_dc_converter_0(value)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(_y_dc_conversion_message_0) from _y_dc_conversion_error
        pass
        self._y_dc_store_0 = _y_dc_lazy_processed

    def _y_dc_del_0(self):
        del self._y_dc_store_0
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)
