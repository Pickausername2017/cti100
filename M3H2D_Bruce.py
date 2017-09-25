# CTI-110 
# M3HW2 - Discount Calculator
# Denise Bruce
# 24 Sept 2017
# This program calculates bulk discounts for software
#stored variables for this program 
def main ():
    discount_0 = 9  #1-9 software packages
    discount_10 = 19 # 10 - 19 software packages
    discount_20 = 49 # 20 - 49 software packages
    discount_30 = 99 # 50 -99 software packages
    discount_40 = 100 # 100+ Software packages 
    
    number_Retail = float (input('Please enter the quantity'))
    if number_Retail <= discount_0:
        cost =(99* number_Retail)
        print (cost)
    elif number_Retail <= discount_10:
        cost = (99* number_Retail) 
        discount = cost * .10
        print ('discount is')
        print (discount)
        pay = cost - discount
        print ('total amount is')
        print (pay)
    elif number_Retail <= discount_20:
        cost = (99* number_Retail) 
        discount = cost * .20
        print ('discount is')
        print (discount)
        pay = cost - discount
        print ('total amount is')
        print (pay)
    elif number_Retail <= discount_30:
        cost = (99* number_Retail) 
        discount = cost * .30
        print ('discount is')
        print (discount)
        pay = cost - discount
        print ('total amount is')
        print (pay)
    elif number_Retail >= discount_40:
        cost = (99* number_Retail) 
        discount = cost * .40
        print ('discount is')
        print (discount)
        print ('total amount is')
        pay = cost - discount
        print (pay)
    
        


main ()
