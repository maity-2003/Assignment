#Task 1: Calculate Factorial Using a Function

n= int(input("Enter a number: "))
def factorial(n):
 if n < 2 :
  return 1
 else:
  return (n*factorial(n-1))

result = factorial(n)
print  (f"Factorial of {n} is :" ,result)


#Task 2: Using the Math Module for Calculations

a = int(input("Enter a number: "))
def square(a):
 return pow(a,1/2)

result = square(a)
print("Square root : " , result)

import math
log = math.log(a)
print("Logarithm : ", log)

import math
sin = math.sin(a)
print("Sine : ", sin)
