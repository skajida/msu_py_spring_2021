from itertools import accumulate


def main():
    n = int(input())
    array = input().split()
    array.sort(key=lambda s: (list(accumulate(map(int, s)))[-1], int(s)))
    print(*array)


if __name__ == "__main__":
    main()
