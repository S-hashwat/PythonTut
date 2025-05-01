total_sum = 0

while True:
    user_input = input("Enter a number (or type 'No' to stop): ")
    
    if user_input.lower() == 'no':
        break
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'No' to stop.")

print("The total sum of the numbers is:", total_sum)