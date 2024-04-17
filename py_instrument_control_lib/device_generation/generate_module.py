import json
import os
import sys
from os.path import abspath

DISCLAIMER = '''"""
This code is automatically generated from \'{}\'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""'''


def load_spec(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)


def indent(code: str, level: int = 1) -> str:
    spaces = level * '    '
    return spaces + code.replace('\n', '\n' + spaces)


def generate_base_module(spec: dict) -> str:
    return generate_imports(spec) + '\n\n\n' + f"class {spec['name']}({spec['devicetype']}, {spec['superclass']}):"


def get_default_imports() -> str:
    import_path = abspath('')
    if not import_path.endswith('device_generation'):
        import_path = os.path.join(import_path, 'device_generation')
    import_path = os.path.join(import_path, 'DEFAULT_IMPORTS.py')
    with open(import_path, 'r') as f:
        return f.read()


def generate_imports(spec: dict) -> str:
    return get_default_imports() + ('\n' + spec['imports'] if 'imports' in spec else '')


def generate_signature(method: dict) -> str:
    if method['signature'] != '':
        method['signature'] += ', '
    return f"self, {method['signature']}check_errors: bool = False"


def generate_method(method: dict) -> str:
    code = ''
    if 'return' not in method:
        method['return'] = 'None'

    if method['type'] == 'generated':

        check_error_buffer = f'if check_errors:' \
                             f'\n    self.check_error_buffer()'
        if method['return'] == 'None':
            code = f'self.execute({method["command"]})' \
                   f'\n{check_error_buffer}'
        else:
            if method['return'] == 'float':
                conversion = 'float(val)'
            elif method['return'] == 'int':
                conversion = 'int(val)'
            else:
                conversion = 'val'
            code = f'val = self.query({method["command"]})' \
                   f'\n{check_error_buffer}' \
                   f'\nreturn {conversion}'

    elif method['type'] == 'code':
        code = method['code']

    return generate_method_head(method) + f'\n{indent(code)}'


def generate_docs(method: dict) -> str:
    docs = ''
    if 'docs' in method:
        docs = f'\n"""\n{method["docs"]}\n"""'
    return docs


def generate_method_head(method: dict) -> str:
    return f'def {method["name"]}({generate_signature(method)}) \\' \
           f'\n        -> {method["return"]}:{indent(generate_docs(method))}{indent(generate_requirements(method))}'


def generate_requirements(method: dict) -> str:
    if 'requirements' in method:
        return f'\nif not ({method["requirements"]}):' \
               f'\n    raise ValueError(\'Requirements not satisfied\')\n'
    else:
        return ''


def generate_code(spec: dict) -> str:
    methods = list(map(generate_method, spec['commands']))
    return generate_base_module(spec) + '\n\n' + indent('\n\n'.join(methods), 1) + '\n'


def generate_module(filepath: str, target_dir: str = '.') -> None:
    spec = load_spec(abspath(filepath))
    module = DISCLAIMER.format(filepath) + '\n\n' + generate_code(spec)
    file_name = os.path.join(target_dir, spec['name'] + '.py')
    with open(file_name, 'w') as f:
        f.write(module)
    os.system(f'python3 -m autopep8 -i --max-line-length 120 {abspath(file_name)}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You need to set the path to the specification of the device!')
    else:
        generate_module(sys.argv[1])
