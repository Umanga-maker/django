height = int(input("What is your height in feet?"))
if height >= 3:
    print("You can ride a horse.")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay Rs.150")
    elif 12 > age < 18:
        print("Please pay Rs.200")
    else:
        print("Please pay Rs.250")
else:
    print("You cannot ride.")
print("Bye")

