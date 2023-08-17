import random

def got_let_int(ggg):
    letters = {
        "*": 100,
        "A": 26,
        "B": 25,
        "C": 24,
        "D": 23,
        "E": 22,
        "F": 21,
        "G": 20,
        "H": 19,
        "I": 18,
        "J": 17,
        "K": 16,
        "L": 15,
        "M": 14,
        "N": 13,
        "O": 12,
        "P": 11,
        "Q": 10,
        "R": 9,
        "S": 8,
        "T": 7,
        "U": 6,
        "V": 5,
        "W": 4,
        "X": 3,
        "Y": 2,
        "Z": 1
    }
    return letters.get(ggg, 0)
def roll():
    #li = input()
    #fi += 1
    ran = random.randint(1,351)


    if ran == 1:
        ship_let = "A"
    elif ran <=3:
        ship_let = "B"
    elif ran <=6:
        ship_let = "C"
    elif ran <=10:
        ship_let = "D"
    elif ran <=15:
        ship_let = "E"
    elif ran <=21:
        ship_let = "F"
    elif ran <=28:
        ship_let = "G"
    elif ran <=36:
        ship_let = "H"
    elif ran <=45:
        ship_let = "I"
    elif ran <=55:
        ship_let = "J"
    elif ran <=66:
        ship_let = "K"
    elif ran <=78:
        ship_let = "L"
    elif ran <=91:
        ship_let = "M"
    elif ran <=105:
        ship_let = "N"
    elif ran <=120:
        ship_let = "O"
    elif ran <=136:
        ship_let = "P"
    elif ran <=153:
        ship_let = "Q"
    elif ran <=171:
        ship_let = "R"
    elif ran <=190:
        ship_let = "S"
    elif ran <=210:
        ship_let = "T"
    elif ran <=231:
        ship_let = "U"
    elif ran <=253:
        ship_let = "V"
    elif ran <=276:
        ship_let = "W"
    elif ran <=300:
        ship_let = "X"
    elif ran <=325:
        ship_let = "Y"
    elif ran <=351:
        ship_let = "Z"
    ran = random.randint(0, 9999)
    if ran/10 >= 1:
        if ran/100 >= 1:
            if ran/1000 >= 1:
                niki = ship_let+"-"+str(ran)
            elif ran/1000 < 1:
                niki = ship_let+"-0"+str(ran)
        elif ran/100 < 1:
            niki = ship_let+"-00"+str(ran)
    elif ran/10 < 1:
        niki = ship_let+"-000"+str(ran)
    return niki
def get_int_ship(self_int):
    if int(self_int)/10 >= 1:
        if int(self_int)/100 >= 1:
            if int(self_int)/1000 >= 1:
                niki = "-"+str(self_int)
            elif int(self_int)/1000 < 1:
                niki = "-0"+str(self_int)
        elif int(self_int)/100 < 1:
            niki = "-00"+str(self_int)
    elif int(self_int)/10 < 1:
        niki = "-000"+str(self_int)
    return niki
def get_d_sym(a):
    if a <= 20:
        total = "$"
    elif a <= 70:
        total = "$|$"
    elif a <= 120:
        total = "$|$|$"
    elif a <= 200:
        total = "$|$|$|$"
    else:
        total = "$|$|$|$|$"
    return total
def get_cost(a):
    s_let, s_int = a.split("-")
    cost = (got_let_int(s_let)*int(s_int))//1000
    return cost
