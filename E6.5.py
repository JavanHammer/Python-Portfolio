#Extracts a floating point number from any given string/line

#Text subject
text = "X-DSPAM-Confidence:    0.8475"

#Finds the index of ":" character
ipos = text.find(':')

#Parses the number string from the line
piece = text[ipos+1:]

#Converts number string to float type
num = float(piece)

#Prints float type number that was contained in the line
print(num)