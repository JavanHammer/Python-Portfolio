#This program scrapes a file for eamils and prints out each email along with how many times each email was found within the file.

#Prompts the user for the file name
file_name = input("Enter file: ")
#Defaulted the file name to "mbox-short.txt" to speed up debugging
if len(file_name) < 1:
    file_name = "mbox-short.txt"

#Opens file
file_handle = open(file_name)

#Initializes dictionary to count occurences of each email address showing up
counts = dict()

#Reads through each line of the file
for line in file_handle:
    #Removes trailing whitespace
    line = line.rstrip()
    #Splits up each line into words
    words = line.split()
    #Checks each line to make sure a line is not blank and starts with "From"
    if len(words) > 1 and words[0] == ('From'):
        #Gets email address
        email = words[1]
        #Adds email to dictionary if not already in it and then it updates the count of how many times it has been found within the text file
        counts[email] = counts.get(email, 0) + 1

#Initializes variables to keep track of which email showed up the most and how many times that email showed up
highest_email_occurence = None
email_with_highest_count = None

#Loops through dictionary to find the email with the highest count and count number
for email, count in counts.items():
    if highest_email_occurence is None or count > highest_email_occurence:
        #Updates variables with highest count if conditions are met for highest counted email
        email_with_highest_count = email
        highest_email_occurence = count

#Prints the email with the highest frequency followed by the amount of times that email came up in the file
print (email_with_highest_count, highest_email_occurence)