grades = [] #creating a list to store the grades inputted by the user

#function to input number grades, convert them from str to int and append into the list
def grade_input():
   
    print("Enter your grades as integers from 0 to 100. Type 'finished' when done.")

    #user is prompted to enter their grades one by one
    while True:
        valid = {str(i) for i in range(0,101)}
        gr = input("Enter grade here: ").strip()
        if gr == "finished":
            break
        elif gr not in valid:
            print("Please enter an integer between 0 and 100 or type 'finished' if done. ")
            continue
        try:
            #converting grades inputted by the user into integers
            grade = int(gr)
            #adding inputs into the list
            grades.append(grade)
        #error case handling
        except ValueError:
            print("This is an invalid input. Please enter an integer between 0 and 100 to proceed or type 'finished' if done.")

    print("These are the grades we have recieved:  ", grades)


#function to input the letter grades as strings, convert to integers using the dictionary and add them to the list storing the grades.
def letter():
    print("Enter your grades as letters(ex. A, B-, C+) from A+ to F-. Type 'finished' when done.")
    #creating a dictionary for string to integer calculations
    conversion = {
        'a+':100,
        'a':95,
        'a-':90,
        'b+':85,
        'b':80,
        'b-':75,
        'c+':70,
        'c':65,
        'c-':60,
        'd+':55,
        'd': 50,
        'd-':45,
        'e+':40,
        'e':35,
        'e-':30,
        'f+':25,
        'f':20,
        'f-':15
    }

    #creating a while loop to take inputs
    while True:
        let = input("Enter grade here: ").strip().lower()
        letter_display = []
        if let == "finished":
            break
        if let in conversion:
        #adding the converted integers into the list
            grades.append(conversion[let])
        else:
            #Adding an else statement to handle edge cases and then looping back to taking the input
            print("This is an invalid input. Please enter a letter from A+ to F- or type 'finished' if done.")

    print("These are the numerical grades we converted them too:  ", grades)


while True:
    #checking if user will be inputting letter grades or number grades and reacting accordingly
    choice = input("Are you entering number grades(0) or letter grades?(1): ")
    if choice == "0":
        grade_input() #calling the function
        break
    elif choice == "1":
        letter()
        break
    else:
        print("Invalid input. Please enter '0' for number grades or '1' for letter grades.")


#function to calculate unweighted GPA
def calculate_gpa(grades):
    # GPA formula: ((sum of all grades/number of grades inputted)/100)*4 - 4.0 GPA scale
    gpa = (((sum(grades)/len(grades))/100)*4)
    #printing out the output(unweighted GPA)
    print("Your unweighted gpa is:",round(gpa,2))


#Confirming that the user has inputted the right grades before calculations.
while True:
    confirmation = input("If these are correct enter 'True'. If not, enter 'False': ").strip().lower()
    if confirmation == "true" and len(grades) != 0:
        calculate_gpa(grades) #calling function
        break
    elif confirmation == "false":
        print("Please restart the program to re-enter the grades.")
        break
    else:
        print("Invalid Input. Please enter 'True' or 'False' ")
