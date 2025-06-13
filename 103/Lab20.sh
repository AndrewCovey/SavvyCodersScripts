#!/bin/bash
# Write a script that counts the number of the lines in a file.
# Hint need to use the wc command.

# Prompt the user for a file name
read -p "Enter the name of the file: " filename

# Check if the file exists
if [[ -f "$filename" ]]; then
    # Count and display the number of lines
    lines=$(wc -l < "$filename")
    echo "The file '$filename' has $lines lines."
else
    echo "File not found: $filename"
    exit 1
fi