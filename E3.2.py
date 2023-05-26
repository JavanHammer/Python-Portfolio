#This program gives a letter grade for a score inputted and also validates the input value

#Requests user input and converts it to a float type
score = float(input("Enter Score: "))

#The following if/elifs checks if the value is within each grade boundary
if score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
elif score < 0.6:
    grade = "F"
else:
    #Validates user input by giving an error message if invalid value
    print("Please enter a valid value")
    quit()

#Prints letter grade
print('Your grade is',grade)