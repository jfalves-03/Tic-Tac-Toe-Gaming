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
    print(f"Round: {r}")

def cpu(matriz: list) -> None:
    cont = 0
    playCpu_cell = randrange(0, len(matriz))
    playCpu_c = randrange(0, len(matriz[playCpu_cell])) 
    while True:
        if matriz[playCpu_cell][playCpu_c] == '': 
            matriz[playCpu_cell][playCpu_c] = 'X' 
            break
        else: 
            playCpu_cell = randrange(0, len(matriz))
            playCpu_c = randrange(0, len(matriz[playCpu_cell])) 
            cont += 1 
        if cont > 10: 
            break
    return True
    

def player(matriz: list) -> None: 
    line = int(input('Line: ')) 
    column = int(input('Column: ')) 
    while True:
        if matriz[line][column] == '':
            matriz[line][column] = 'O' 
            break
        else: 
            return False 
    return True

def end(matriz: list) -> bool: 
    cont = 0
    for cell in matriz: 
        for c in cell:
            if c != '': 
                cont += 1
    if cont == 9: 
        return True 
    return False
