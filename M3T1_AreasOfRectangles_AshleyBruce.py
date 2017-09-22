# CTI-110 
# M3T1
# Ashley Denise Bruce
# 22 Sept 2017
# Area of a Rectangle

#input the length and width of rectangle 1
length1= int(input('enter the length of rectange 1:'))
width1= int(input('enter the width of rectange 1:'))
#input the length and width of rectangle 2
length2= int(input('enter the length of rectange 2:'))
width2= int(input('enter the width of rectange 2:'))
#Calculate the area of rectangle 1.
#Calculate the area of rectangle 2
area1 = length1 * width1
area2 = length2 * width2
#possible outcomes 1<2 2<1 1=2
#if area1 > area2 display "Rectangle 1 has the greatest area"
#eles if area2 > area1 display "rectangle2 has the greatest area"
#else display "Both rectangles have the same area"
if area1 > area2:
    print ('Rectangle 1 has the greater area.')
elif area2 > area1:
    print ('Rectangle 2 has the greater area.')
else:
    print ('both have the same area.') 
