import cfg

def pick1():
      if cfg.matches == 1:
            cfg.winnings = cfg.bet*100+cfg.startamount
            print("winner")
            result = True
      else:
            result = False
            print("loser")


def pick8(n):
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
     
