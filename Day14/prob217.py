nums = [1,2,3,4,1,5,2]
seen = set() #variable for set to add unique numbers

for num in nums:
    if num in seen: # if num matches the number in seen
        print("Output:", True)
        break
    seen.add(num) # adding from num to seen
else:
    print("Output:",False)