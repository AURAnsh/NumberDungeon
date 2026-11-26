import random
import time

randnum = random.randint(1,100)
low = 1
high = 100
guessed = False

print("You walk into the slimy dungeon, preparing to fight off hordes of monsters.")
time.sleep(2)
print("However, to your surprise, you only see a single knight, holding the key to the door ahead.")
time.sleep(2)
print("With a snap, the door behind you shuts.")
time.sleep(2)
print('"I have chosen a number been one and a hundred. Guess it right within seven guesses and you may proceed", says the knight.')
time.sleep(2)
print('"That’s impossible!", you blurt out, confused as to how the number can be guessed within only seven guesses.')
time.sleep(2)
print("That's where you're wrong. After each guess, I'll tell you whether your guess is higher or lower than my number.")
time.sleep(2)
print("Are you ready to guess?")
print("")


time.sleep(2.5)

for i in range(7):
  guess = int(input("My guess is... "))
  time.sleep(0.5)
  if guess == randnum:
    if i == 0:
      print("Congratulations! You successfully guessed my number in just one try!")
      time.sleep(2)
      print("Seems oddly suspicious though...")
    else:
      print("Congratulations! You successfully guessed my number in " + str(i+1) + " tries!")
    guessed = True
    break
  else:
    if guess > randnum:
      print("Too high!")
      if guess < high:
        high = guess - 1
    elif guess < randnum:
      print("Too low!")
      if guess > low:
        low = guess + 1

    time.sleep(1)
    print("My number is between " + str(low) + " and " + str(high) + "!")
    if i == 6:
      print("You're out of guesses!")
    elif i == 5:
      print("Last guess!")
    else:
      print("Only " + str(6-i) + " guesses left!")
    print("")

time.sleep(2)

if guessed:
  print("The knight hands you the key to the door behind him and steps aside.")
  time.sleep(2)
  print("Little did you know, you still have a long way to go...")
else:
  print("The knight looks back at you.")
  time.sleep(1)
  print("You can't see his face, but you can tell he is ashamed.")
  time.sleep(2)
  print("The door behind you opens gradually and you step out, defeated by a simple number puzzle. Good job!")

time.sleep(1)
print("———END—OF—STORY———")
