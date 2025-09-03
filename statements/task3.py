number_items = int(input('Enter the number of items: '))
total = 0.0

for i in range(1, number_items + 1):
    name = input(f'Item {i} name: ')
    unit_price = float(input(f'Item {i} unit price: '))
    quantity = int(input(f'Item {i} quantity: '))
    extended_price = unit_price * quantity
    total += extended_price
    print(f'Item {i}: {name}, unit price: {unit_price:.2f}, quantity: {quantity}, extended price: {extended_price:.2f}')

print(f'Total: {total:.2f}')
