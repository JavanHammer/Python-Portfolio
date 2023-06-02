#Counts how many eamils were sent each hour of the day from a data log of email record

#Requests user to input file name
file_name = input("Enter file:")

#Defaults the file name to file "mbox-short.txt" if enter is pressed to speed debugging process
if len(file_name) < 1:
    file_name = "mbox-short.txt"

#Opens file
file_handle = open(file_name)

#Initializes dictionary to count of emails sent each hour
counts = dict()

#Reads each line in the file
for line in file_handle:
    #Removes trailing whitespace
    line = line.rstrip()
    #Splits each line up into a list of words
    words = line.split()
    #Checks each line to make sure a line is not blank and starts with "From"
    if len(words) > 1 and words[0] == ('From'):
        #Parses line to find the time stamp
        time = words[5].split(':')
        #Parses timestamp string to find the hour of the day
        hour = time[0]
        #Update the count of email sent in that hour
        counts[hour] = counts.get(hour, 0) + 1

#Sort the dictionary by hour
countsSorted = sorted(counts.items())

#Print each tuple of hour followed by the count of emails sent within that hour
for hour, count in countsSorted:
    print(hour, count)
