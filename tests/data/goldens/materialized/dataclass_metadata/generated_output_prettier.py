class Catalog(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ("count", "label", "retired", "tags", "limit")

    def __init__(
        self,
        count: _y_dc_annotation_0,
        label: _y_dc_annotation_1 = _y_dc_default_1,
        tags: _y_dc_annotation_3 = _y_dc_factory_sentinel,
        *,
        limit: _y_dc_annotation_5 = _y_dc_default_5
    ) -> None:
        pass
        _y_dc_value_0 = count
        pass
        pass
        self.count = _y_dc_value_0
        _y_dc_value_1 = label
        pass
        pass
        self.label = _y_dc_value_1
        _y_dc_value_2 = _y_dc_default_2
        pass
        pass
        self.retired = _y_dc_value_2
        if tags is _y_dc_factory_sentinel:
            try:
                _y_dc_value_3 = _y_dc_factory_3()
            except _y_dc_ContextErrors:
                raise
            except Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError(
                    "declarations.<locals>.Catalog.tags: factory failed"
                ) from _y_dc_factory_error
        else:
            _y_dc_value_3 = tags
        pass
        pass
        self.tags = _y_dc_value_3
        _y_dc_value_5 = limit
        pass
        pass
        self.limit = _y_dc_value_5

    pass
    pass
    pass
    pass
    pass
    pass
    pass
