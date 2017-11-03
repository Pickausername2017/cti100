
# M6T1
# Kilometer Conversio
# Denise Bruce
# 2 Nov 2017
#This program converts kilometers to miles
CONVERSION_FACTOR = 0.6214 #global variable
#The main function gets a distance in kilometers and calls
#the show_miles function to convert it.
def main():
    #get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers:'))

    #Display the distance converted to miles
    show_miles (kilometers)
#The show_miles function converts the parameters kim
#kilometrs to miles and displays the result
def show_miles(km):
#calculates miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles
    print(km,'kilometers equals', miles, 'miles.')

main() 
