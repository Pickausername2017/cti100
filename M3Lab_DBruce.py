# CTI-110 
# M3Lab - Grade Converter
# Denise Bruce
# 24 September 2017
# Convert numerical grades to letter grades using a 10 point scale. 
def main ():
    # This program takes a number grade and turns it into a letter grade
    # There are four letter Grades, A, B, C, and F
    # There is a 10 point grading scale
    # Below 70 is failing 

    a_Score = 90 
    b_Score = 80 
    c_Score = 70 
    
    score = int (input('Enter grade'))
    if score >= a_Score:
        print ('Your grade is: A')
    elif score >= b_Score:
        print ('Your score is a B')
    elif score >= c_Score:
        print ('Your score is a C')
    elif score < c_Score:
        print ('Your score is F') 
#program starts 
main() 

  



      
         
    
