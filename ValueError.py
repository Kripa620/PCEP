#prompts the user to input an integer and raises a ValueError expection if the input is not a valid integer

try:
    val = int(input("Enter an integer: "))
    print("you picked:", val)

except ValueError:
     print("That is not a valid integer.")
