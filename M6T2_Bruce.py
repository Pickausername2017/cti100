# M6T2
# Feet to Inches 
# Denise Bruce
# 2 Nov 2017

#Constant for the number inches per foot.
INCHES_PER_FOOT=12

# main function
def main():
    #get a number of feet from the user
    feet = int(input('Enter a number of feet:'))
# The feet_to_inches function converts feet to inches.       

               
    #Convert that to inches.
    print(feet, 'equals' , feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet* INCHES_PER_FOOT


#Call the main function
main()
