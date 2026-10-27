class Child(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0', '_y_dc_frozen', '_y_dc_freezing')

    def __init__(self, value: _y_dc_annotation_0):
        self._y_dc_frozen = False
        self._y_dc_freezing = False
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
        if self._y_dc_freezing:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_frozen
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_freezing
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
        if 1 in _y_dc_state_values:
            self._y_dc_frozen = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_frozen
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_freezing = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_freezing
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
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        pass
        pass
        self._y_dc_store_0 = value

    def _y_dc_del_0(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        del self._y_dc_store_0
    value = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

    def freeze(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False) or _y_dc_getattr(self, '_y_dc_freezing', False):
            return
        self._y_dc_freezing = True
        try:
            pass
            _y_dc_freeze_value = self.value
            self._y_dc_frozen = True
        finally:
            self._y_dc_freezing = False

class Parent(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0', '_y_dc_frozen', '_y_dc_freezing')

    def __init__(self, child: _y_dc_annotation_0):
        self._y_dc_frozen = False
        self._y_dc_freezing = False
        pass
        _y_dc_value_0 = child
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.child if True else None,) == (other.child if True else None,)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('child' + '=' + repr(self.child),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        if self._y_dc_freezing:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_frozen
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_freezing
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
        if 1 in _y_dc_state_values:
            self._y_dc_frozen = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_frozen
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_freezing = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_freezing
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
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        pass
        pass
        self._y_dc_store_0 = value

    def _y_dc_del_0(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        del self._y_dc_store_0
    child = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

    def freeze(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False) or _y_dc_getattr(self, '_y_dc_freezing', False):
            return
        self._y_dc_freezing = True
        try:
            pass
            self._y_dc_store_0 = _y_dc_freeze_0(self.child)
            self._y_dc_frozen = True
        finally:
            self._y_dc_freezing = False

class Explicit(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0', '_y_dc_frozen', '_y_dc_freezing')

    def __init__(self, child: _y_dc_annotation_0):
        self._y_dc_frozen = False
        self._y_dc_freezing = False
        pass
        _y_dc_value_0 = child
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.child if True else None,) == (other.child if True else None,)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('child' + '=' + repr(self.child),)) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        if self._y_dc_freezing:
            raise _y_dc_LazyInitializationError(_y_dc_copy_busy_message)
        pass
        try:
            _y_dc_state_values[0] = self._y_dc_store_0
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self._y_dc_frozen
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_freezing
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
        if 1 in _y_dc_state_values:
            self._y_dc_frozen = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_frozen
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_freezing = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_freezing
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
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        pass
        pass
        self._y_dc_store_0 = value

    def _y_dc_del_0(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
        del self._y_dc_store_0
    child = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

    def freeze(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False) or _y_dc_getattr(self, '_y_dc_freezing', False):
            return
        self._y_dc_freezing = True
        try:
            pass
            self._y_dc_store_0 = _y_dc_freeze_0(self.child)
            self._y_dc_frozen = True
        finally:
            self._y_dc_freezing = False
