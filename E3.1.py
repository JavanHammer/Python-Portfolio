#This program calculates pay (including overtime) with a pay rate and hours worked input

#Request the user for hours worked that week and hourly pay rate
hours = input('Enter Hours:')
rate = input('Enter Rate:')

#Convert from string to float
fh = float(hours)
fr = float(rate)

#Check if overtime rate eligibility
if fh > 40 :
    #Regular pay
    reg = fr*fh
    #Overtime pay
    otp = (fh-40)*(fr*0.5)
    #Total pay
    pay = reg + otp
else:
    #Non-overtime pay
    pay = fh*fr

#Print total pay
print('Pay:',pay)