import inspect
import json

import pandas

def get_source(func):
    return inspect.getsource(func)

def prepare_esc(func, func_args):
    esc = get_source(func)
    dataframe = None
    imports = set()
    
    esc_lines = []
    for line in esc.split('\n'):
        if '@' in line: continue
        esc_lines.append(line+'\n')
    
    esc = "".join(esc_lines)
    
    for key, item in func_args.copy().items():
        if type(item) not in (int, float, str, bool, dict, list, set, tuple, pandas.DataFrame): \
           return f"Wrong variable type {type(item)} in function arguments"
        
        if type(item) == pandas.DataFrame:
            dataframe = key
            func_args[key] = item.to_dict()

    if dataframe: imports.add('pandas.Dataframe')
    esc += f"args = {json.dumps(func_args)} \n\n"
    esc += f"if {dataframe}: args[{dataframe}] = pandas_Dataframe.from_dict(args[{dataframe}])\n\n\n"
    esc += f"def execute():\n   return {func.__name__}(**args)"

    return esc, imports
