"""Broad post-GREEN capture-domain audit, not duplicate public canonical protocols."""
import builtins
import copy
from yidl_dataclass import dataclass, field, const

names=('locals','object','len','isinstance','ValueError','RuntimeError','__name__','__builtins__','__base__','_y_dc_restore','_y_dc_deepcopy','_y_dc_replace','_y_dc_namespace','_y_dc_metaclass','_y_dc_error','_y_dc_validator_0','_y_dc_factory_0','_y_dc_arg_default_0_0','_y_dc_default_0','_y_dc_annotation_0')
for name in names:
    declaration=builtins.type(name,(),{'__module__':__name__,'__annotations__':{'value':int},'value':const(default=3)})
    model=dataclass(declaration)
    value=model()
    assert copy.copy(value).value==3 and copy.deepcopy(value).value==3
    assert model.__name__==name and model.__module__==__name__
print('all20 additional builtin/metadata/helper result names preserve copy and public identity')
