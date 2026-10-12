"""Fresh-process timing-boundary feasibility; not final performance evidence."""
import argparse
import dataclasses as std
import hashlib
import json
import os
import time

parser=argparse.ArgumentParser()
parser.add_argument('--variant',choices=['product','stdlib_default','stdlib_slots'],required=True)
parser.add_argument('--fields',choices=[3,12],type=int,required=True)
args=parser.parse_args()
os.environ['ASTICHI_LOWER_ENGINE']='native-rust'
if args.variant=='product':
    import yidl_dataclass as api
else:
    api=std
namespace={'__module__':__name__,'__annotations__':{f'f{i}':int for i in range(args.fields)}}
namespace.update({f'f{i}':i for i in range(args.fields)})
declaration=type('Fields',(),namespace)
start=time.perf_counter_ns()
model=api.dataclass(slots=args.variant!='stdlib_default',order=True)(declaration)
elapsed=time.perf_counter_ns()-start
assert model().f0==0
print(json.dumps({'classification':'cold boundary feasibility only; not final benchmark',
                  'variant':args.variant,'fields':args.fields,'operations':1,
                  'elapsed_ns':elapsed,'minimum_batch_ns':20_000_000,
                  'reaches_planned_batch_minimum':elapsed>=20_000_000,
                  'imports_and_declaration_setup':'outside measured interval',
                  'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest()}))
