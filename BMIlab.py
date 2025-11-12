print("BMI Calculator (Python)")
#ask for user name -EP
theyName = input("what is your name: ")
#ask for user weight -EP
theyWeight = input("what is your weight: ")
#ask for user wight -EP
theyHeight = input("what is your height: ")
#prints name,weight, and height -EP
print(f"Name: " + theyName + " WightL " + theyWeight + " Height: " + theyHeight)# ---------------------------------------------


# BMI Calculator Program
# Get user input for name, height and weight
# Make sure height and weight are positive
# Calculate and display BMI value and BMI category
# ---------------------------------------------

def getPositiveNumber(prompt):
    """
    Ask the user for a positive number using a while loop.
    Repeats until the user enters a value greater than 0.
    """
    value = 0
    while value <= 0:
        # Prompt the user for input
        value = float(input(prompt))
        # Check if input is positive
        if value <= 0:
            print("Please enter a positive number greater than zero.")
    return value


