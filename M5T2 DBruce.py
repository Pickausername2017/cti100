# CTI-110 
# M5T2: Insect Count
# Denise Bruce
# 21 Oct 2017
# This program counts insects over a seven day period

#User Input is needed

def main():
   total = 0 #intialize the accumulator to zero
    
    
    #for each 7 days:
   for day in  range (1,8): #range function will go up to but not include
        print ('Enter the bugs collected on day', day)
        bugs = int(input())# prompts user to enter number of bugs collected for a day
        total = total + bugs #add bugs total 
        
        #add bugs collectd to the total
        print ('you collected a total of', total, 'bugs.')

main() 
