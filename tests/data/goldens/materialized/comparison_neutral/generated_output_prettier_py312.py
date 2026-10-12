class Neutral:
    __slots__ = ("payload",)

    def __init__(self, payload):
        self.payload = payload

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.payload.rank if True else None,
            self.payload.size if True else None,
        ) == (
            other.payload.rank if True else None,
            other.payload.size if True else None,
        )

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.payload.rank if True else None,
            self.payload.size if True else None,
        ) < (other.payload.rank if True else None, other.payload.size if True else None)

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.payload.rank if True else None,
            self.payload.size if True else None,
        ) <= (
            other.payload.rank if True else None,
            other.payload.size if True else None,
        )

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.payload.rank if True else None,
            self.payload.size if True else None,
        ) > (other.payload.rank if True else None, other.payload.size if True else None)

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.payload.rank if True else None,
            self.payload.size if True else None,
        ) >= (
            other.payload.rank if True else None,
            other.payload.size if True else None,
        )

    def __hash__(self):
        return hash(
            (self.payload.rank if True else None, self.payload.size if True else None)
        )
