# Pythonic expression:
# Parity function
def main():
    number = int(input('Pick a number: '))
    print(parity_check(number))


def parity_check(n):
    return f'{n} is a even number!' if n % 2 == 0 else f'{n} is a odd number!'


main()
