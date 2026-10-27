class Dictionary(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    pass

    def __init__(self) -> None:
        pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
    pass

class AssignedLater(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('value', 'pending')
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
    pass

class Custom(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('value',)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
    pass

class Unconsumed(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('value',)

    def __init__(self) -> None:
        pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
    pass

class Keywords(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ('first', 'later', 'optional', '__weakref__')

    def __init__(self, first: _y_dc_annotation_0, *, later: _y_dc_annotation_1, optional: _y_dc_annotation_2=_y_dc_default_2) -> None:
        pass
        self.first = first
        self.later = later
        self.optional = optional
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass

    def __replace__(self, **changes):
        return _y_dc_replace(self, **changes)
    pass
