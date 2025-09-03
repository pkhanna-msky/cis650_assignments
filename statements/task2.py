while True:
    next_input = input('Enter an integer: ')
    try:
        n = int(next_input)
        break
    except ValueError:
        print('Error: please enter a whole number (e.g., -5, 0, 12). ')

if n == 0:
    multiples = [0]
else:
    step = abs(n)
    multiples = list(range(0, 100, step))

print(', '.join(str(x) for x in multiples))

