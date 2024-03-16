# def main():
#     choice = input("What will you do? Fight or Flee?")
#     if input == ("Fight"):
#         print("You begin the ")

#RNG generator for npc 
import random

npc_power = random.randint(0, 10)

#delay timer
import time

def delay():
    time.sleep(1)

#realistic type
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

#Welcome message
print_slow("Welcome to Adventure Text! Let's see if you can survive. \n")
delay()

#Ask for user's name and properly format
name = input("Before we begin, what is your name?\n").title().strip()
delay()
print_slow(f"Hello, {name}! I'm rooting for you!\n")

#Adventure starts
print_slow("Off we go!\n")
delay()

# Encounter 1 - The Road
print_slow("As you set off, you come across a split road.\n")
delay()
en1 = input("Do you go Left or Right? \n").title()
if en1 == "Left":
    print_slow("Uh oh, you fell into a deep hole! Game Over.\n")
elif en1 == "Right":
    print_slow("You walk for a few miles and find a worn out bridge\n")

# Encounter 2 - The Bridge
    en2 = input("Do you Run or Walk across it? \n").title()

    if en2 == "Run":
        print_slow("The Bridge is unstable! It snapped in the middle and you fell to your death! Game Over.\n")
    elif en2 == "Walk":
        print_slow("You cautiously walked across and made it safely to the other side.\n")
    else:
        print_slow("Invalid Option! You spontaniously combusted. Game Over.\n")
else:
    print_slow("Invalid Option! You spontaniously combusted. Game Over.\n")




# Encounter 3 - The Bear

# Encounter 4 - The Boat

# Encounter 5 - The Island

# Encounter 6 - The Cave

# Encounter 7 - The Hidden Passage

# Congratulations! You Survived!
