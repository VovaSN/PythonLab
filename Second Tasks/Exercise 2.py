import random

MAX_RANGE = 9999

def confirmExit():
    while True:
        confirmInput = input("Are you sure you want to quit? [y/n]: ").casefold()
        if confirmInput == 'y':
            print("Goodbye!")
            return True
        elif confirmInput == 'n':
            return False
        print("Please enter 'y' for yes or 'n' for no.")
    
def playerGuess():
    guessNumber = random.randint(1,MAX_RANGE)
    attempts = 0
    while True:
        ans = int(input(f"\nEnter integer number (1-{MAX_RANGE}): "))

        if ans == 0:
            if confirmExit():
                return
            continue

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
    "\ts(or <)- when number is smaller\n "
    "\tb(or >)- when number is  bigger\n " 
    "\tf(or =)- when number is found\n")  

    attempts, minValue, maxValue = 0, 1, MAX_RANGE

    while minValue <= maxValue:
        ans = (minValue + maxValue) // 2

        attempts += 1

        print(f"Machine guess number is: {ans}")
        playerInput = input("Enter indicates: ").casefold()

        if playerInput == '0':
            if confirmExit():
                return
            attempts -= 1
            continue

        if playerInput == 's' or playerInput == '<':
            if ans == minValue:
                print(f"[!] Cheating! You previously said the number was greater than {minValue-1}. It cannot be less than {ans}!")
            maxValue = ans - 1

        elif playerInput == 'b' or playerInput == '>':
            if ans == maxValue:
                print(f"[!] Cheating! You previously said the number was less than {maxValue+1}. It cannot be greater than {ans}!")
            minValue = ans + 1

        elif playerInput == 'f' or playerInput == '=':
            print(f"Fine! Your number is: {ans}. Total attempts: {attempts}")
            break
        else:
            print("Incorrect input please read hints\n")
            attempts -= 1
        
while True:
    print("\n\tGUESS NUMBER.")
    print("\t1.Player Guess.")
    print("\t2.Machine Guess.")
    print("\t3.Exit")   
    playerChoose = input("\nWhat do you want to play? Choose (1-3):")

    if playerChoose == '1':
        playerGuess()

    elif playerChoose == '2':
        machineGuess()
    elif playerChoose == '3' or playerChoose == '0':
        if confirmExit():
          break  
        continue
    else:
        print("Incorrect input")
        continue

    playAgain = input("Do you want to play again? [y/n]: ").casefold()
    if playAgain == 'y':
        continue
    else:
        print("Goodbye!")
        break