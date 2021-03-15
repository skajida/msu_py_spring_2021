def main():
    n = int(input())
    array = list(map(int, input().split()))

    s = set()
    for number in array:
        if number not in s:
            print(number, end=' ')
        s.add(number)
    print('\n{}'.format(len(array) - len(s)))


if __name__ == "__main__":
    main()
