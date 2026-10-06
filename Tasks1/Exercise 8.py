import random
import time
def multiplyTableTest():
    first, second, mistake = 0,0,0
    startTime = time.time()
    for i in range(0, 10):
        first = random.randint(1,10)
        second = random.randint(1,10)
        mult = first * second

        
        ans = int(input(f"{i+1}. {first} * {second} = "))

        if  mult != ans:
            mistake += 1
    endTime = time.time()
    averageTime = (endTime - startTime) / 10
    print(f"Average Time: {averageTime:.2f} seconds")
    return mistake

mistakes = multiplyTableTest()
if mistakes == 0:
    print("Excellent.")
elif mistakes == 1:
    print("Very good.")
elif mistakes <= 3:
    print("Good.")
elif mistakes < 7:
    print("Average.")
elif mistakes < 10:
    print("You should rework this table.")
else:
    print("You MUST rework this table.")
