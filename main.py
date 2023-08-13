import random
import os
import re
import termcolor
import time
from func import roll, got_let_int, get_int_ship
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
    user_input=input("Menu:\n1. Case menu\n2. Collection\n3. Fight\n4. Exit\n>>> ")
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
        clear()
        enemy_rand = random.randint(1,3)
        enemy_list = []
        for en_i in range(enemy_rand):
            roll_en = roll()
            enemy_list.append(roll_en)
        print("Your enemies:")
        for en_i1 in range(enemy_rand):
            print(str(en_i1+1)+". "+enemy_list[en_i1-1])
            time.sleep(0.8)
        while len(enemy_list) != 0:
            print("Choose your ship to attack:")
            for i_non in range(len(ship_list)):
                print(str(i_non+1)+") "+ship_list[i_non])
            user_input = int(input(">>> "))
            player_cost = 0
            enemy_cost = 0
            if user_input <= len(ship_list) and user_input > 0:
                player_ship = ship_list[user_input-1]
                ship_list.pop(user_input-1)
                player_letter, player_int = player_ship.split("-")
                player_cost = (got_let_int(player_letter)*int(player_int))//1000

                enemy_ship = enemy_list[0]
                enemy_letter, enemy_int = enemy_ship.split("-")
                enemy_cost = (got_let_int(enemy_letter)*int(enemy_int))//1000
            elif user_input == "exit":
                print("You left the battlefield")
                input_enter = input("Press ENTER to continue... ")
            else:
                print("You do not have ship with choosed number.")
                input_enter = input("Press ENTER to continue... ")
            if player_cost != 0 and enemy_cost != 0:
                if player_cost > enemy_cost:
                    print("You won and got: "+str(enemy_cost//2)+"$!")
                    damage = random.randint(0, 30)
                    time_player_int = int(player_int)
                    fin_player_int = time_player_int - damage
                    player_int = get_int_ship(fin_player_int)
                    new_ship = str(player_letter)+str(player_int)
                    ship_list.append(new_ship)
                    print("Your ship has taken "+str(damage)+" damage. Now it is "+str(new_ship)+".")
                    money += enemy_cost//2
                    enemy_list.pop(0)
                    save()
                    input_enter = input("Press ENTER to continue... ")
                    
                else:   
                    print("You've lost your ship! Be careful next time!)")
                    save()
                    input_enter = input("Press ENTER to continue... ")
    if user_input == "4":
        break
    else:
        clear()
                
