# input() = A function that prompts the user to enter data t
#  returns the data as a string

# name=input("What is your name?: ")
# age=int(input("What is your age?: "))
# cnfAge=input("Are you sure you are {age}? (y/n): ")

# age =age + 1

# print(f"Hello {name}!")
# print(f"Your age is {age}")

# if cnfAge=="y":
#     print("Great!")
# else:
#     print("Please enter the correct age")

# ! Exercise 1 = Rectangle area calculate

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# area = length * width

# print(f"The area of the rectangle is: {area} cm^2")

# ! Exercise 2 = shopping cart program

# product="The available products are: \n1. Apple\n2. Banana "
# print(product)
# item=(("Ypu want to shop?"))
# item=input("Make a choice: \n1. Yes \n2. No\n")
# if item=="1":
#     print("You can shop now!")
# else:
#     print("Thank you for visiting!")
#     exit()
# case1 = "Apple"
# case2 = "Banana"
# price1 = 10 
# price2 = 5   

# buy = input("Enter the product number (1 for Apple, 2 for Banana): ")
# if buy == "1":
#     print(f"You have selected {case1}")
#     price = price1
# elif buy == "2":
#     print(f"You have selected {case2}")
#     price = price2
# else:
#     print("Invalid selection")
#     exit()

# quantity = int(input("Enter the quantity: "))

# total_amount = quantity * price
# print(f"The total amount is {total_amount}")

# print("Thank you for shopping with us!")


# ! Exercise 3 = MADLIBS GAME

# word game where you create a story by filling in the blanks with random words

# adjective1 = input("Enter an adjective: ")
# noun1 = input("Enter a noun: ")
# adjective2 = input("Enter an adjective: ")
# verb1 = input("Enter a verb: ")
# adjective3 = input("Enter an adjective: ")

# print(f"Today i went to {adjective1} zoo.")
# print(f"In an exhibition, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# ! Exercise 4 = BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
height = height / 100
bmi = (weight / (height * height))
print(f"Your hight in cm is: {height}")
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
else:
    print("You are obese")