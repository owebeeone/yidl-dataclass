class Catalog(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('count', 'label', 'retired', 'tags', 'limit')

    def __init__(self, count: _y_dc_annotation_0, label: _y_dc_annotation_1=_y_dc_default_1, tags: _y_dc_annotation_3=_y_dc_factory_sentinel, *, limit: _y_dc_annotation_5=_y_dc_default_5) -> None:
        pass
        self.count = count
        self.label = label
        self.retired = _y_dc_default_2
        if tags is _y_dc_factory_sentinel:
            tags = _y_dc_factory_3()
        self.tags = tags
        self.limit = limit
