import random
import time
import payout
import cfg
x = True
#startamount = 100
u = True
#pick = []
#bet = 1
#spot = None
#match = []
#name =[]
readrules = "n"
#drum =[]
#match = []
#winnings = 0

def spots():
    x = True
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
    x = True
    y = True
    print("your starting amount is "+str(cfg.startamount)+" credits")
    while x == True:
        while True:
            try:
                cfg.bet = int(input("How much would you like to bet?"))
                break
            except Exception:
                print("please enter a whole number")
                  
        if int(cfg.bet) > cfg.startamount:
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
    readrules = input("Hello "+cfg.name+" Good Luck, would you like to know the rules? y/n")
      
def welcome():
    global readrules
    print("Wlecome to Keno")
    cfg.name = str(input("What is your name?"))
    readrule()
    if readrules == "y":
        rules()
    elif readrules =="n":
        print("Lets Play!")
    else:
        readrule()


def numbers():
    amount = list(range(cfg.spot))
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
                cfg.pick.append(pick1)

def drumroll():
    cfg.drum = random.sample((range(1,80)), k=20)

def matches():
    for z in cfg.drum:
        for x in range(1):
            print(z)
        for y in cfg.pick:
            if y == z:
                cfg.match.append(y)

def picks():
    if cfg.spot == 1:
        payout.pick1
    elif cfg.spot == 2:
        payout.pick2
    elif cfg.spot == 3:
        payout.pick3
    elif cfg.spot == 4:
        payout.pick4
    elif cfg.spot == 5:
        payout.pick5
    elif cfg.spot == 6:
        payout.pick6
    elif cfg.spot == 7:
        payout.pick7
    elif cfg.spot == 8:
        payout.pick8


            
def maingame():
    picks()
    cfg.startamount = cfg.startamount-cfg.bet
    print(cfg.winnings)
    if cfg.result == True:
        print("you are a winner")
        print("Credits = " +str(cfg.startamount))
    else:
        print("you are a loser")
        print("Credits = " +str(cfg.startamount))
    

def Playagain():
    drumroll()
    matches()
    maingame()
    
    
    
        
    



if __name__ == "__main__":
    welcome()
    firsttime = True
    playagain = True
    while firsttime == True:
        bets()
        spots()
        numbers()
        drumroll()
        matches()
        maingame()
        firsttime = False
    while playagain == True:
        m = input("would you like to play again? y/n")
        if m == "y":
            Playagain()
        else:
            playagain = False
    
    
    
    # game()