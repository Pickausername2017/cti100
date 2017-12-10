# A brief description of the project
# 11-14 
# CTI-110 M6HW2 - Random Number Guessing Game
# Denise Bruce 
def main():
    import random
    print ("Welcome to the guessing game")
    b = random.randint(1,100)
    x = float(input("Guess a Number"))
    if x < b:
        print ('Too Low, Try Again')
    if x > b: 
        print ("Too High, Try Again")
    if x == b:
        print ("You Win") 

        
       

main() 
