'''
Write a program to take two two numbers and as an user input and perform the following task-
If the first number is bigger than the second number perform subtraction.
If the first number is smaller than the second number perform addition.
if the two numbers are equal perform multiplication.
'''
num1 = int(input("Enter first number here: "))
num2 = int(input("Enter number 2 here: "))

if num1>num2:
    sub = num1 - num2
    print("The difference between the 2 numbers is ",sub)
elif num1<num2:
    sum = num1 + num2
    print("The sum of the 2 numbers is ",sum)
elif num1 == num2:
    pro = num1*num2
    print("The product of the 2 numbers is ",pro)
