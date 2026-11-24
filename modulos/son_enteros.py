def son_enteros(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    for fila in sudoku:  # cogemos cada fila
        for num_columna in fila:  # cogemos cada elemento de la fila
            if type(num_columna) != int:  # si alguno no es int
                return False  # ya no vale
    return (
        True  # este return va FUERA de los dos for: solo se llega aquí si TODOS son int
    )

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

    # casos test son_enteros
    assert son_enteros(incorrecto1) is True
    assert son_enteros(correcto) is True
    assert son_enteros(incorrecto2) is True
    assert son_enteros(incorrecto3) is True
    assert son_enteros(incorrecto4) is False
    assert son_enteros(incorrecto5) is False
    assert son_enteros(incorrecto6) is True