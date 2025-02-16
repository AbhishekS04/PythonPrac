# friend=10
# friend = friend + 1
# friend +=

# friend = friend -1
# friend -= 1

# friend = friend * 2
# friend *= 2

# friend = friend / 2
# friend /= 2

# friend = friend % 2
# friend  %= 2

# print(friend)


# ! built in functions

# x=3.14
# y=-4
# z=5
# print(round(x))
# print(abs(y))
# print(pow(z,2))
# print(max(x,y,z))

#  ! Math module

import math

# x=9.1

# print (math.pi)
# print(math.e)
# print (math.sqrt(16))


# print(math.floor(x))
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

# radius = input("Enter the radius of the circle: ")
# radius = float(radius)
# circumference = 2* math.pi * radius
# print(round(circumference))

# !

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * math.pow(radius,2)
# print(round(area,2))

# !

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

c=math.sqrt( pow(a,2)+pow(b,2))
print(f"Side c= {c}")