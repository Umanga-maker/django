x = 0
while not (1 <=x<= 100):
    x=int(input("Please enter a number between 1 and 100: "))
print("valid no", x)


for i in range(7):
    x=int(input("Please enter a number between 1 and 100: "))
    if 1 <=x<= 100:
        print("valid no, x")
        break
    else:
        print("Invalid number. Try again.")

number=int(input("enter a number(-1 to quit)"))
while number != -1:
    print(number)
    number = int(input("Enter anumber(-1 to quit)"))
else:
    print("in else block")
print("out from loop")

count = 0
while True:
    print(count)
    count += 1
    if count==5:
        break
else:
    print("in else block")#this else block won't be executed because the loop is forcefully terminated
print("out from loop")

numbers = [3, 2, 4]

for num in numbers:
    print(f"Counting down from {num}:")
    while num > 0:
        print(num)
        num -= 1
    print("Done!\n")