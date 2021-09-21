def brackets(n, str='', opened=0, closed=0):
    if opened + closed == 2 * n:
        yield str
    elif opened < n:
        yield from brackets(n, str + '(', opened + 1, closed)
    if closed < opened:
        yield from brackets(n, str + ')', opened, closed + 1)


def main():
    for i in brackets(int(input())):
        print(i)


if __name__ == '__main__':
    main()
