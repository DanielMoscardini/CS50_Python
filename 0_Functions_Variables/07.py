# How to organize functions in your code?
def main():
    name = input('Whats your name? ')
    hello(name)


def hello(to="world"):
    print(f'Hello, {to}')


main()
