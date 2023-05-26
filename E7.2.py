#This program computes the average of specific numbers located in certain lines throughout a file

#Prompts the userto input file name (Use the file name "mbox-short.txt")
file_name = input("Enter file name: ")

#Opens the file
file_handle = open(file_name)

#Initializes a counter and total to keep track of how many data points are being used and what their running total is
count = 0
total = 0

#Reads each line in the file
for line in file_handle:
    #Checks if the line starts with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        #If not, it will skip to the next line
        continue
    #If the line does start with "X-DSPAM-Confidence:", it increases the data point counter
    count = count + 1
    #Then it will parse the number out of the line, convert the data point into a float value, and add it to the running total
    total = total + float(line[20:])

#After all lines have been processed, it calculates and prints the average spam confidence
print("Average spam confidence:", total/count)
