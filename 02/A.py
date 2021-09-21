def solution1(Input):
    return [4 * c for c in Input]


def solution2(Input):
    return [(i + 1) * c for i, c in enumerate(Input)]


def solution3(Input):
    return [i for i in Input if not i % 3 or not i % 5]


def solution4(Input):
    return [j for i in Input for j in i]


def solution5(Input):
    squares = [i ** 2 for i in range(1, Input + 1)]
    pairs = [(x, y) for x in range(1, Input) for y in range(x + 1, Input) if x ** 2 + y ** 2 in squares]
    return [(x, y, int((x ** 2 + y ** 2) ** 0.5)) for x, y in pairs]


def solution6(Input):
    return [[i + j for i in Input[1]] for j in Input[0]]


def solution7(Input):
    return [[i[j] for i in Input] for j in range(len(Input[0]))]


def solution8(Input):
    return [list(map(int, i.split())) for i in Input]


def solution9(Input):
    symbols = range(ord('a'), ord('z') + 1)
    return {chr(symbols[i % (ord('z') + 1 - ord('a'))]): i ** 2 for i in Input}


def solution10(Input):
    return {i.lower().capitalize() for i in Input if len(i) > 3}


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
