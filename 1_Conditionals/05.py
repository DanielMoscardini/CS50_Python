# And condition

x = int(input('Whats x? '))
y = int(input('Whats y? '))

if x > y and x % 2 == 0:
    print('x is even and greater than y')
elif x > y and x % 2 != 0:
    print('x is odd and greater than y')
else:
    print('y is greater than x')
