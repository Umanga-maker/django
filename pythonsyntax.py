base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Dave", "IT Support")

# Returning Values
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,8)
area_b = area_triangle(3,9)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def greeting(name):
    print("Welcome, " + name)

result = greeting("Cristiano")
print(result)# output is none because there is no return statement in the function

# Code reuse
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

# logical operators
print("yellow" > "cyan" and "purple" < "red") # alphabetical order #both statement needs to be true for "and" operator
print(25 > 50 or 1 != 2) # If 1 statement is true then the output is true
print(not 1 == 2) # gives the opposite output(True for false & false for true)







