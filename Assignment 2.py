#Task 1: Check if a Number is Even or Odd
num=int(input("Enter a number: "))
if num % 2 == 0:
    print ( f" {num} is a even number")
else :
    print ( f" {num} is a odd number")


#Task 2: Sum of Integers from 1 to 50 Using a Loop
total_sum = 0
for number in range(1, 51):
    total_sum += number
print("The sum of integers from 1 to 50 is: {total_sum}")