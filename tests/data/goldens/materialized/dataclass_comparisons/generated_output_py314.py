class Quote(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('sku', 'price', 'currency', 'tags', 'note', 'cache', 'audit')

    def __init__(self, sku: _y_dc_annotation_0, price: _y_dc_annotation_1, currency: _y_dc_annotation_2=_y_dc_default_2, tags: _y_dc_annotation_3=_y_dc_default_3, note: _y_dc_annotation_4=_y_dc_default_4, cache: _y_dc_annotation_5=_y_dc_factory_sentinel, audit: _y_dc_annotation_6=_y_dc_default_6) -> None:
        pass
        self.sku = sku
        self.price = price
        self.currency = currency
        self.tags = tags
        self.note = note
        if cache is _y_dc_factory_sentinel:
            cache = _y_dc_factory_5()
        self.cache = cache
        self.audit = audit

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        _y_cmp_result = self.sku == other.sku
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        _y_cmp_result = self.price == other.price
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        _y_cmp_result = self.currency == other.currency
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.tags == other.tags

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) < (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) <= (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) > (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) >= (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __hash__(self):
        return hash((self.sku if True else None, self.price if True else None, self.currency if True else None))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('sku' + '=' + repr(self.sku), 'price' + '=' + repr(self.price), 'currency' + '=' + repr(self.currency), 'tags' + '=' + repr(self.tags), 'note' + '=' + repr(self.note))) + ')'

class Removed(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('sku', 'price', 'currency', 'tags', 'note')

    def __init__(self, sku: _y_dc_annotation_0, price: _y_dc_annotation_1, currency: _y_dc_annotation_2=_y_dc_default_2, tags: _y_dc_annotation_3=_y_dc_default_3, note: _y_dc_annotation_4=_y_dc_default_4) -> None:
        pass
        self.sku = sku
        self.price = price
        self.currency = currency
        self.tags = tags
        self.note = note

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        _y_cmp_result = self.sku == other.sku
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        _y_cmp_result = self.price == other.price
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        _y_cmp_result = self.currency == other.currency
        try:
            if not _y_cmp_result:
                return _y_cmp_result
        finally:
            del _y_cmp_result
        return self.tags == other.tags

    def __lt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) < (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __le__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) <= (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __gt__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) > (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __ge__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.sku if True else None, self.price if True else None, self.currency if True else None, self.tags if True else None) >= (other.sku if True else None, other.price if True else None, other.currency if True else None, other.tags if True else None)

    def __hash__(self):
        return hash((self.sku if True else None, self.price if True else None, self.currency if True else None))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('sku' + '=' + repr(self.sku), 'price' + '=' + repr(self.price), 'currency' + '=' + repr(self.currency), 'tags' + '=' + repr(self.tags), 'note' + '=' + repr(self.note))) + ')'

class Excluded(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('visible', 'hidden')

    def __init__(self, visible: _y_dc_annotation_0=_y_dc_default_0, hidden: _y_dc_annotation_1=_y_dc_default_1) -> None:
        pass
        self.visible = visible
        self.hidden = hidden

    def __eq__(self, other):
        pass
        if self is other:
            return True
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
        return self.__class__.__qualname__ + '(' + ', '.join(('visible' + '=' + repr(self.visible),)) + ')'

class Unhashable(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('value',)

    def __init__(self, value: _y_dc_annotation_0) -> None:
        pass
        self.value = value

    def __eq__(self, other):
        pass
        if self is other:
            return True
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.value == other.value
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('value' + '=' + repr(self.value),)) + ')'
