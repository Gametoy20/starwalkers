import random
import os
import re
import termcolor
from func import roll, got_let_int
from termcolor import colored, cprint
print(colored("WELCOME TO STARWALKERS!", "red", attrs=["bold"]))


let_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
summ_w = len(let_list)
summ_all = int()
a = int()
for i in range(summ_w):
    b = let_list[i]
    a = i+1
    summ_all += a
    #print(b, summ_all)
ran = int()
fi = -1
#print(summ_all)
#priti = str()
#infi = 0
#while priti != "A-9999":
#    priti = roll()
#    infi += 1
#print(infi)
#zina = input()
clear = lambda: os.system('cls')
money = 100
user_case = 0
ship_list = []
name = str(input("Enter your name: "))
name_txt = name+".txt"
try:
    filename = open(name_txt, "r")
    file_cont = filename.readlines()
    lines = len(filename.readlines())
    money = int(re.sub(r"[\n]", "", file_cont[0]))
    user_case = int(re.sub(r"[\n]", "", file_cont[1]))
    for j in range(len(file_cont)-2):
        ship_list.append(re.sub(r"[\n]", "", file_cont[j+2]))
    filename.close()
    #print("Lines:", lines)
except FileNotFoundError:
    filename = open(name_txt, "w")
    filename.write("100\n")
    filename.write("0")
    filename.close()
    print("Registered:", name)
def save():
    filename = open(name_txt, "w")
    filename.write(str(money)+"\n")
    filename.write(str(user_case))
    for k in range(len(ship_list)):
        filename.write("\n"+ship_list[k-1])
    filename.close()
clear()
while True:
    print("You have " + str(money)+"$ and "+str(user_case)+" cases.")
    user_input=input("Menu:\n1. Case menu\n2. Collection\n3. Exit\n>>> ")
    if user_input == "1":
        clear()
        user_input2 = input("What do you want to do with cases?\n1. Buy\n2. Open\n3. Close\n>>> ")
        if user_input2 == "1":
            clear()
            user_input3 = int(input("How much?"))
            if money >= 10*user_input3:
                money -= 10*user_input3
                user_case += user_input3
                clear()
                print("Thanks for buying", user_input3, "cases.")
                save()
                input_enter = input("Press ENTER to continue... ")
            else:
                print("Not enough money, bro.")
                input_enter = input("Press ENTER to continue... ")
        if user_input2 == "2":
            if user_case >= 1:
                user_case -= 1
                gotter = roll()
                ship_list.append(gotter)
                #print(ship_list)
                clear()
                gotter_letter, gotter_int = gotter.split("-")
                cost = (got_let_int(gotter_letter)*int(gotter_int))//1000
                print("You got:", gotter+"! It costs:", cost)
                save()
                input_enter = input("Press ENTER to continue... ")
    if user_input == "2":
        clear()
        coli = ""
        for ii in range(len(ship_list)):
            if ii == len(ship_list)-1:
                coli += ship_list[ii-1] + "."
            else:
                coli += ship_list[ii-1] + ", "
        print("Your collection of ships:", coli)
        input_enter = input("Press ENTER to continue... ")
    if user_input == "3":
        break
    else:
        clear()
                
