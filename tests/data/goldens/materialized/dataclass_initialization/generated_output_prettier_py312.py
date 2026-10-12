class Order(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("summary", "total", "units")

    def __init__(self, units: _y_dc_annotation_2) -> None:
        pass
        _y_dc_value_2 = units
        pass
        pass
        self.units = _y_dc_value_2
        _y_dc_value_3 = _y_dc_type(self).rate
        try:
            _y_dc_value_1 = _y_dc_factory_1(
                _y_dc_arg_default_1_0,
                _y_dc_value_2,
                rate=_y_dc_value_3,
                cls=_y_dc_type(self),
            )
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Order.total: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.total = _y_dc_value_1
        try:
            _y_dc_value_0 = _y_dc_factory_0(total=_y_dc_value_1, units=_y_dc_value_2)
        except _y_dc_ContextErrors:
            raise
        except _y_dc_Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError(
                "render_case.<locals>.Order.summary: factory failed"
            ) from _y_dc_factory_error
        pass
        pass
        self.summary = _y_dc_value_0

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.summary if True else None,
            self.total if True else None,
            self.units if True else None,
        ) == (
            other.summary if True else None,
            other.total if True else None,
            other.units if True else None,
        )

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
            + ", ".join(
                (
                    "summary" + "=" + repr(self.summary),
                    "total" + "=" + repr(self.total),
                    "units" + "=" + repr(self.units),
                )
            )
            + ")"
        )
