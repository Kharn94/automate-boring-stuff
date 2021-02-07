import sys


def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print("Enter number:")
try:
    n = input()
    n = int(n)
    collatz_n = n
    while collatz_n != 1:
        collatz_n = collatz(collatz_n)
    else:
        sys.exit
except ValueError:
    print('You must enter an integer.')




