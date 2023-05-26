#This program uses regular expressions to parse a text file finding all of the numbers within the file and adding them together to find the sum.

#Import regular expressions package
import re

#Imports file
file_name = "regexsum.txt"

#Opens file
file_handle = open(file_name)

#Initializes variable for running total
total = 0

#Reads through each line in the file
for line in file_handle:
    #Removes trailing whitespace
    line = line.rstrip()
    #Parses each line for numbers
    numbers = re.findall('[0-9]+', line)
    #Loops through each number so it can add each one to the running total
    for number in numbers:
        number = int(number) #Converts number string into int type
        total = total + number

#Prints the sum
print(total)