import time

count = 0

for i in range(100):
    time.sleep(0.3)
    count += 1
    
    if (count % 5 == 0 and count % 3 == 0):
        print("FizzBuzz")
    elif (count % 3 == 0):
        print("Fizz")
    elif (count % 5 == 0):
        print("Buzz")
    else:
        print(count)
