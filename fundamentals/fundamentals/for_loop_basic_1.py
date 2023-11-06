#basic

for i in range (0,151):
    print(i)
#multiple of five
for i in range (5,1001,5):
    print(i)
#counting the dojo way
for integer in range (1,101):
    if integer % 10 == 0:
       print ("Coding Dojo")
    elif integer % 5 == 0:
         print ("Coding")
    else:
        print(integer)
#Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001,2):
    sum += i 
    print(i)        
# Countdown by Fours 
for i in range(2018,0,-4) :
    print(i)      
#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum +1):
    if i%mult==0:
        print(i)

