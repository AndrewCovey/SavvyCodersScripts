#!/bin/bash

# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

function do_report () {

  echo -e "WHOIS OUTPUT\n------------------------------------------------------------------------------\n" >> $2
  eval "whois $1" >> $2

  echo -e "\n\nDIG OUTPUT\n------------------------------------------------------------------------------\n" >> $2
  eval "dig $1" >> $2

  echo -e "\n\nHOST OUTPUT\n------------------------------------------------------------------------------\nhost" >> $2
  eval "host $1" >> $2

  echo -e "\n\nNSLOOKUP OUTPUT\n------------------------------------------------------------------------------\nnslookup" >> $2
  eval "nslookup $1" >> $2

  echo -e "Report generated in logfile: $2\nThank you and have a nice day!\n"

}

do_report $1 $2

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty