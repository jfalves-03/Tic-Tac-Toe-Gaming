'''TIC TAC TOE GAME''' 
from random import * 
from menu import *
from os import * 
from time import sleep



matriz = [["", "", ""], 
          ["", "", ""], 
          ["", "", ""]] 

round = 1

while True: 
    system('cls') 
    menu(matriz, round) 
    fim = end(matriz) 
    if fim:
        break
    sit_player = player(matriz) 
    if sit_player is True: 
        sit_cpu = cpu(matriz) 
        round += 1 
    else: 
        continue
    sleep(1) 

