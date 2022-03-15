'''TIC TAC TOE GAME''' 
from random import * 
from menu import *
from os import * 
from time import sleep


matriz = [["", "", ""], 
          ["", "", ""], 
          ["", "", ""]] 

team = ['X', 'O'] 

system('cls')
print('''0 -> X 
1 -> O''')
choose = int(input('Choose your team: ')) 
person = team.pop(choose) 
pc = team[0] 

round = 1

while True: 
    system('cls') 
    # =========show the menu=========
    menu(matriz, round) 
    # =============================== 

    # ===========check if it´s the end of the game==============
    if any([check_lines(matriz, [person, pc]), check_columns(matriz, [person, pc]), check_diagonal_l(matriz, [person, pc]), check_diagonal_r(matriz, [person, pc])]) or end(matriz): 
        print('-'*24)
        break
    # =========================================================== 

    # =========input of the game========  
    try:
        sit_player = player(matriz, [person, pc]) 
        if sit_player is True: 
            cpu(matriz, [person, pc]) 
            round += 1 
        else: 
            continue 
    except: 
        continue
    # ================================== 
    sleep(1) 

