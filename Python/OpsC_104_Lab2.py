# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.

num1 = int(input("Input an integer, 1-10: "))
num2 = int(input("Input another integer, 1-10: "))

if (num1 == num2):
    print("Number 1 is equal to number 2!")
if (num1 != num2):
    print("Number 1 is not equal to number 2")
if (num1 < num2):
    print("Number 1 is less than number 2")
if (num1 <= num2):
    print("Number 1 is less or equal to number 2")
if (num1 > num2):
    print("Number 1 is greater than number 2")
if (num1 >= num2):
    print("Number 1 is greater or equal to number 2")
#else:
#    print("No conditions were met ...  Shouldn't happen!")
# Stretch Goals (Optional Objectives)

# Pursue stretch goals if you are a more advanced user or have remaining lab time.


# Create an if statement with two conditions by using and between conditions.
#
if ( 1 <= num1 and num1 <= 10):
    print("You followed directions for number 1, yay you!")

# Create an if statement with two conditions by using or between conditions.

if ( num1 >= 1 or num2 <= 10):
    print("You followed at least 1/4th of the directions!")

# Create a nested if statement.

if (num1 == num2):
    if (num1 != num2):
        print ("This should never happen")
    else:
    print("Reality is not broken")
    
# Hint:  a = int(input("Enter a number "))