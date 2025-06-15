#prompts the user to input two numbers and raises a ValueError exception if the inputs are not numerical

def num(prompt):
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Invalid Input.")

num1 = num("Enter the 1st number: ")
num2 = num("Enter the 2nd number: ")

print(num1)
print(num2)
