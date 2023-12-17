#! python3.7
import argparse


def run(n: int, m: int):
    # "длина" ведь не может быть отрицательной, верно?
    if m == 0:
        print()
        return

    a1 = 1
    while True:
        print(a1, end='')
        a1 = (a1 + m - 2) % n + 1
        if a1 == 1:
            print()
            return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='task1')
    parser.add_argument('n', type=int, help='n - array length')
    parser.add_argument('m', type=int, help='m - span length')
    args = parser.parse_args()

    run(args.n, args.m)
