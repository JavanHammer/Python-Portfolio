#Uses a defined function to compute the pay given input of hours worked and pay rate

#Define a function to compute the pay
def compute_pay(hours, rate):
    #Makes overtime pay calculations if necessary
    if fh > 40 :
        reg = fr*fh
        otp = (fh-40)*(fr*0.5)
        pay = reg + otp
    else:
        pay = fh*fr
    print("Returning",pay)
    return pay

#Request user input for hours worked and pay rate
hours = input('Enter Hours:')
rate = input('Enter Rate:')

#Convert the input values to float types
fh = float(hours)
fr = float(rate)

#Calls the compute_pay function to compute the pay
pay = compute_pay(fh,fr)

#Prints the total pay
print('Pay:',pay)