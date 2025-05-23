#!/bin/bash

# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 

# This will send Bob an email (if it's run on a Linux system with sendmail that is) a reminder not to open nigerian prince emails every hour.
# It runs forever because users often have short memories regarding such things ...

while true
do

echo "To: bob@solarwinds.com
From: admin@solarwinds.com
Subject: Nigerian Princes Are Not Real

Friendly reminder Bob: Do not open emails from Nigerian prices wishing to share millions of dollars with you. These are fake emails.  If it sounds too good to be true, it probably isnt." | sendmail -t

sleep 3600

done