def es_cuadrada(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    numero_filas = len(sudoku)  # cuántas filas tiene
    for fila in range(numero_filas):  # recorremos cada fila por su posición
        if (
            len(sudoku[fila]) != numero_filas
        ):  # si una fila no mide lo mismo que el nº de filas
            return False  # no es cuadrada
    return True  # todas las filas miden lo mismo que el nº de filas

if __name__ == "__main__":
    # Casos test
    correcto = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

    incorrecto1 = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]

    incorrecto2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

    incorrecto3 = [
        [1, 2, 3, 4, 5],
        [2, 3, 1, 5, 6],
        [4, 5, 2, 1, 3],
        [3, 4, 5, 2, 1],
        [5, 6, 4, 3, 2],
    ]

    incorrecto4 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

    incorrecto5 = [[1, 1.5], [1.5, 1]]

    incorrecto6 = [[1, 0, 0, 0], [0, 1, 0], [0, 0, 0, 1]]
        
    # casos test es_cuadrada
    assert es_cuadrada(incorrecto1) is True
    assert es_cuadrada(correcto) is True
    assert es_cuadrada(incorrecto2) is True
    assert es_cuadrada(incorrecto3) is True
    assert es_cuadrada(incorrecto4) is True
    assert es_cuadrada(incorrecto5) is True
    assert es_cuadrada(incorrecto6) is False