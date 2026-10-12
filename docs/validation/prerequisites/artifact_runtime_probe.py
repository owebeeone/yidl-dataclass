import ast,builtins,json,os,sys
from pathlib import Path
os.environ["ASTICHI_LOWER_ENGINE"]="python"
import astichi
assert Path(astichi.__file__).resolve().is_relative_to(Path(sys.prefix).resolve())
assert astichi.__version__=="1.1.4.dev0"
from astichi.frontend import AUTHORED_SOURCE
source="astichi_bind_external(value)\nvalue"
tree=ast.parse(source)
payload=astichi.export_compiled_template(astichi.compile(source,file_name="owner/value.py"))
original=builtins.compile
attempts=[]
static_imports=[]
def protected(source,*args,**kwargs):
    if isinstance(source,(str,bytes,bytearray)):
        filename=args[0] if args else kwargs.get("filename")
        if isinstance(filename,str):
            path=Path(filename)
            if path.is_absolute() and path.is_file() and path.suffix==".py":
                actual=path.read_bytes()
                supplied=source.encode("utf-8") if isinstance(source,str) else bytes(source)
                if supplied==actual:
                    static_imports.append(path.name)
                    return original(source,*args,**kwargs)
        attempts.append(type(source).__name__)
        raise AssertionError("fresh source compile during artifact runtime")
    return original(source,*args,**kwargs)
builtins.compile=protected
try:
    a=astichi.load_compiled_template(payload)
    b=astichi.load_compiled_template(payload)
    c=astichi.compile_ast(tree,file_name="owner/structural.py",source_kind=AUTHORED_SOURCE)
    outputs=[p.bind(value=v).with_keep_names("owner_pinned").to_executable_ast() for p,v in [(a,[1,{"x":2}]),(b,3),(c,4)]]
finally:
    builtins.compile=original
assert not attempts
assert a.tree is not b.tree
assert a._lower_template.engine is not b._lower_template.engine
results=[]
for output in outputs:
    assert isinstance(output,ast.Module)
    # Evaluate its final expression independently without source parsing.
    body=output.body
    env={}
    if len(body)>1:
        exec(original(ast.fix_missing_locations(ast.Module(body=body[:-1],type_ignores=[])),"<owner-artifact>","exec"),env)
    results.append(eval(original(ast.fix_missing_locations(ast.Expression(body[-1].value)),"<owner-artifact>","eval"),env))
assert results==[[1,{"x":2}],3,4]
negative_results=[]
for name,node in [
    ("expression_in_statement_list",ast.Module(body=[ast.Name(id="x",ctx=ast.Load())],type_ignores=[])),
    ("statement_in_expression",ast.Module(body=[ast.Expr(value=ast.Pass())],type_ignores=[])),
    ("wrong_context",ast.Module(body=[ast.Expr(value=ast.Name(id="x",ctx=ast.Add()))],type_ignores=[])),
    ("invalid_identifier",ast.Module(body=[ast.Expr(value=ast.Name(id="not an identifier",ctx=ast.Load()))],type_ignores=[])),
]:
    ast.fix_missing_locations(node)
    try:
        astichi.compile_ast(node,file_name="owner/invalid.py")
    except astichi.CompiledTemplateError:
        negative_results.append(name)
    else:
        raise AssertionError("structural invalid input accepted: "+name)
print(json.dumps({"python":sys.version.split()[0],"backend":"python","protected_source_compile_calls":len(attempts),"normal_static_import_compilations":static_imports,"independent_values":results,"fresh_trees":True,"fresh_engines":True,"invalid_structural_inputs_rejected":negative_results},sort_keys=True))
