'''
Multi line comments can be done by using unassigned string literals; just sorta a bug-feature more than an actual feature
'''


# Task 1

age = int(input("\nWhat is your age? "))

if age < 18:
    print("\nYou are a minor!\n")
elif age >= 19 and age <= 64:
    print("\nYou are an adult\n")
elif age >= 65:
    print("\nYou are a senior\n")
else:
    print("\nWhat are you exactly?  Not Born Yet?\n")


# Task 2

username = 'Mister User'
is_logged_in = True

if is_logged_in:
    print("\nWell, " + username + " you happen to be logged in!");
else:
    str(input("\nUser Name: "));
    str(input("\nPassword: "));


# Task 3

grade = float(input("\nPlease tell me your grade (0 - 100): "))

if grade >= 90:
    print("\nGood job! You get an A!\n")
elif grade >=80 and grade <= 89:
        print("\nNice work!  You get a B!\n")
elif grade >=70 and grade <= 79:
        print("\nEh ... mid.  You get a C.\n")
elif grade > 70:
        print("\nPlay it again, you failed this time.  You get an F.\n")


# Task C

way = str(input("\nWhich way would you like to go ... right, or left?: "))

if way == 'left' or way == 'Left' or way == 'LEFT':
    print("\nYou get eaten by a green dragon!\n")
elif way == 'right' or way == 'Right' or way == 'RIGHT':
    print("\nYou find treasure!\n")
else:
    print("\nThat's not a way really ...\n")