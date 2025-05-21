#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

while true
do

echo -e "\n\nChoose an activity by typing in a number:\n1 - Say 'Hello, World!'\n2 - Ping The Evil Empire (Google)\n3 - Run ifconfig\n4 - For The Love Of God, Stop!"
read -p "Enter your choice: " option

case $option in

  1)
    echo -n "Hello, World!"
    ;;

  2)
    eval ping google.com
    ;;

  3)
    eval ifconfig -a
    ;;

  4)
    exit 1
    ;;

  *)
    echo -n "Invalid entry; Play It Again Carl!"
    ;;
esac

done