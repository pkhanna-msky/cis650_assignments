while True:
    raw = input('Enter an integer: ')
    try:
        n = int(raw)
        break
    except ValueError:
        print('Error: please enter a whole number (e.g., -5, 0, 12). ')

if n == 0:
    mutiples = [0]
else:
    step = abs(n)
    mutiples = list(range(0, 100, step))

print(', '.join(str(x) for x in mutiples))

