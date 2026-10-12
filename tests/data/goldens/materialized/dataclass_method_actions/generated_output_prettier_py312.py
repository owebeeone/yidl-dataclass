class Inherited(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    pass
    pass
    pass
    pass
    pass
    pass
    pass


class Local(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    pass
    pass
    pass
    pass
    pass
    pass
    pass


class Automatic(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    pass
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )


class Unsafe(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    pass
    pass
    pass
    pass
    pass

    def __hash__(self):
        return hash((self.value if True else None,))

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )


class Recursive(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

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
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )


class Empty(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ()

    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return True

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return () < ()

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return () <= ()

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return () > ()

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return () >= ()

    def __hash__(self):
        return hash(())

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + "()"


class HashOnly(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("value",)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    pass
    pass
    pass
    pass
    pass

    def __hash__(self):
        return hash((self.value if True else None,))

    @_y_dc_recursive_repr
    def __repr__(self):
        return (
            self.__class__.__qualname__
            + "("
            + ", ".join(("value" + "=" + repr(self.value),))
            + ")"
        )
