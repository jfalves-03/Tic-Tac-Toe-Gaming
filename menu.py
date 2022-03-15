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

def cpu(matriz: list, team: list) -> bool:
    cont = 0
    playCpu_cell = randrange(0, len(matriz))
    playCpu_c = randrange(0, len(matriz[playCpu_cell])) 
    while True:
        if matriz[playCpu_cell][playCpu_c] == '': 
            matriz[playCpu_cell][playCpu_c] = team[1] 
            break
        else: 
            playCpu_cell = randrange(0, len(matriz))
            playCpu_c = randrange(0, len(matriz[playCpu_cell])) 
            cont += 1 
        if cont > 10: 
            break 
    

def player(matriz: list, team: list) -> bool: 
    line = int(input('Line: ')) 
    column = int(input('Column: ')) 
    while True:
        if matriz[line][column] == '':
            matriz[line][column] = team[0] 
            break
        else: 
            return False 
    return True 

def check_lines(matriz: list, team: list) -> bool: 
    line_o = [] 
    line_x = [] 
    for cell in matriz: 
        line_o = [o for o in cell if o == 'O'] 
        line_x = [x for x in cell if x == 'X'] 
        if len(line_o) == 3 and len(line_x) == 0: 
            if team[0] == line_o[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_o[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
        if len(line_x) == 3 and len(line_o) == 0: 
            if team[0] == line_x[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_x[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True
    return False 

def check_columns(matriz: list, team: list) -> bool:
    for c in range(3): 
        line_o = [] 
        line_x = []
        for cell in range(3): 
            if matriz[cell][c] == 'O': 
                line_o.append(matriz[cell][c]) 
            if matriz[cell][c] == 'X':
                line_x.append(matriz[cell][c]) 
        if len(line_o) == 3 and len(line_x) == 0: 
            if team[0] == line_o[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_o[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
        if len(line_x) == 3 and len(line_o) == 0: 
            if team[0] == line_x[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_x[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 

def check_diagonal_r(matriz: list, team: list) -> bool: 
    line_o = [] 
    line_x = [] 
    for i in range(3): 
        if matriz[i][i] == 'O': 
            line_o.append(matriz[i][i]) 
        if matriz[i][i] == 'X':
            line_x.append(matriz[i][i]) 
    if len(line_o) == 3 and len(line_x) == 0: 
            if team[0] == line_o[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_o[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
    if len(line_x) == 3 and len(line_o) == 0: 
            if team[0] == line_x[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_x[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
    return False 

def check_diagonal_l(matriz: list, team: list) -> bool: 
    line_o = [] 
    line_x = [] 
    cont = 0
    for i in range(2, -1, -1): 
        if matriz[i][cont] == 'O': 
            line_o.append(matriz[i][cont]) 
        if matriz[i][cont] == 'X':
            line_x.append(matriz[i][cont]) 
        cont += 1
    if len(line_o) == 3 and len(line_x) == 0: 
            if team[0] == line_o[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_o[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
    if len(line_x) == 3 and len(line_o) == 0: 
            if team[0] == line_x[0]: 
                print('THE PLAYER HAS GAINED!')
            if team[1] == line_x[0]: 
                print('THE COMPUTER HAS GAINED!')
            return True 
    return False

def end(matriz: list) -> bool: 
    cont = 0
    for cell in matriz: 
        for c in cell:
            if c != '': 
                cont += 1
    if cont == 9: 
        return True 
    return False
