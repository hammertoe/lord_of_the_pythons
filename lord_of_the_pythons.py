import re
import os
from pathlib import Path
import ast


def find_all_variable_names(filename):
    root = ast.parse(open(filename).read(), 
                     filename=filename)
    names = {node.id for node in ast.walk(root) if isinstance(node, ast.Name)}
    return names

def find_all_variable_names_in_dir(path):
    all_names = set()
    filenames = Path(path).glob('**/*.py')
    for filename in filenames:
        all_names |= find_all_variable_names(str(filename))

    all_names = set([x.lower() for x in all_names])
    return all_names

if __name__ == '__main__':
    lotr_names = [ x.lower().strip() for x in open('lotr.txt').readlines()]
    lotr_names = set([ x for x in lotr_names if x])
    print('lotr', lotr_names)

    old_varnames = find_all_variable_names_in_dir('.old-code')
    new_varnames = find_all_variable_names_in_dir('.new-code')
    print('old', old_varnames)
    print('new', new_varnames)

    new_lotr = (new_varnames - old_varnames) & lotr_names
    num = len(new_lotr)
    
    print('new lotr', new_lotr)

    return {'new_lotr', new_lotr,
            'num', num,
            'amount', int(1e6 * num)
            }
