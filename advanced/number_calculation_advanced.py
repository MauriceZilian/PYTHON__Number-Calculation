# Initialize an empty list to store the numbers
numbers = []

# Welcome message and instructions
print("Welcome! This program helps you calculate the maximum, minimum, and average of your inputs.")
print("Enter a number and press Enter. Type 'done' to finish.")

while True:
    user_input = input('\nEnter a number: ')
    
    if user_input.lower() == 'done':
        break
        
    try:
        number = float(user_input)
        numbers.append(number)
        
    except ValueError:
        print('Invalid input! Please enter a valid number.')

# Check if any valid numbers were entered
if numbers:
    # Perform calculations
    average = sum(numbers) / len(numbers)
    
    # Display the results
    print("\n" + "="*40)  # A line for better visual structure
    print(f"Results:")
    print(f"---------------------------")
    print(f"Maximum: {max(numbers):.2f}")  # Format to 2 decimal places
    print(f"Minimum: {min(numbers):.2f}")
    print(f"Average: {average:.2f}")
    print(f"---------------------------")
    print("="*40)
else:
    print("\nNo valid numbers were entered.")
