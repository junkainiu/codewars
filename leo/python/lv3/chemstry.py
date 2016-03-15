import re
from collections import defaultdict

atom_pattern = re.compile(r'[A-Z]')
sub_atom_pattern = re.compile(r'[a-z]')
num_pattern = re.compile(r'\d')
br_start_pattern = re.compile(r'\[|\{|\(')
br_end_pattern = re.compile(r'\]|\}|\)')

def get_num(formula, i):
    r = re.match(r'\d+', formula[i:])
    len = r.span()[1] - r.span()[0]
    result = int(r.group())
    return result,len

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
                        num,num_len = get_num(formula, i+2)
                        result[name].update({i+2 : num})
                        i = i+2+num_len
                    else:
                        result[name].update({i+1 : 1})
                        i += 2
                elif num_pattern.match(formula[i+1]):
                    num,num_len = get_num(formula, i+1)
                    result[name].update({i+1 : num})
                    i = i + 1 + num_len
                else:
                    result[name].update({i : 1})
                    i += 1
            elif br_start_pattern.match(formula[i]):
                i += 1
            elif br_end_pattern.match(formula[i]):
                if num_pattern.match(formula[i+1]):
                    num,num_len = get_num(formula, i+1)
                    result = add_br_end_num(result, i+1, num, br_position)
                    i += 1 + num_len
                else:
                    result = add_br_end_num(result, i+1, 1, br_position)
                    i += 1
            else:
                i += 1
        except IndexError:
            if num_pattern.match(formula[len(formula)-1]):
                if atom_pattern.match(formula[i]):
                    num,num_len = get_num(formula, i+1)
                    result[name].update({i+1, num})
                    i = i + 1 + num_len
                elif br_end_pattern.match(formula[i]):
                    num,num_len = get_num(formula, i+1)
                    result = add_br_end_num(result, i+1, num, br_position)
                    i += 1 + num_len
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
    print result
    return result

def add_br_end_num(result, i, v, br_position):
    for elem in br_position:
        if elem[1] == i:
            for value in result.itervalues():
                for key in value.keys():
                    if key > elem[0] and key < elem[1]:
                        value[key] = int(value[key]) * int(v)
    return result

def calculate_result(result):
    result = {key:sum([int(v) for v in value.itervalues()]) for key,value in result.iteritems()}
    return result
