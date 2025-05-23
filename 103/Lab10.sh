#!/bin/bash

# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is

counter=0

until [ $counter -gt 10 ]
do
  echo -e "Counter value is: $counter, adding one to the counter..."
  ((counter++))
done

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty