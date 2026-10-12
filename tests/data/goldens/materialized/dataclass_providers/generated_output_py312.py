class Configuration(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('total', 'management', 'tag', 'box')

    def __init__(self, seed: _y_dc_annotation_1=_y_dc_default_1) -> None:
        pass
        _y_dc_value_1 = seed
        pass
        pass
        _y_dc_value_2 = type(self).scale
        try:
            _y_dc_value_0 = _y_dc_factory_0(seed=_y_dc_value_1, scale=_y_dc_value_2)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Configuration.total: factory failed') from _y_dc_factory_error
        pass
        pass
        self.total = _y_dc_value_0
        try:
            _y_dc_value_3 = _y_dc_factory_3(total=_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Configuration.management: factory failed') from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_3
        try:
            _y_dc_value_4 = _y_dc_factory_4(self=self, cls=type(self))
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Configuration.tag: factory failed') from _y_dc_factory_error
        pass
        pass
        self.tag = _y_dc_value_4
        try:
            _y_dc_value_5 = _y_dc_factory_5(total=_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Configuration.box: factory failed') from _y_dc_factory_error
        pass
        pass
        self.box = _y_dc_value_5

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.total if True else None, self.tag if True else None) == (other.total if True else None, other.tag if True else None)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('total' + '=' + repr(self.total), 'management' + '=' + repr(self.management), 'tag' + '=' + repr(self.tag))) + ')'

class StandardProvider(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('answer',)

    def __init__(self, seed: _y_dc_annotation_0=_y_dc_factory_sentinel) -> None:
        pass
        if seed is _y_dc_factory_sentinel:
            try:
                _y_dc_value_0 = _y_dc_factory_0()
            except _y_dc_ContextErrors:
                raise
            except Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('render_case.<locals>.StandardProvider.seed: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_0 = seed
        pass
        pass
        try:
            _y_dc_value_1 = _y_dc_factory_1(seed=_y_dc_value_0)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.StandardProvider.answer: factory failed') from _y_dc_factory_error
        pass
        pass
        self.answer = _y_dc_value_1

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.answer if True else None,) == (other.answer if True else None,)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('answer' + '=' + repr(self.answer),)) + ')'
