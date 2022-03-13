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
    sit_cpu = cpu(matriz)
    sit_player = player(matriz) 
    if sit_cpu is True:
        round += 1 
        system('cls') 
        menu(matriz, round)
    if sit_player is True: 
        round += 1 
        menu(matriz, round)
    fim = end(matriz) 
    if fim: 
        break
    sleep(1) 

