class Processed(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('total', '_y_dc_store_1', '_y_dc_store_2', 'management')

    def __init__(self, units: _y_dc_annotation_1=_y_dc_default_1, token: _y_dc_annotation_2=_y_dc_default_2) -> None:
        pass
        _y_dc_value_1 = units
        try:
            _y_dc_value_1 = _y_dc_converter_1(_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(_y_dc_conversion_message_1) from _y_dc_conversion_error
        try:
            _y_dc_validation_result = _y_dc_validator_1(_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_validation_error:
            raise _y_dc_FieldValidationError(_y_dc_validation_message_1) from _y_dc_validation_error
        try:
            if _y_dc_validation_result is False:
                raise _y_dc_FieldValidationError(_y_dc_validation_rejected_1)
            if _y_dc_validation_result is not None and _y_dc_validation_result is not True:
                raise TypeError(_y_dc_validation_contract_1)
        finally:
            del _y_dc_validation_result
        self._y_dc_store_1 = _y_dc_value_1
        try:
            _y_dc_value_0 = _y_dc_factory_0(units=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Processed.total: factory failed') from _y_dc_factory_error
        pass
        pass
        self.total = _y_dc_value_0
        _y_dc_value_2 = token
        pass
        pass
        self._y_dc_store_2 = _y_dc_value_2
        try:
            _y_dc_value_3 = _y_dc_factory_3(units=_y_dc_value_1)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Processed.management: factory failed') from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_3

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.total if True else None, self.units if True else None, self.token if True else None) == (other.total if True else None, other.units if True else None, other.token if True else None)
    pass
    pass
    pass
    pass
    __hash__ = None

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('total' + '=' + repr(self.total), 'units' + '=' + repr(self.units), 'token' + '=' + repr(self.token))) + ')'

    @property
    def units(self):
        return self._y_dc_store_1

    @units.setter
    def units(self, value):
        try:
            value = _y_dc_converter_1(value)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_conversion_error:
            raise _y_dc_FieldConversionError(_y_dc_conversion_message_1) from _y_dc_conversion_error
        try:
            _y_dc_validation_result = _y_dc_validator_1(value)
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_validation_error:
            raise _y_dc_FieldValidationError(_y_dc_validation_message_1) from _y_dc_validation_error
        try:
            if _y_dc_validation_result is False:
                raise _y_dc_FieldValidationError(_y_dc_validation_rejected_1)
            if _y_dc_validation_result is not None and _y_dc_validation_result is not True:
                raise TypeError(_y_dc_validation_contract_1)
        finally:
            del _y_dc_validation_result
        self._y_dc_store_1 = value

    @units.deleter
    def units(self):
        del self._y_dc_store_1

    @property
    def token(self):
        return self._y_dc_store_2

    @token.setter
    def token(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

    @token.deleter
    def token(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_2)

class Frozen(*_y_dc_bases):
    locals().update(_y_dc_namespace)
    __slots__ = ('_y_dc_store_0', 'cache', 'management')

    def __init__(self, amount: _y_dc_annotation_0, cache: _y_dc_annotation_1=_y_dc_factory_sentinel) -> None:
        pass
        _y_dc_value_0 = amount
        pass
        pass
        self._y_dc_store_0 = _y_dc_value_0
        if cache is _y_dc_factory_sentinel:
            try:
                _y_dc_value_1 = _y_dc_factory_1()
            except _y_dc_ContextErrors:
                raise
            except Exception as _y_dc_factory_error:
                raise _y_dc_FieldInitializationError('render_case.<locals>.Frozen.cache: factory failed') from _y_dc_factory_error
        else:
            _y_dc_value_1 = cache
        pass
        pass
        self.cache = _y_dc_value_1
        try:
            _y_dc_value_2 = _y_dc_factory_2()
        except _y_dc_ContextErrors:
            raise
        except Exception as _y_dc_factory_error:
            raise _y_dc_FieldInitializationError('render_case.<locals>.Frozen.management: factory failed') from _y_dc_factory_error
        pass
        pass
        self.management = _y_dc_value_2

    def __eq__(self, other):
        pass
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.amount if True else None,) == (other.amount if True else None,)
    pass
    pass
    pass
    pass

    def __hash__(self):
        return hash((self.amount if True else None,))

    @_y_dc_recursive_repr
    def __repr__(self):
        return self.__class__.__qualname__ + '(' + ', '.join(('amount' + '=' + repr(self.amount),)) + ')'

    @property
    def amount(self):
        return self._y_dc_store_0

    @amount.setter
    def amount(self, value):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)

    @amount.deleter
    def amount(self):
        raise _y_dc_FrozenInstanceError(_y_dc_frozen_message_0)
