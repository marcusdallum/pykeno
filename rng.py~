import random
import time
x = True
startamount = 100
u = True
picks = []
bet = 1
number = 8
match = []

def pick7(n):
      global bet
      global startamount
      if n == 1:
            print("you got one match you are not a winner")
      elif n == 2:
            print("you got 2 matchs you are not a winner")
      elif n == 3:
            print("you got 2 matchs you are not a winner")
      elif n == 4:
            startamount = bet+bet+startamount
            print("you got 4 matchs Winner!")
      elif n == 5:
            startamount = bet*10+startamount
            print("you got 5 matchs Winner!")
      elif n == 6:
            startamount = bet*100+startamount
            print("you got 6 matchs Winner!")
      elif n == 7:
            startamount = bet*4000+startamount
            print("you got 7 matchs Winner!")
      else:
            startamount = bet+startamount
            print("you got 0 matchs Winner!")


def pick8(n):
      global bet
      global startamount
      if n == 1:
            print("you got one match you are not a winner")
      elif n == 2:
            print("you got 2 matchs you are not a winner")
      elif n == 3:
            print("you got 2 matchs you are not a winner")
      elif n == 4:
            startamount = bet+startamount
            print("you got 4 matchs Winner!")
      elif n == 5:
            startamount = bet*4+startamount
            print("you got 5 matchs Winner!")
      elif n == 6:
            startamount = bet*40+startamount
            print("you got 6 matchs Winner!")
      elif n == 7:
            startamount = bet*400+startamount
            print("you got 7 matchs Winner!")
      elif n == 8:
            startamount = bet*20000+startamount
            print("you got 8 matchs Winner!")
      else:
            startamount = bet+startamount
            print("you got 0 matchs Winner!")

def drumroll(matches,pik):
      drum = random.sample((range(1,80)), k=20)
      num = 1
      for z in drum:
            for x in range(num):
                  #print("-")
                  #time.sleep(0.2)
                  #print("|")
                  print(z)
            for y in pik:
                  if y == z:
                        print("its a match!!")
                        matches.append(y)

def theend():

def betting():

      global u
      global x
      global startamount
      global match
      global bet
      match.clear()
      l = input("Do you want to continue? y/n")
      if l == "y":
            x=True
            if startamount < 1:
                  x=False
                  print("you are out of money, please play again")
            else:
                  x=True
                  print(startamount)
                  p = input('keep the same bet? y/n')
                  if p == "y":
                        startamount = startamount - bet
                        u = False
                  else:
                        u = True            
      else:
            x=False

name = input("Welcome to Keno!! What is your name?")
print('Hello' + name)
print("Good Luck!")
print('To start the game you have ' + str(startamount))
while x==True:
      while u == True:
            #print("you have " + str(startamount))
            bet = int(input("how much do you want to bet"))
            startamount = startamount-bet
            print(startamount)
            number = int(input("Chose a number 1 thru 8"))
            amount = list(range(number))
            for x in amount:
                  pick = input("chose your number")
                  picks.append(int(pick))
            drumroll(match,picks)
            m = len(match)
            pick8(m)
            theend()
      else:
            drumroll(match,picks)
            m = len(match)
            pick8(m)
            theend()

else:
      print("goodbye!")
      