'''
Write a program to take two two numbers and as an user input and perform the following task-

Use Ternary Operator to find smaller number among two and print it.
Bitwise AND 
Bitwise OR
Bitwise NOT for first number
1 bit LEFT and 2 bit  RIGHT shift of second number
'''
num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))

smaller = num1 if num1<num2 else num2
print("The smaller number is ",smaller)

bitwiseAnd = num1 & num2
print("The Bitwise And of num1 and num2 is ",bitwiseAnd)

bitwiseOr = num1 | num2
print("The Bitwise Or of these numbers is ",bitwiseOr)

bitwiseNot = ~ num1
print("The Bitwise Not of num1 is ",bitwiseNot)

a = num1<<1
print("The left shift on num1 is ",a)

b= num2>>2
print("The right shift by 2 on num2 is ",b)
