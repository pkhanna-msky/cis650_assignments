name = input('Enter your name: ')
age_input = input('Enter your age: ')

if not name:
    print('Error: Name cannot be blank. ')

if not age_input.isdigit():
    print('Error: Age must be a number. ')

age = int(age_input)

if age <= 0:
    print ('You are not born yet')
elif age < 18:
    print('You are a minor')
elif age <= 99:
    print('Adult')
else:
    print('Nice to meet you')

print ('done with ')