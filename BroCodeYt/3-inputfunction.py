# input() = A function that prompts the user to enter data t
#  returns the data as a string

name=input("What is your name?: ")
age=int(input("What is your age?: "))
cnfAge=input("Are you sure you are {age}? (y/n): ")

age =age + 1

print(f"Hello {name}!")
print(f"Your age is {age}")

# if cnfAge=="y":
#     print("Great!")
# else:
#     print("Please enter the correct age")