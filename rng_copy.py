import random
import time
import payout
import cfg
x = True
startamount = 100
u = True
pick = []
bet = 1
spot = None
match = []
name =[]
readrules = "n"
drum =[]
match = []
winnings = 0

def spots():
      x = True
      global spot
      while x == True:
            while True:
                  try:
                        cfg.spot = int(input("How many spots would you like to pick? 1 - 8"))
                        break
                  except Exception:
                        print("that is not a valid option Please Choose a between 1 and 8 spots")
            if int(cfg.spot) < 9:
                  x = False
            else:
                   print("that is not a valid option Please Choose a between 1 and 8 spots")


def bets():
      global startamount
      global bet
      x = True
      y = True
      print("your starting amount is "+str(startamount)+" credits")
      while x == True:
            while True:
                  try:
                        bet = int(input("How much would you like to bet?"))
                        break
                  except Exception:
                        print("please enter a whole number")
                  
            if int(bet) > startamount:
                  print("you dont have that much money")
            else:
                  x = False
def game():
      print("playing the game")

def rules():
      marker = True
      while marker == True:
            print("these are the rules")
            x = input("Do you want to read them again? y/n ")
            if x  != "y":
                  marker = False
            
def readrule():
      global readrules
      readrules = input("Hello "+name+" Good Luck, would you like to know the rules? y/n")
      
def welcome():
      global name
      global readrules
      print("Wlecome to Keno")
      name = input("What is your name?")
      readrule()
      if readrules == "y":
             rules()
      elif readrules =="n":
            print("Lets Play!")
      else:
            readrule()


def numbers():
      global spot
      global pick
      amount = list(range(spot))
      for x in amount:
            x = True
            while x == True:
                  while True:
                        try:
                              pick1 = int(input("Pick a Number 1 - 80?"))
                              break
                        except Exception:
                              print("please enter a whole number")
                        
                  if int(pick1) > 81 or int(pick1) < 0:
                        print("Pick a number 1 - 80")
                  else:
                        x = False
                        pick.append(pick1)

def drumroll():
    global drum
    drum = random.sample((range(1,80)), k=20)

def matches():
    global drum
    global pick
    global match
    for z in drum:
        for x in range(1):
            print(z)
        for y in pick:
            if y == z:
                match.append(y)

if __name__ == "__main__":
    #welcome()
    #bets()
    spots()
    print(cfg.spot)
    #numbers()i
    #drumroll()
    #matches()
    #payout.pick1(100,2,1,False,winnings)
    #print(winnings)
    #game()

