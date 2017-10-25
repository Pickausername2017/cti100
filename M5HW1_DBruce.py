# M5HW1_
# Distance Traveled program 
# Denise Bruce 
# 23 Oct 2017

#Write a program that asks the user two questions:\
#I got a late start working on this section, and man did this take a LOT of work!
#after lots of trail and error and lots of going over how loops work since Friday evening
#here is the end result! 


r = 0
d = 0
r =int (input ('What is the vehicles speed in mph?'))
t = int(input('How many hours have you travel?'))
print ('                             ')
print ('Hour', '', 'distace traveld?')
print('------------------------------')
for i in range(1,t+1):
    d = (i * r)
    print ((i), ('        '), (d))
    
 


