import time
by5 = 0
by3 = 0
count = 0
while True:
    time.sleep(0.3)
    count += 1
    by5 = count / 5
    by3 = count / 3
    by5 = str(by5)
    by3 = str(by3)
    
    by5array = by5.split(".")
    by3array = by3.split(".")
    
    if (by3array[1][0] == "0" and by5array[1][0] == "0"):
        print("FizzBuzz")
    elif (by3array[1][0] == "0"):
        print("Fizz")
    elif (by5array[1][0] == "0"):
        print("Buzz")
    else:
        print(count)
