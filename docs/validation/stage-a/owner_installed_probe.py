import os,sys,pathlib,json,inspect,weakref,importlib.metadata,dataclasses as std
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
import astichi,yidl,yidl_dataclass as product
for module in (astichi,yidl,product):
 assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
assert importlib.metadata.version('astichi')=='1.1.3'
assert importlib.metadata.version('yidl')=='0.1.0'
from astichi.lower_engine.native import load_native_extension, select_lower_engine
selection=select_lower_engine()
assert selection.selected_engine==sys.argv[1] and selection.fallback_scope is None
native=load_native_extension(required=True)
assert pathlib.Path(native.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
assert native.capabilities()['version']=='1.0.7'
assert 'native.compiled_template_artifact.v1' not in native.capabilities()['engine_features']

@product.dataclass(eq=False,repr=False,weakref_slot=True)
class Plain:
    count:int
    label:str='cold'
a=Plain(7)
assert not hasattr(a,'__dict__')
assert (a.count,a.label)==(7,'cold')
a.count=8
assert a.count==8 and weakref.ref(a)() is a
assert [f.name for f in std.fields(Plain)]==['count','label']
assert all(isinstance(f,std.Field) for f in std.fields(Plain))
assert std.asdict(a)=={'count':8,'label':'cold'}
assert std.replace(a,count=11).count==11 and a.count==8
assert inspect.signature(Plain).parameters['count'].annotation is int
assert Plain.__dataclass_params__.slots is True

class Opaque:
    def __repr__(self):
        raise AssertionError('default repr ran during generation')
first_default,second_default=Opaque(),Opaque()
first_field=product.field(default=first_default)
second_field=product.field(default=second_default)
First=product.dataclass(type('First',(),{'__module__':__name__,'__annotations__':{'payload':object},'payload':first_field}),eq=False,repr=False)
Second=product.dataclass(type('Second',(),{'__module__':__name__,'__annotations__':{'payload':object},'payload':second_field}),eq=False,repr=False)
assert First().payload is first_default
assert Second().payload is second_default
assert First().payload is first_default
assert First.__dataclass_fields__['payload'].default is first_default
assert inspect.signature(First).parameters['payload'].default is first_default
assert first_field.name is None and second_field.name is None

@product.dataclass(eq=False,repr=False,slots=False,init=False)
class Fallback:
    value:int=product.field(default=3,init=False)
b=Fallback()
assert b.__dict__=={} and b.value==3
Fallback.value=4
assert b.value==4
print(json.dumps({'python':sys.version.split()[0],'selected_backend':sys.argv[1],'sdk_versions':{'astichi':'1.1.3','yidl':'0.1.0','native':'1.0.7'},'product_version':importlib.metadata.version('yidl-dataclass'),'installed_origins':'pass','slot_constructor_metadata_helpers':'pass','opaque_default_capture_isolation':'pass','field_copy_ownership':'pass','dictionary_class_default_fallback':'pass','scope':'Stage A subset only; repr/comparison/policies/lazy/inheritance remain unverified'},sort_keys=True))
