class Scope(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0', '_y_dc_store_1', '_y_dc_frozen', '_y_dc_freezing')

    def __init__(self, name: _y_dc_annotation_0, children: _y_dc_annotation_1=_y_dc_factory_sentinel):
        self._y_dc_frozen = False
        self._y_dc_freezing = False
        pass
        _y_dc_value_0 = name
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0
        if children is _y_dc_factory_sentinel:
            try:
                _y_dc_value_1 = _y_dc_factory_1()
            except _y_dc_ContextErrors:
                raise
            except _y_dc_Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('render_case.<locals>.Scope.children: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_1 = children
        pass
        pass
        self._y_dc_store_1 = _y_dc_value_1

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        _y_cmp_result = self.name == other.name
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.children == other.children
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('name' + '=' + repr(self.name), 'children' + '=' + repr(self.children))) + ')'

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
            _y_dc_state_values[1] = self._y_dc_store_1
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_frozen
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self._y_dc_freezing
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
            self._y_dc_store_1 = _y_dc_state_values[1]
        else:
            try:
                del self._y_dc_store_1
            except AttributeError:
                pass
        if 2 in _y_dc_state_values:
            self._y_dc_frozen = _y_dc_state_values[2]
        else:
            try:
                del self._y_dc_frozen
            except AttributeError:
                pass
        if 3 in _y_dc_state_values:
            self._y_dc_freezing = _y_dc_state_values[3]
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

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
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
    name = _y_dc_property(_y_dc_get_0, _y_dc_set_0, _y_dc_del_0)

    def freeze(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False) or _y_dc_getattr(self, '_y_dc_freezing', False):
            return
        self._y_dc_freezing = True
        try:
            pass
            self.name
            self._y_dc_store_1 = _y_dc_freeze_1(self.children)
            self._y_dc_frozen = True
        finally:
            self._y_dc_freezing = False

    def _y_dc_get_1(self):
        return self._y_dc_store_1

    def _y_dc_set_1(self, value):
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)
        pass
        pass
        self._y_dc_store_1 = value

    def _y_dc_del_1(self):
        if _y_dc_getattr(self, '_y_dc_frozen', False):
            raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_1)
        del self._y_dc_store_1
    children = _y_dc_property(_y_dc_get_1, _y_dc_set_1, _y_dc_del_1)
