#build your hand as close to the number 21 as possible face cards are 10, ace is 11, or 1 if you are close to 21. Type "end" in the bet input to end the program
import random
import sys

totalEarnings = 0

while True: 
  
  bet = input("how much would you like to bet? ")
  if bet == "end":
    break 
  else:
    bet = int(bet)

  yourHand = random.randint(1,11) + random.randint(1,11)
  opponentHand = random.randint(1,11) + random.randint(1,11)
  
  if yourHand == 22:
    yourHand = 12

  if opponentHand == 22:
    opponentHand = 12

  def hideSet():
    #sys.stdout.write('\x1b[1A') moves the cursor up 1 in the console, sys.stdout.write('\x1b[2K') deletes that line
    
    for lines in range(7):
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')

  def showCards():
    hideSet()
    print("total:", totalEarnings, "\nbet:", bet,"\nyour hand:", yourHand,"\nyour opponents hand:", opponentHand)

  while opponentHand < 21 and yourHand < 21:
    
    showCards()
    yourMove = input("hit, stand, or doubledown? ")
    
    if opponentHand <= 16:
      opponentHand += random.randint(1,11)

    if yourMove == "hit":
      yourHand += random.randint(1,11)
    elif yourMove == "doubledown":
      yourHand += random.randint(1,11)
      bet = bet*2
    elif opponentHand > 16:
      break
  
  showCards()
  
  if (yourHand > 21 and opponentHand > 21) or (yourHand == 21 and opponentHand == 21):
    print("draw")
    print("total:",totalEarnings)
  elif (yourHand == 21) or (opponentHand > 21 and yourHand <=21):
    print("you win!")
    totalEarnings += bet
    print("total:",totalEarnings)
  elif (yourHand < 21 and opponentHand < 21):
    if opponentHand > yourHand: 
      print("you lose!")
      totalEarnings -= bet
      print("total:",totalEarnings)
    elif opponentHand == yourHand:
      print("draw")
      print("total:",totalEarnings)
    else:
      print("you win!")
      totalEarnings += bet
      print("total:",totalEarnings)
  else:
    print("you lose!")
    totalEarnings -= bet
    print("total:",totalEarnings)
  


print("\nsession ended\ngrand total:",totalEarnings)
if totalEarnings < 0:
  print("\nF")
