class Inventory(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("count", "label", "reserve")

    def __init__(
        self,
        count: _y_dc_annotation_0,
        label: _y_dc_annotation_1 = _y_dc_default_1,
        reserve: _y_dc_annotation_2 = _y_dc_default_2,
    ) -> None:
        pass
        self.count = count
        self.label = label
        self.reserve = reserve

    pass
    pass
    pass
    pass
    pass
    pass
    pass


class Declaration(*_y_dc_bases, metaclass=_y_dc_metaclass):
    locals().update(_y_dc_namespace)
    __slots__ = ("units",)

    def __init__(
        self, inherited: _y_dc_annotation_0, units: _y_dc_annotation_1 = _y_dc_default_1
    ) -> None:
        pass
        self.inherited = inherited
        self.units = units

    pass
    pass
    pass
    pass
    pass
    pass
    pass
