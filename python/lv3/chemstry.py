import re
from collections import defaultdict

atom_pattern = re.compile(r'[A-Z]')
sub_atom_pattern = re.compile(r'[a-z]')
num_pattern = re.compile(r'\d')
br_start_pattern = re.compile(r'\[|\{|\(')
br_end_pattern = re.compile(r'\]|\}|\)')

def calculate_br_pos(formula):
    result = []
    pair_pattern = re.compile(r'\[\w+\]|\{\w+\}|\(\w+\)')
    while pair_pattern.search(formula):
        br_pos = pair_pattern.search(formula).span()
        br_len = br_pos[1] - br_pos[0]
        result.append(br_pos)
        formula = pair_pattern.sub('a'*br_len, formula, 1)
    return result

def parse_molecule(formula):
    i = 0
    result = defaultdict(dict)
    br_position = calculate_br_pos(formula)
    while i<len(formula):
        try:
            if atom_pattern.match(formula[i]):
                name = formula[i]
                if sub_atom_pattern.match(formula[i+1]):
                    name = formula[i] + formula[i+1]
                    if num_pattern.match(formula[i+2]):
                        result[name].update({i+2 : formula[i+2]})
                        i += 3
                    else:
                        result[name].update({i+1 : 1})
                        i += 2
                elif num_pattern.match(formula[i+1]):
                    result[name].update({i+1 : formula[i+1]})
                    i += 2
                else:
                    result[name].update({i : 1})
                    i += 1
            elif br_start_pattern.match(formula[i]):
                i += 1
            elif br_end_pattern.match(formula[i]):
                if num_pattern.match(formula[i+1]):
                    result = add_br_end_num(result, i+1, formula[i+1], br_position)
                    i += 2
                else:
                    result = add_br_end_num(result, i+1, 1, br_position)
                    i += 1
            else:
                i += 1
        except IndexError:
            if num_pattern.match(formula[len(formula)-1]):
                if atom_pattern.match(formula[i]):
                    result[name].update({i+1, formula[i+1]})
                    i += 2
                elif br_end_pattern.match(formula[i]):
                    result = add_br_end_num(result, i+1, formula[i+1], br_position)
                    i += 2
                else:
                    i += 1
            elif br_end_pattern.match(formula[len(formula)-1]):
                if atom_pattern.match(formula[i]):
                    result[name].update({i : 1})
                    i += 1
                else:
                    i += 1
            elif sub_atom_pattern.match(formula[len(formula)-1]):
                result[name].update({i+1 : 1})
                i += 2
            elif atom_pattern.match(formula[len(formula)-1]):
                result[name].update({i : 1})
                i += 1
            continue
    result = calculate_result(result)
    return result

def add_br_end_num(result, i, v, br_position):
    import pdb; pdb.set_trace()
    for elem in br_position:
        if elem[1] == i:
            for value in result.itervalues():
                for key in value.keys():
                    if key > elem[0] and key < elem[1]:
                        value[key] = int(value[key]) * v

def calculate_result(result):
    result = {key:sum([int(v) for v in value.itervalues()]) for key,value in result.iteritems()}
    return result
