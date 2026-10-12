class Before(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('code', 'measure', '_y_dc_store_2', 'label', 'doubled', 'management')

    def __init__(self, code: _y_dc_annotation_0, measure: _y_dc_annotation_1=_y_dc_default_1, obsolete: _y_dc_annotation_2=_y_dc_default_2, label: _y_dc_annotation_3=_y_dc_default_3) -> None:
        pass
        _y_dc_value_0 = code
        pass
        pass
        self.code = _y_dc_value_0
        _y_dc_value_1 = measure
        pass
        pass
        self.measure = _y_dc_value_1
        _y_dc_value_2 = obsolete
        try:
            _y_dc_value_2 = _y_dc_converter_2(_y_dc_value_2)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(_y_dc_conversion_message_2) from _y_dc_conversion_error
        pass
        self._y_dc_store_2 = _y_dc_value_2
        _y_dc_value_3 = label
        pass
        pass
        self.label = _y_dc_value_3
        try:
            _y_dc_value_4 = _y_dc_factory_4(measure=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Before.doubled: factory failed') from _y_dc_factory_error
        pass
        pass
        self.doubled = _y_dc_value_4
        try:
            _y_dc_value_5 = _y_dc_factory_5()
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Before.management: factory failed') from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_5

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None) == (other.code if True else None, other.measure if True else None, other.obsolete if True else None, other.doubled if True else None)

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None) < (other.code if True else None, other.measure if True else None, other.obsolete if True else None, other.doubled if True else None)

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None) <= (other.code if True else None, other.measure if True else None, other.obsolete if True else None, other.doubled if True else None)

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None) > (other.code if True else None, other.measure if True else None, other.obsolete if True else None, other.doubled if True else None)

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None) >= (other.code if True else None, other.measure if True else None, other.obsolete if True else None, other.doubled if True else None)

    def __hash__(self):
        return hash((self.code if True else None, self.measure if True else None, self.obsolete if True else None, self.doubled if True else None))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('code' + '=' + repr(self.code), 'measure' + '=' + repr(self.measure), 'obsolete' + '=' + repr(self.obsolete), 'label' + '=' + repr(self.label), 'doubled' + '=' + repr(self.doubled))) + ')'

    def __getstate__(self):
        _y_dc_state_values = {}
        pass
        pass
        try:
            _y_dc_state_values[0] = self.code
        except AttributeError:
            pass
        try:
            _y_dc_state_values[1] = self.measure
        except AttributeError:
            pass
        try:
            _y_dc_state_values[2] = self._y_dc_store_2
        except AttributeError:
            pass
        try:
            _y_dc_state_values[3] = self.label
        except AttributeError:
            pass
        try:
            _y_dc_state_values[4] = self.doubled
        except AttributeError:
            pass
        try:
            _y_dc_state_values[5] = self.management
        except AttributeError:
            pass
        return (1, _y_dc_state_values, None)

    def __setstate__(self, state):
        if type(state) is not tuple or len(state) != 3 or type(state[0]) is not int or (state[0] != 1) or (type(state[1]) is not dict) or (state[2] is not None):
            raise ValueError('unsupported dataclass state schema')
        _y_dc_state_values = state[1]
        pass
        if 0 in _y_dc_state_values:
            self.code = _y_dc_state_values[0]
        else:
            try:
                del self.code
            except AttributeError:
                pass
        if 1 in _y_dc_state_values:
            self.measure = _y_dc_state_values[1]
        else:
            try:
                del self.measure
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
            self.label = _y_dc_state_values[3]
        else:
            try:
                del self.label
            except AttributeError:
                pass
        if 4 in _y_dc_state_values:
            self.doubled = _y_dc_state_values[4]
        else:
            try:
                del self.doubled
            except AttributeError:
                pass
        if 5 in _y_dc_state_values:
            self.management = _y_dc_state_values[5]
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

    def _y_dc_get_2(self):
        return self._y_dc_store_2

    def _y_dc_set_2(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    def _y_dc_del_2(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)
    obsolete = _y_dc_property(_y_dc_get_2, _y_dc_set_2, _y_dc_del_2)

class After(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('code', 'measure', 'label', 'doubled', 'management')

    def __init__(self, code: _y_dc_annotation_0, measure: _y_dc_annotation_1=_y_dc_default_1, label: _y_dc_annotation_2=_y_dc_default_2) -> None:
        pass
        _y_dc_value_0 = code
        pass
        pass
        self.code = _y_dc_value_0
        _y_dc_value_1 = measure
        pass
        pass
        self.measure = _y_dc_value_1
        _y_dc_value_2 = label
        pass
        pass
        self.label = _y_dc_value_2
        try:
            _y_dc_value_3 = _y_dc_factory_3(measure=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.After.doubled: factory failed') from _y_dc_factory_error
        pass
        pass
        self.doubled = _y_dc_value_3
        try:
            _y_dc_value_4 = _y_dc_factory_4()
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.After.management: factory failed') from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_4

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.doubled if True else None) == (other.code if True else None, other.measure if True else None, other.doubled if True else None)

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.doubled if True else None) < (other.code if True else None, other.measure if True else None, other.doubled if True else None)

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.doubled if True else None) <= (other.code if True else None, other.measure if True else None, other.doubled if True else None)

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.doubled if True else None) > (other.code if True else None, other.measure if True else None, other.doubled if True else None)

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.code if True else None, self.measure if True else None, self.doubled if True else None) >= (other.code if True else None, other.measure if True else None, other.doubled if True else None)

    def __hash__(self):
        return hash((self.code if True else None, self.measure if True else None, self.doubled if True else None))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('code' + '=' + repr(self.code), 'measure' + '=' + repr(self.measure), 'label' + '=' + repr(self.label), 'doubled' + '=' + repr(self.doubled))) + ')'
