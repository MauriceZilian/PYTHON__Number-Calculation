def main():
    # Initialization
    total = 0.0
    count = 0
    minimum = None
    maximum = None

    # Input loop
    while True:
        entry = input("Please enter a number (or 'done' to exit): ")

        if entry.lower() == 'done':
            break

        try:
            number = float(entry)
            total += number
            count += 1

            if minimum is None or number < minimum:
                minimum = number

            if maximum is None or number > maximum:
                maximum = number

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Output
    print("\nResults:")
    print("Count:", count)
    print("Total:", total)

    if count > 0:
        average = total / count
        print("Average:", average)
    else:
        print("No average to calculate.")

    print("Minimum:", minimum)
    print("Maximum:", maximum)


if __name__ == "__main__":
    main()
