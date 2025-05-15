#!/bin/bash

# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

do_report ($uname) {

echo -en "Basic math script...  Enter two integers and a basic math operator.\nEnter an integer: "
read anum1

echo -n "Enter another integer: "
read anum2

echo -n "New enter a mathematical operator ('+', '-', '*', or '/'): "
read moper

let answer=$anum1$moper$anum2
echo "The answer to $anum1 $moper $anum2 is: $answer"

}

do_math

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty