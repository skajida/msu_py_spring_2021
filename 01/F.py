from collections import Counter


def is_subcounter(counter_nested, counter_enclosing):
    counter_nested, counter_enclosing = map(dict, (counter_nested, counter_enclosing))
    for word, quantity in counter_nested.items():
        if not counter_enclosing.get(word) or quantity > counter_enclosing[word]:
            return False
    return True


def main():
    sentence1, sentence2 = input().lower().split(), input().lower().split()
    print('YES' if is_subcounter(Counter(sentence2), Counter(sentence1)) else 'NO')


if __name__ == "__main__":
    main()
