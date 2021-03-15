def main():
    change = float(input())
    denominations = [10., 5., 2., 1., 0.5, 0.1, 0.05, 0.01]
    for denomination in denominations:
        div = int(change // denomination)
        if (div):
            print('{:5.2f}\t{}'.format(denomination, div))
            change -= div * denomination


if __name__ == "__main__":
    main()
