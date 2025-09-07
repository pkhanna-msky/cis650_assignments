levels = [301, 201, 151, 101, 51, 0]
colors = ['Maroon', 'Purple', 'Red', 'Orange', 'Yellow', 'Green']
concerns = ['Hazardous', 'Very unhealthy', 'Unhealthy', 'Unhealthy for Sensitive Groups', 'Moderate', 'Good',]

def read_input(prompt: str):  #Define a helper function to read and validate input value
    s = input(prompt).strip() #Show the prompt, read what the user typed, remove spaces at ends 
    if s.lower() == 'exit':   #If user typed "exit", (EXIT, Exit, etc.)
        return None          #Return None to signal signal to the main loop to quit
    if not s.isdigit():     #If the input is not all digits (e.g., 'abc', '12.3'. '-5')
        print("Invalid input. Please enter a whole number from the list of levels.")
        return "retry"
    return int(s)

print('Valid levels:', levels)
print('Type "exit" to quit the program.')

while True:
    value = read_input('Enter a level value (or type "exit" to quit): ')
    if value is None:
        print("Exiting the program.")
        break
    if value == "retry":    
        continue

    if value not in levels:
        print('That level is not in the list. Please try again.')
        continue

    idx = levels.index(value)
    print(f'Color: {colors[idx]}, Concern: {concerns[idx]}')

