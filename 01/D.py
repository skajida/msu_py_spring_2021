from itertools import accumulate


def main():
    n, k = input().split()
    all_numbers = [int(i * n) for i in range(1, int(k) + 1)]
    print(list(accumulate(all_numbers))[-1] if len(all_numbers) else 0)


if __name__ == "__main__":
    main()
