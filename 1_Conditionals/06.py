# Parity function
def main():
    number = int(input('Pick a number: '))
    print(parity_check(number))


def parity_check(n):
    if n % 2 == 0:
        return f'{n} is a even number!'
    else:
        return f'{n} is a odd number!'


main()
