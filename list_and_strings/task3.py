per_line = 10
count = 0

for code in range(32, 127):
    print(f'{code:3}', end=' ')
    count += 1
    if count == per_line:
        print()
        
        if count % per_line != 0:
            print()
            