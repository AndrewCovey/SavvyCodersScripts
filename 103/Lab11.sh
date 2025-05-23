#!/bin/bash

# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)

read -p "Please provide side lengths for a triangle, starting with the first side: " num1
read -p "And the second side: " num2
read -p "And the last side: " num3

# Compare numbers
if [[ $num1 -eq $num2 && $num2 -eq $num3 ]]; then
    echo "Your triangle is an EQUILATERAL traingle."
elif [[ $num1 -eq $num2 || $num1 -eq $num3 || $num2 -eq $num3 ]]; then
    echo "Your trianlge is an ISOSCELES triangle."
else
    echo "Your triangle is a SCALENE triangle."
fi

# This is here to keep git bash from insta-closing the powershell window before anyone can see the output...
read -p "Press Enter to continue... " </dev/tty