def main():
    left, right = 1, 100001
    div = 10
    while (right - left >= div):
        requests = range(left, right, (right - left) // div)
        for request in requests:
            print('?', request)
        print('+', flush=True)
        answer = [bool(int(input())) for i in range(div)]
        idx = answer.index(True) if True in answer else -1
        left, right = (requests[idx], right) if idx < 1 else (requests[idx - 1], requests[idx])
    print('! {}'.format(right - 1))


if __name__ == "__main__":
    main()
