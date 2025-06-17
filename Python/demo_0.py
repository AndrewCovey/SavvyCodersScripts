#########################################################################################################################################################
#  Very simple I/O script that does some rather basic stuff; gets a variable from the user and pukes it out at them if they entered the right           #
#  class name.                                                                                                                                          #
#                                                                                                                                                       #
#########################################################################################################################################################

class_name = input("\n\nEnter A Class Name? ");

if class_name == "SecOps Class":
    print("\nCorrect, we are in " + class_name + ".")
else:
    print("\nThat's not the right class name doofas...\nYou are supposed to be in 'SecOps Class'.");

