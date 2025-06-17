#########################################################################################################################################################
#  Very simple I/O script that does some rather basic stuff; gets a variable from the user and pukes it out at them later...                            #
#########################################################################################################################################################

name = input("\nEnter your name please: ")
age = input("Enter your age: ")
school_stat = input("Are you in school right now (Y/N): ")
fav_lang = input("What programming language are you most interested in: ")

if school_stat == "Y" or school_stat == "y":
    school = " in "
if school_stat == "N" or school_stat == "n":
    school = " not in "

print ("\n\nHello, " + name + ".\nYou are " + age + " years old, and you are" + school + "school right now.\nYou are interested in the " + fav_lang + " programming language.\nHave a nice day!")