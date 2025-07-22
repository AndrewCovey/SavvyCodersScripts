#Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this. 💪

#Write your code below this line 👇

ppl = int(input("How many people are paying? "))
cost = float(input("What was the total for the bill? $"))
tip = int(input("What percent will you tip? "))

tot = (1 + (tip / 100)) * cost
amt = round(tot/ppl,3)

# or, harder to read ...
amt =  round(((1 + (tip / 100)) * cost)/ppl,3)

print("Each person should pay $" + str(amt))