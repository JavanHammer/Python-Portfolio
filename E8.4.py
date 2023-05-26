#This program will read through a file, find, and print all of the words contained in the text file in ascending order with no repeats.

#Prompts the user to input the name of the file (Enter "romeo.txt")
file_name = input("Enter file name: ")

#Opens file
file_handle = open(file_name)

#Initializes list to store the unique words in
lst = list()

#Reads each line in the file
for line in file_handle:
    #Removes trailing whitespace
    line = line.rstrip()
    #Splits each line up into words
    words = line.split()
    #Loops over each word
    for word in words:
        #If the word is already in the list then it gets skipped
        if word in lst:
            continue
        #If the word is new (not in the list), then it gets added to the list
        lst.append(word)

#Sorts the list of unique words
lst.sort()

#Prints out the sorted list of unique words
print(lst)