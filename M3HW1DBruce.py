# CTI-110 
# M3HW1 - Age Classifier
# Denise Bruce
# 24 Sept 2017
# This program classifies people based on age.
#
# These are the variables for age ranges.
#Infants 0 - 1 years old
#Child 2 - 12 years old 
# Teen 13-18 years old
# Adult 20 + Years old

def main(): 
    class_1 = 1
    class_2 = 12
    class_3 = 19
    class_4 =20

    age = int (input('Enter age'))
    if age <= class_1:
        print ('Class is Infant') 
    elif age <= class_2:
        print ('Class is Child')
    elif age <= class_3:
        print ('Class is Teen')
    elif age >= class_4:
        print('Class is Adult') 
main() 
# Start program 
