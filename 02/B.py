from re import sub
from functools import reduce
from operator import setitem
from collections import defaultdict


def solution1(Input):
    func = lambda item: sub(r'\D', '', item)[::-1]
    return list(map(int, map(func, Input)))


def solution2(Input):
    func = lambda item: reduce(lambda lhs, rhs: lhs * rhs, item)
    return list(map(func, Input))


def solution3(Input):
    return list(filter(lambda item: item % 6 in [0, 2, 5], Input))


def solution4(Input):
    return list(filter(bool, Input))


def solution5(Input):
    func = lambda item: setitem(item, 'square', item['width'] * item['length']) or item
    return list(map(func, Input))


def solution6(Input):
    func = lambda item: setitem(item, 'square', item['width'] * item['length']) or item
    return list(map(func, map(dict, Input)))


def solution7(Input):
    return reduce(set.intersection, Input)


def solution8(Input):
    func = lambda Dict, val: setitem(Dict, val, Dict[val] + 1) or Dict
    return dict(reduce(func, Input, defaultdict(int)))


def solution9(Input):
    filter_func = lambda item: item['gpa'] > 4.5
    get_name_func = lambda item: item['name']
    return list(map(get_name_func, filter(filter_func, Input)))


def solution10(Input):
    even_func = lambda item: sum(map(int, item[::2]))
    odd_func = lambda item: sum(map(int, item[1::2]))
    filter_func = lambda t: t[0] == t[1]
    get_str = lambda item: item[-1]
    return list(map(get_str, filter(filter_func, zip(map(even_func, Input), map(odd_func, Input), Input))))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
