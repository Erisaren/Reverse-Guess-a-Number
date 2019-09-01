#  Variables.
import math

x = 50  # Computer's guess
i = 0  # Interval's half
turn = 0  # Turns to complete
Ia = 0  # Starting interval
Ib = 100  # Ending interval

print("Guess a number between 1 and 100 and keep it in your head.")
print(f"Your number is {x}...")
c = input("Press H if your number is higher, press L if it is lower, press Y if it is the correct number: ")

while True:
    turn = turn + 1

    if c == "Y" or c == "y":
        print(f"Ah, I finally guessed it! {x} that is it. It took me {turn} turns.")
        print("Thank you for playing.")
        break

    elif c == "H" or c == "h":  # Interval [x - 100]
        Ia = x  # Computer guessed
        i = ((Ib - Ia) / 2)
        i = math.ceil(i)
        x = x + i  # Adding interval's half to computer guessed
        print(f"Your number is {x}...")
        c = input("Press H if your number is higher, press L if it is lower, press Y if it is the correct number: ")

    elif c == "L" or c == "l":  # Interval [0 - x]
        Ib = x  # Computer guessed
        i = ((Ib - Ia) / 2)
        i = math.ceil(i)
        x = x - i  # Adding interval's half to computer guessed
        print(f"Your number is {x}...")
        if x > 0:
            c = input("Press H if your number is higher, press L if it is lower, press Y if it is the correct number: ")
        else:
            print("I am supposed to guess between 1 and 100.")
            break
