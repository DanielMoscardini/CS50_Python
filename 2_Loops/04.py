while True:
    n = int(input('How many times do you want the cat to meow? '))
    
    for _ in range(n):
        print('Meow')

    if n > 0:
        break
