import time
by5 = 0
by3 = 0
count = 0
while True:
    time.sleep(0.3)
    count += 1
    by5 = count / 5
    by3 = count / 3
    # print("by5: " + str(by5) + " by3: " + str(by3))
    if (str(by3)[2] == "0" and str(by5)[2] == "0"):
        print("FizzBuzz")
    elif (str(by3)[2] == "0"):
        print("Fizz")
    elif (str(by5)[2] == "0"):
        print("Buzz")
    else:
        print(count)