#!/bin/bash

# Today's challenges is to create a script in bash that naviagetes to the document directory and list the files in there
# Then ask the user to create or edit a file and opens the file up in the terminal


# Navigate to the user's Documents directory
cd "$HOME/Documents" || {
    echo "Failed to navigate to Documents directory."
    exit 1
}

# Prompt the user for a filename
read -p "Enter the name of the file to create or edit: " filename

# Open the file with nano
nano "$filename"