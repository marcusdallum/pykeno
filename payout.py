import cfg

def pick1():
    if cfg.matches == 1:
        cfg.winnings = cfg.bet*100+cfg.startamount
        print("winner")
        cfg.result = True
    else:
        cfg.result = False
        print("loser")


def pick8():
    n = 8
    if n == 1:
        print("you got one match you are not a winner")
    elif n == 2:
        print("you got 2 matchs you are not a winner")
    elif n == 3:
        print("you got 2 matchs you are not a winner")
    elif n == 4:
        cfg.startamount = cfg.bet+cfg.startamount
        cfg.result = True
    elif n == 5:
        cfg.startamount = cfg.bet*4+cfg.startamount
        print("you got 5 matchs Winner!")
        cfg.result = True
    elif n == 6:
        cfg.startamount = cfg.bet*40+cfg.startamount
        print("you got 6 matchs Winner!")
        cfg.result = True
    elif n == 7:
        cfg.startamount = cfg.bet*400+cfg.startamount
        print("you got 7 matchs Winner!")
        cfg.result = True
    elif n == 8:
        cfg.startamount = cfg.bet*20000+cfg.startamount
        cfg.result = True
        print("you got 8 matchs Winner!")
    else:
        startamount = bet+startamount
        print("you got 0 matchs Winner!")