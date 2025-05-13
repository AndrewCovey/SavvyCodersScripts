#!/bin/bash

echo -en "Basic math script...  Enter two integers and a basic math operator.\nEnter an integer: "
read anum1

echo -n "Enter another integer: "
read anum2

echo -n "New enter a mathematical operator ('+', '-', '*', or '/'): "
read moper

let answer=$anum1$moper$anum2
echo "The answer to $anum1 $moper $anum2 is: $answer"

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty