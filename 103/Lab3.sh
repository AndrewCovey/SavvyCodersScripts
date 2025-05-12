#!/bin/bash

echo -n "Enter a number: "
read anum

if [ $anum -gt 5 ]; then
  echo "your number is greater than 5"
elif [ $anum -lt 5 ]; then
  echo "your number is less than 5"
else
  echo "your number is five."
fi

# This is here to keep git bash from just shutting the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty