temperature = 15
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# Ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

#Logical Operators
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

user = 'Admin'
logged_in = False

if user == "Admin" or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

user = 'Admin'
logged_in = True

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


number = int(input("Enter a number: "))
if number > 0: # checking positive number
    if number %2 == 0:
        print("this is even number")
    else:
        print("this is odd number")
else:
    if number == 0:
        print("this is zero")
    else:
        print("this is a negative number")

age = 16
status = "Major" if age >= 18 else "Minor"
print(status)

Y = int(input("Enter the year you want to check: "))
Year = Y%4

Status = "Leap year" if Year == 0 else "Not a Leap Year"

print(Status)

value = None
if value:
    print("Value is True")
else:
    print("Value is False")

def greeting(details):
    match details:
        case [time, name] if time == "Afternoon":
            return f'Good {time} {name}!'
        case [time, name] if time == "Morning":
            return f'Good {time} {name}!'
        case [time, *names] if time == "Evening":
            msg=''
            for name in names:
                msg+=f'Good {time} {name}!\n'
            return msg
        
print (greeting(["Morning", "Ravi"]))
print (greeting(["Morning", "Guest"]))
print (greeting(["Evening", "David", "Kajal", "Preeti"]))



        



