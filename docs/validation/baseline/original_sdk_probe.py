import os,sys,pathlib,ast,json,importlib.metadata
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[2]
import astichi,yidl
from yidl.concept_parser import compile_yidl_files
from yidl.generation.data_def_sys import emit_concept_runtime_source
from yidl.generation.matcher_values import from_astichi_code
for module in (astichi,yidl):
 assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
path='tests/data/yidl/dataclasses_example.yidl'
source=pathlib.Path(sys.argv[1]).read_text()
concept=compile_yidl_files({path:source},path).concepts['DataclassSubstitute']
rs=emit_concept_runtime_source(concept.plan.build_data_definition(),resources=concept.resources,assembly_plan=concept)
ns={};exec(compile(rs,'<baseline-yidl-runtime>','exec'),ns)
b=ns['new_builder']()
b.add(ns['FacadesCollection'],ns['DataclassFacade'](class_id='Widget',class_name='Widget',module_name='baseline',decorator_slots=True,slot_names=('count','label'),decorator_frozen=True,match_args=('count','label')))
for index,(name,annotation) in enumerate((('count','int'),('label','str'))):
 b.add(ns['FieldsCollection'],ns['DataclassField'](field_id='Widget.'+name,field_owner='Widget',field_name=name,field_order=index,annotation=annotation))
tree=ns['build_DataclassModule'](b.freeze()).to_executable_ast()
out={};exec(compile(tree,'<baseline-generated-class>','exec'),out)
cls=out['Widget'];a=cls(3,'x');same=cls(3,'x');other=cls(4,'x')
assert a==same and a!=other
assert hash(a)==hash((3,'x'))
assert not hasattr(a,'__dict__')
# Existing identifier specialization already emits a literal field access.
piece=astichi.compile('def read(self):\n    return self.astichi_ref(external=field_name)',keep_names=('self','read','count')).bind(field_name='count')
specialized=piece.to_executable_ast()
function=specialized.body[0]
assert isinstance(function.body[0].value,ast.Attribute)
assert function.body[0].value.attr=='count'
assert not any(isinstance(n,ast.Call) for n in ast.walk(function))
resource=from_astichi_code('value = 1')
assert resource.to_generator() is resource.to_generator()
print(json.dumps({'astichi':importlib.metadata.version('astichi'),'yidl':importlib.metadata.version('yidl'),'selected_backend':sys.argv[2],'existing_yidl_dataclass_slots_eq_hash':'pass','field_specific_attribute_specialization':'pass','existing_resource_compilation_cache':'pass','scope':'feasibility only; not full requested product'},sort_keys=True))
