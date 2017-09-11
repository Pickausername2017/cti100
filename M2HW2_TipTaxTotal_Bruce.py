# CTI-110 
# M2HW2 - Tip Tax Total 
# Denise Bruce
# 10 Sept 2017
# Tip Calculator
#Calculate Tip
#Asks for the amount of the food, requires user input
foodCost = float(input("how much is the subtotal?"))
#Calculates tip amount, based on a 18 percent tip
tipAmount = float(foodCost*.18)
#Calculates the sales tax at 7 percent
salesTax= float(foodCost*0.07)
#Displays the tip amount
print( "Tip is," , tipAmount)
#displays the amount of sales tax
print("Tax is,", salesTax)
#displays the total cost of the bill 
print("Total is,", foodCost+tipAmount+salesTax)

 
