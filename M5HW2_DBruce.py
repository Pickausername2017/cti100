# M5HW2
# Calculatng Program 
# Denise Bruce 
# 22 Oct 2017

#Write a program that calculates a running total

grade = 1
grade_1 = 0
print('Enter Grades')
print('Enter 0 to quit.')
while grade > -1:                           
    print('Current Sum of Grades:', grade_1)            
    grade = float(input('Grade? '))        
    grade_1 = grade_1 + grade                          
print('Total Sum =', grade_1)
