a= int(input()) 
b= int(input()) 
c= int(input()) 
x= int

if (c<0 and b!=c**2) or (a==0 and b!=c**2): #Checking if the equation does exist with these a, b and c
    print ('NO SOLUTION')
elif (a==b==c==0) or (a==0 and b==c**2): #Checking if the x collapses and 2 remaining numbers are equal
    print ('MANY SOLUTIONS')
else:
    x = int((c**2 - b)/a)
    if (a*x + b)<0 or (c**2 - b)%a !=0: #Checking if x is integer
        print('NO SOLUTION')
    else:
        print(x)
