from random import * 

def menu(container: list, r: int) -> None:  
    cont = 0
    print('----TIC TAC TOE GAME----') 
    print("   0  1  2")
    for cell in container: 
        print(f'{str(cont)}: ' , end='')
        for c in cell:
            print(c + ' | ', end='') 
        print('\n-----------')
        cont += 1 
    print(f"Jogadas: {r}")

def cpu(matriz: list) -> None:
    playCpu_cell = randrange(0, len(matriz))
    playCpu_c = randrange(0, len(matriz[playCpu_cell])) 
    while True:
        if matriz[playCpu_cell][playCpu_c] != 'X': 
            matriz[playCpu_cell][playCpu_c] = 'X' 
            return True
        else: 
            playCpu_cell = randrange(0, len(matriz))
            playCpu_c = randrange(0, len(matriz[playCpu_cell]))
    

def player(matriz: list) -> None: 
    line = int(input('Line: ')) 
    column = int(input('Column: ')) 
    while True:
        if matriz[line][column] != 'X':
            matriz[line][column] = 'O' 
            return True
        else: 
            line = int(input('Line: ')) 
            column = int(input('Column: ')) 

def end(matriz: list) -> bool: 
    for cell in matriz: 
        if all(cell) != '': 
            return True 
    return False
