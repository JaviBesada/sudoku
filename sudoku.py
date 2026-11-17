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

incorrecto3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]

incorrecto4 = [["a", "b", "c"], 
               ["b", "c", "a"], 
               ["c", "a", "b"]]

incorrecto5 = [[1, 1.5], 
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0], 
               [0, 1, 0], 
               [0, 0, 0, 1]]


def es_cuadrada(sudoku):
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
    for fila in sudoku:
        if len(fila) != len(set(fila)):
            return False
    return True


def columna_correcta(sudoku):
    for i in range(len(sudoku)):
        numeros_vistos = []
        for fila in sudoku:
            numero = fila[i]
            if numero in numeros_vistos:
                return False
            numeros_vistos.append(numero)
    return True


def rango_correcto(sudoku):
    for fila in sudoku:                                
        for numero_buscado in range(1, len(sudoku) + 1):   
            if numero_buscado not in fila:             
                return False
    return True                                       


def check_sudoku(sudoku):
    if (
        es_cuadrada(sudoku)
        and son_enteros(sudoku)
        and fila_correcta(sudoku)
        and columna_correcta(sudoku)
        and rango_correcto(sudoku)
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    # casos test check sudoku
    print("CHECK SUDOKU")
    print(check_sudoku(incorrecto1))  # >>> False
    print(check_sudoku(correcto))  # >>> True
    print(check_sudoku(incorrecto2))  # >>> False
    print(check_sudoku(incorrecto3))  # >>> False
    print(check_sudoku(incorrecto4))  # >>> False
    print(check_sudoku(incorrecto5))  # >>> False
    print(check_sudoku(incorrecto6))  # >>> False
    print("-------------------")
    # casos test es_cuadrada
    print("ES CUADRADA")
    print(es_cuadrada(incorrecto1))  # >>> True
    print(es_cuadrada(correcto))  # >>> True
    print(es_cuadrada(incorrecto2))  # >>> True
    print(es_cuadrada(incorrecto3))  # >>> True
    print(es_cuadrada(incorrecto4))  # >>> True
    print(es_cuadrada(incorrecto5))  # >>> True
    print(es_cuadrada(incorrecto6))  # >>> False

    # casos test son_entero

    print("-------------------")
    print("SON ENTEROS")
    print(son_enteros(incorrecto1))  # >>> True
    print(son_enteros(correcto))  # >>> True
    print(son_enteros(incorrecto2))  # >>> True
    print(son_enteros(incorrecto3))  # >>> True
    print(son_enteros(incorrecto4))  # >>> False
    print(son_enteros(incorrecto5))  # >>> False
    print(son_enteros(incorrecto6))  # >>> True

    # casos test fila_correcta
    print("-------------------")
    print("FILA CORRECTA")
    print(fila_correcta(incorrecto1))  # >>> True
    print(fila_correcta(correcto))  # >>> True
    print(fila_correcta(incorrecto2))  # >>> True
    print(fila_correcta(incorrecto3))  # >>> True
    print(fila_correcta(incorrecto4))  # >>> False
    print(fila_correcta(incorrecto5))  # >>> False
    print(fila_correcta(incorrecto6))  # >>> True

    # casos test columna_correcta
    print("-------------------")
    print("COLUMNA CORRECTA")
    print(columna_correcta(correcto))  # >>> True
    print(columna_correcta(incorrecto1))  # >>> True
    print(columna_correcta(incorrecto2))  # >>> True
    print(columna_correcta(incorrecto3))  # >>> True
    print(columna_correcta(incorrecto4))  # >>> False
    print(columna_correcta(incorrecto5))  # >>> False
    print(columna_correcta(incorrecto6))  # >>> True

    # casos test rango_correcto

    print("-------------------")
    print("RANGO CORRECTO")
    print(rango_correcto(correcto))     # >>> True
    print(rango_correcto(incorrecto1))  # >>> True
    print(rango_correcto(incorrecto2))  # >>> True
    print(rango_correcto(incorrecto3))  # >>> False
    print(rango_correcto(incorrecto4))  # >>> True
    print(rango_correcto(incorrecto5))  # >>> True
    print(rango_correcto(incorrecto6))  # >>> True
