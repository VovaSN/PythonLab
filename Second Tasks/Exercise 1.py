import random
MAX_RANGE = 999

def playerGuess():
    guessNumber = random.randint(1,MAX_RANGE)
    attempts = ans = 0
    while 1:
        ans = int(input(f"\nEnter integer number(1-{MAX_RANGE}): "))

        attempts += 1

        if(ans > guessNumber):
            print(f"Secret number is less than: {ans}")

        elif(ans < guessNumber):
            print(f"Secret number is greater than: {ans}")
        else:
            print(f"You guessed the number. Congratulations!\n Total attempts {attempts}.")
            break

def machineGuess():

    print(f"\n\tChoose a number from 1 to {MAX_RANGE}.")
    print("Hints:\n " \
    "\ts(S)- when number is smaller\n "
    "\tb(B)- when number is  bigger\n " 
    "\tf(F)- when number is found\n")  

    attempts, minValue, maxValue = 0, 1, MAX_RANGE

    while 1:
        ans = (minValue + maxValue) // 2

        attempts += 1

        print(f"Machine guess number is: {ans}")
        playerInput = input("Enter indicates: ").casefold()

        if playerInput == 's':
            maxValue = ans

        elif playerInput == 'b':
            minValue = ans

        elif playerInput == 'f':
            print(f"Fine! Your number is: {ans}. Total attempts: {attempts}")
            break
        else:
            print("Incorrect input please read hints\n")
            attempts -= 1
        

while 1:
    print("\n\tGUESS NUMBER.")
    print("\t1.Player Guess.")
    print("\t2.Machine Guess.")
    print("\t3.Exit")   
    playerChoose = input("\nWhat do you want to play? Choose (1-3):")

    if playerChoose == '1':
        playerGuess()

    elif playerChoose == '2':
        machineGuess()
    elif playerChoose == '3':
        print("Goodbye!")
        break
    else:
        print("Incorrect input")
        continue

    playAgain = input("Do you want to play again? [y/n]: ").casefold()
    if playAgain == 'y':
        continue
    else:
        print("Goodbye!")
        break


