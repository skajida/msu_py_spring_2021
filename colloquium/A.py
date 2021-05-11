def find_substring(text, string):
    idx_left_best, idx_right_best = len(text), len(text)
    idx_left_curr, idx_right_curr = len(text), len(text)
    hamming_distance = len(string)
    alphabet = set(string)
    while idx_left_curr != 0:
        while not alphabet.issubset(text[idx_left_curr:idx_right_curr]) and idx_left_curr:
            idx_left_curr -= 1
        while alphabet.issubset(text[idx_left_curr:idx_right_curr]) and idx_left_curr < idx_right_curr:
            if idx_left_best == len(text) or idx_right_curr - idx_left_curr <= idx_right_best - idx_left_best:
                idx_left_best, idx_right_best = idx_left_curr, idx_right_curr
            idx_right_curr -= 1
    return idx_left_best, idx_right_best


def main():
    s1, s2 = input(), input()
    idx_left, idx_right = find_substring(s1, s2)
    print(s1[idx_left:idx_right])


if __name__ == '__main__':
    main()
