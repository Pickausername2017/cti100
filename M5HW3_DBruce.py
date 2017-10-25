# M5HW13_
# Factorial 
# Denise Bruce 
# 23 Oct 2017
def main():

    n = int(input('enter number'))
    f= 1
# check if the number 
    if n < 0:
       print("Enter a Positive Interger")
    elif n == 0:
       print("The factorial of 0 is 1")
    else:
        for i in range(1,n+ 1):  
            f = f*i
            print("The factorial of",n,"is",f)

main()
