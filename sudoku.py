# Casos test
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

def es_cuadrada(sudoku):

    assert isinstance(sudoku, list), "sudoku debe ser una lista"

    numero_filas = len(sudoku)       
                      
    for fila in range(numero_filas):                  
        if len(sudoku[fila]) != numero_filas:          
            return False                               
    return True                                        

def son_enteros(sudoku):
    for fila in sudoku:
        for num_columna in fila:
            if type(num_columna) != int:
                return False
        return True                                              


def fila_correcta(sudoku):
    pass                                               


def columna_correcta(sudoku):
    pass                                               


def check_sudoku(sudoku):
    pass                                               

if __name__ == "__main__":
    # casos test check sudoku

    print(check_sudoku(incorrecto1))   # >>> False
    print(check_sudoku(correcto))      # >>> True
    print(check_sudoku(incorrecto2))   # >>> False
    print(check_sudoku(incorrecto3))   # >>> False
    print(check_sudoku(incorrecto4))   # >>> False
    print(check_sudoku(incorrecto5))   # >>> False
    print(check_sudoku(incorrecto6))   # >>> False

    # casos test es_cuadrada

    print(es_cuadrada(incorrecto1))   # >>> True
    print(es_cuadrada(correcto))      # >>> True
    print(es_cuadrada(incorrecto2))   # >>> True
    print(es_cuadrada(incorrecto3))   # >>> True
    print(es_cuadrada(incorrecto4))   # >>> True
    print(es_cuadrada(incorrecto5))   # >>> True
    print(es_cuadrada(incorrecto6))   # >>> False

    # casos test son_entero
    print("-------------------")
    print(son_enteros(incorrecto1))   # >>> True
    print(son_enteros(correcto))      # >>> True
    print(son_enteros(incorrecto2))   # >>> True
    print(son_enteros(incorrecto3))   # >>> True
    print(son_enteros(incorrecto4))   # >>> False
    print(son_enteros(incorrecto5))   # >>> False
    print(son_enteros(incorrecto6))   # >>> True