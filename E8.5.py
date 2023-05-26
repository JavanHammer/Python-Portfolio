#Scrapes a file for email addresses and provides a count of how many were found at the end.

#Prompts the user for the file name (Enter "mbox-short.txt" as file name)
file_name = input("Enter file name: ")
#Defaulted the file name to "mbox-short.txt" to speed up debugging
if len(file_name) < 1:
    file_name = "mbox-short.txt"

#Opens file
file_handle = open(file_name)

#Initializes email counter
count = 0

#Reads throught the lines of the file
for line in file_handle:
    #Removes trailing whitespace
    line = line.rstrip()
    #Splits up each line into words
    words = line.split()
    #Checks each line to make sure a line is not blank and starts with "From"
    if len(words) > 1 and words[0] == ('From'):
        #Keeps track of email count throughout file
        count = count+1
        #Prints out email
        print(words[1])

#Once it's finished scraping the whole file and printing out each email it found along the way, it prints out how many emails it found throughout the file.
print("There were", count, "lines in the file with From as the first word")