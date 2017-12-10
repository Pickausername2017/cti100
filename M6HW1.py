# Program to average test grades and give a letter grade
# 11/13
# CTI-110 M6HW1 - Test Average and Grade
# Densie Bruce
#
total_grades = 5
def main ():
    #Grade entry
    grade_1 = float(input (' Enter Grade 1  '))
    grade_2 = float(input (' Enter Grade 2  '))
    grade_3 = float(input (' Enter Grade 3  '))
    grade_4 = float(input (' Enter Grade 4  '))
    grade_5 = float(input (' Enter Grade 5  '))
    grade_sum = (grade_1+grade_2+grade_3+grade_4+grade_5)
    cal_average(grade_sum)
    letter_grade_1(grade_1)
    letter_grade_2(grade_2)
    letter_grade_3(grade_3)
    letter_grade_4(grade_4)
    letter_grade_5(grade_5)
    
     

def letter_grade_1(grade_1):
    grade = grade_1
    a_Score = 90 
    b_Score = 80
    c_Score = 70 
        
    if grade >= a_Score:
        print ('Grade 1 is: A')
    elif grade >= b_Score:
        print ('Grade 1 is: B')
    elif grade >= c_Score:
        print ('Grade 1 is: C')
    elif grade < c_Score:
        print ('Grade 1 is: F')
        
def letter_grade_2(grade_2):
    grade = grade_2
    a_Score = 90 
    b_Score = 80
    c_Score = 70 
        
    if grade >= a_Score:
        print ('Grade 2 is: A')
    elif grade >= b_Score:
        print ('Grade 2 is: B')
    elif grade >= c_Score:
        print ('Grade 2 is: C')
    elif grade < c_Score:
        print ('Grade 2 is: F')
def letter_grade_3(grade_3):
    grade = grade_3
    a_Score = 90 
    b_Score = 80
    c_Score = 70 
        
    if grade >= a_Score:
        print ('Grade 3 is: A')
    elif grade >= b_Score:
        print ('Grade 3 is: B')
    elif grade >= c_Score:
        print ('Grade 3 is: C')
    elif grade < c_Score:
        print ('Grade 3 is: F')
def letter_grade_4(grade_4):
    grade = grade_4
    a_Score = 90 
    b_Score = 80
    c_Score = 70 
        
    if grade >= a_Score:
        print ('Grade 4 is: A')
    elif grade >= b_Score:
        print ('Grade 4 is: B')
    elif grade >= c_Score:
        print ('Grade 4 is: C')
    elif grade < c_Score:
        print ('Grade 4 is: F')
def letter_grade_5(grade_5):
    grade = grade_5
    a_Score = 90 
    b_Score = 80
    c_Score = 70 
        
    if grade >= a_Score:
        print ('Grade 5 is: A')
    elif grade >= b_Score:
        print ('Grade 5 is: B')
    elif grade >= c_Score:
        print ('Grade 5 is: C')
    elif grade < c_Score:
        print ('Grade 5 is:F')
        
def cal_average (g_sum):
    avg = g_sum/total_grades 
    print (avg, "is the average.")
main()   
        

   
