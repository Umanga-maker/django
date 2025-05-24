import time
start_time = time.perf_counter()
for i in range(1,4):
    print(f"Outer loop iteration: {i}")

    j=1
    while j <=3:
        print(f"   Inner loop iteration: j = {j}")
        j += 1

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")