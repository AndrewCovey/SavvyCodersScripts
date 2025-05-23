#!/bin/bash

# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

  echo -e "\nHow was your day?  Suggested replies: good, bad"
  read -p "Enter your reply: " option

  case $option in

    good)
      echo -e "I am glad you had a good day\n"
      ;;

    bad)
      echo -e "I am sorry you had a bad day.  That sucks...\n"
      ;;

    *)
      echo -e "I have never had a $option day before; is that good or bad?\n"
      ;;
  esac

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty