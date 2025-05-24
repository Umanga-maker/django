import time
start_time = time.perf_counter()
# Initialize counter
count = 0
# While loop runs until count reaches 3
while count < 3:
    print(f"While loop iteration: {count + 1}")
    # For loop iterates over a range of 3
    for i in range(3):
        print(f"  For loop iteration: {i + 1}")
    # Increment the counter
    count += 1

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")