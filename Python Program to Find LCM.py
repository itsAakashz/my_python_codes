import math


num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))

gcd =math.gcd(num1,num2) 

lcm1= num1*num2/gcd
print(lcm1)
