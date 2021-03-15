from itertools import groupby


def main():
    n = int(input())
    words = [input() for i in range(n)]
    groups = groupby(sorted(words, key=sorted), sorted)
    for words in [list(group) for key, group in groups]:
        print(*words)


if __name__ == "__main__":
    main()
