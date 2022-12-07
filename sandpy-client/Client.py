import base64
import os
from pathlib import Path
import pickle
import requests

from time import sleep


class Client():
    def __init__(self, api_key, api_secret, requirements=None, requirements_filename=None, imports='', compute_on='CPU'):
        self.api_key = str(api_key)
        self.api_secret = str(api_secret)
        self.requirements = str(requirements)
        if requirements_filename:
            self.requirements = Path(requirements).read_text()
        
        elif requirements and type(requirements) in (list, set, tuple): self.requirements = '\n'.join(requirements)
        else:
            raise Exception('Please provide correct arguments')
    
        self.imports = set(imports)
        self.compute_on = str(compute_on).upper()

    def run(self, imports=None, compute_on=None):
        if imports is None: imports = self.imports
        else: imports = set(imports)
        
        if compute_on is None: compute_on = self.compute_on
        
        if type(self.api_key) != str or \
        type(self.api_secret) != str or \
        type(self.imports) not in (set, tuple, list) or \
        self.compute_on not in ('CPU', 'GPU'):
            raise Exception('Please provide correct arguments')
        
        def decorator(func):
            def wrapper(**args):
                esc, _imports = prepare_esc(func, args)
                json = {
                    'api_key' : self.api_key,
                    'api_secret' : self.api_secret,        
                    'esc' : esc,
                    'imports' : tuple(imports | _imports),
                    'requirements' : self.requirements,
                    'compute_on' : compute_on,
                }
    
                res = requests.post('http://127.0.0.1:8000/run_calculations', json=json)
                if res.status_code == 200:
                    json = {
                        'api_key' : self.api_key,
                        'api_secret' : self.api_secret,
                        'iid' : res.json()['iid'],
                    }
                    while True:
                        res = requests.post('http://127.0.0.1:8000/get_result', json=json)
                        if res.status_code == 200:
                            body = res.json()
                            exec_code = int(body['status_code'])
                            if exec_code == -1:
                                raise Exception(body['msg'])
                            
                            elif exec_code == 0:
                                sleep(30)
                                
                            elif exec_code == 1:
                                pickle_code = base64.b64decode(body['msg'])
                                output = pickle.loads(pickle_code)
        
                                return output
                            
            return wrapper
                                   
        return decorator


class Project(Client):
    def __init__(self, main_func, project_directory='.'):
        super()
        self.main_func = main_func
        self.project_directory = project_directory

    def get_project_files():
        fd = {}
        for _, _, files in os.walk(self.project_directory):
            for filename in files:
                fd = {'filename' : str(Path.read_text(filename))+'\n'}
