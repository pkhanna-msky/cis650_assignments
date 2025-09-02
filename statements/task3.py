num_items = int(input('Enter the number of items: '))
total = 0.0

for i in range(num_items + 1):
    name = input(f'Enter the name of item {i} name: ')
    unit_price = float(input(f'Enter the unit price of item {i} unit price: '))
    quantity = int(input(f'Enter the quantity of item {i} quantity: '))
    extended_price = unit_price * quantity
    total += extended_price
    print(f'Item {i}: {name}, unit price: {unit_price}, quantity: {quantity}, extended price: {extended_price}')

print(f'Total price for all items: {total}')
