#!/bin/bash

# Lets create a script that would work like a DDOS attack by using a while loop
# In this script we want to contiune to ping our personal pc in a infitine while loop
# Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash
# To End the loop try pressing control z or control c
# Stretch Goal:
# Can you do this with an until loop to have it execute a specfic number of times?

while true
do
  ping 127.0.0.1
done

# STRETCH

# Safe version for demonstration: forks a few pings processes to localhost, and stops running once it's all accomplished. 
# Runs quietly also This likes to run as admin/root b/c of the -c option with ping.
#for i in {1..5}; do
#  ping -c 4 127.0.0.1 > /dev/null &
#  echo "Started ping process $i"
#done

#wait
#echo "All ping processes finished."

# END STRETCH


# SUPER-DUPER STRETCH  

# Very not safe version for edification only: forks as many ping processes as it can to localhost, and stops running quietly pretty much never ...

#while true
#do
#  ping -c 4 127.0.0.1 > /dev/null &
#  echo "Enjoy the ride..."
#done

#wait
#echo "All ping processes finished.  How'd ya get here anyways?"

#END SUPER_DUPER STRETCH