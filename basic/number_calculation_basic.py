# Initialization of variables
total = 0.0
count = 0
minimum = None
maximum = None

# Loop for entering numbers
while True:
    line = input("Please enter a number (or 'done' to exit): ")

    # Exit condition
    if line == 'done':
        break

    try:
        # Convert input to a float
        number = float(line)

        # Update total and count
        total = total + number
        count = count + 1

        # Determine minimum and maximum
        if minimum is None or number < minimum:
            minimum = number

        if maximum is None or number > maximum:
            maximum = number

    # Handle invalid input
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Output results
print('Count:', count)
print('Total:', total)

average = total / count
print('Average:', average)

print('Minimum:', minimum)
print('Maximum:', maximum)
