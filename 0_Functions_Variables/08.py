# Returning a value of a function
def main():
    x = int(input('Whats the value of x? '))
    print(f'x squared is: {square(x)}')


def square(n):
    return n * n


main()
