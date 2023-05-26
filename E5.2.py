#Prompts user for a list of numbers until the user types done. It then computes the largest and smallest numbers without using the maximum or minimum functions. Additionally, it validates user input and gives user error message if input is invalid.

#Initializes smallest and largest varibales to None
largest = None
smallest = None

#Starts an infinite loop
while True:
    #Prompts user for number input (int type)
    num = input("Enter a number: ")
    #If the user is done entering numbers, they can enter "done", to exit the loop
    if num == "done":
        break
    try:
        #Converts the users input to an integer
        num = int(num)
        #Sets the largest and smallest variable to the first number inputted
        if largest is None:
            largest = num
            if smallest is None:
                smallest = num
        #If the current number is greater than the largest number, it stores the current number as the largest value
        elif num > largest:
            largest = num
        #If the current number is smaller than the smallest number, it stores the current number as the smallest value
        elif num < smallest:
            smallest = num
    #Lets user know if their input is invalid
    except:
        print("Invalid input")

#Prints the largest and smallest number that the user inputted
print("Maximum is", largest)
print("Minimum is", smallest)