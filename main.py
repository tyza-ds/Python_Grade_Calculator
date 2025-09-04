# <editor-fold desc="Exercise 1">
"""# Q1
def Q1():
    name = "Zaty"
    age = 28
    is_student = True

    print(f"Name: {name} | Age: {age} | Student: {is_student}")


# Q2
def Q2():
    name, age = input("Enter Name and Age: ").split()
    print(f"Name: {name} | Age: {age}")


# Q3
def Q3():
    colour = input("What is your favorite colour: ")
    print(f"Your favorite colour is {colour}!")


# Q4
# string
def Q4():
    no1, no2 = input("Enter 2 number: ").split()

    # string to int
    no1 = int(no1)
    no2 = int(no2)

    # print the result
    no_sum = no1 + no2
    no_product = no1 * no2
    no_difference = no1 - no2

    print(f"{no_sum},{no_product},{abs(no_difference)}")


# Q5
def Q5():
    numberInput = input("Enter a number: ")
    numberInput = int(numberInput)
    result_square = numberInput * numberInput
    result_cube = numberInput * numberInput * numberInput

    print(f"{result_square}, {result_cube}")


# Q6
def Q6():
    input_float = input("Enter decimal number: ")
    convert_float = float(input_float)
    number_divide = convert_float / 2

    print(number_divide)


# Q7
def Q7():
    no1, no2, no3, no4 = input("Enter 4 digit: ").split()
    no1 = int(no1)
    no2 = int(no2)
    no3 = int(no3)
    no4 = int(no4)

    sum_digit = no1 + no2 + no3 + no4
    product_digit = no1 * no2 * no3 * no4

    sub_no = no1 - no2

    print(f"Sum: {sum_digit}, Product: {product_digit}")
    print(f"Number 1: {no1}, Number 2: {no2}, Number 3: {no3}, Number 4: {no4}")

    # Q6()
"""

# </editor-fold>

# <editor-fold desc="template">
"""

"""
# </editor-fold>

# <editor-fold desc="Input/Output">
"""
name = input("What's your name? ")
year = int(input("What year were you born? "))
age = 2025 - year

print(f"Hi {name}! You are {age}")
"""
# </editor-fold>

# <editor-fold desc="Mark Calculation">
"""
hw = float(input("Enter homework marks: "))
exam = float(input("Enter exam marks: "))
discuss= float(input("Enter discussion marks: "))

total = (hw*0.4) + (exam*0.5) + (discuss*0.1)

print(f"Total marks: {total:.2f}")
print("Total marks: %.2f"%total)
"""
# </editor-fold>

# <editor-fold desc="template">
"""
hw = float(input("Enter homework marks: "))
    exam = float(input("Enter exam marks: "))
    discuss = float(input("Enter discussion marks: "))

    total = (hw * 0.4) + (exam * 0.5) + (discuss * 0.1)

    print(f"Total marks: {total:.2f}")
    print("Total marks: %.2f" % total)
"""
# </editor-fold>

# <editor-fold desc="Week 2 Lab">
"""
parcel_weight_input = float(input("What is the parcel weight (kg)?: "))

if parcel_weight_input < 2.5:
    print("RM6")
elif (parcel_weight_input >= 2.5) and (parcel_weight_input <= 5):
    print("RM5.5")
elif parcel_weight_input > 5:
    print("RM5")
"""
"""
sum = 0.0

count = 0

x = eval(input("Enter a number (negative to quit) >> "))

while x >= 0:

      sum = sum + x

      count = count + 1

      x = eval(input("Enter a number (negative to quit) >> "))

print("\nThe average of the numbers is", sum / count)
"""

"""
numbers = [4, 23, 32, 12, 88]

for value in numbers:

    if value >= 20:

      print('Large number', value)

print("Done")
"""

"""
# Initialize an empty list to store the numbers
numbers = []

# Prompt the user to enter numbers until -1 is entered
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

# Check if any numbers were entered
if numbers:
    total = len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / total

    # Display results in the required format
    print(f"You entered {total} numbers.")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Average: {average:.2f}")
else:
    print("No numbers were entered.")

"""
# </editor-fold>

# <editor-fold desc="LAB 3">
"""

def part_a_1():
    input_no = float(input("Enter a number: "))
    result = input_no % 2

    division = input_no / 2
    remainder = input_no % 2

    print(f"This is division: {division}\n This is remainder: {remainder}")

    print(result)

    if input_no % 2 == 0:
        print("This is even!")
    elif input_no % 2 != 0:
        print("This is Odd!")


def part_a_2():
    grade_input = float(input("Enter you score: "))

    if grade_input >= 90 and grade_input <= 100:
        print("Your grade is A")
    elif grade_input >= 80 and grade_input <= 89:
        print("Your grade is B")
    elif grade_input >= 70 and grade_input <= 79:
        print("Your grade is C")
    elif grade_input >= 1 and grade_input <= 69:
        print("Your grade is F")
    else:
        print("Error")


def part_b_3():
    loop_number = 1

    while loop_number <= 10:
        print(loop_number)
        loop_number += 1


def part_b_4():
    input_number = int(input("Enter a number (N):  "))
    total = 0
    for counter in range(1, input_number + 1):
        total = total + counter

    print("The sum of numbers from 1 to", input_number, "is:", total)


def part_b_5():
    input_number = int(input("Enter a multiplication number: "))
    for counter in range(1, 11):
        print(f"{input_number} x {counter} = {input_number * counter}")


def part_c_6():
    correct_password = "namasayazaty"
    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:
        entered_password = input("Enter password: ")

        if entered_password == correct_password:
            print("Access granted!")
            break
        else:
            attempt += 1
            print(f"Incorrect password. Please try again. attempt = {max_attempts - attempt} ")
            if attempt < max_attempts:
                print(f"You have {max_attempts - attempt} attempt(s) left.")
            else:
                print("Too many failed attempts. Access Denied.")

"""
# part_a_1()
# part_a_2()
# part_b_3()
# part_b_4()
# part_b_5()
# part_c_6()
# </editor-fold>

# <editor-fold desc="W3LA1">

"""
def celsius_to_fahrenheit(c):
    return (9 / 5) * c + 32


def display():
    print("Enter temperature in celsius (Type 'done' to finish)")
    while True:
        temp = input("Celsius: ")
        if temp.lower() == "done":
            break
        else:
            celsius = float(temp)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} °C is {fahrenheit: .2f} °F")

"""

# </editor-fold>

# <editor-fold desc="W3LA2">

"""
def find_largest(a, b, c):
    return max(a, b, c)


def display():
    print("Enter three numbers:")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    num3 = float(input("Third number: "))

    largest = find_largest(num1, num2, num3)
    print(f"The largest number is: {largest}")


# Call display() to run the program

display()
"""


# </editor-fold>

# <editor-fold desc="W3LB3">


def multiples(n, limit):
    result = []
    for i in range(n, limit + 1, n):
        result.append(i)
    return result


# </editor-fold>
