def son_enteros(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    for fila in sudoku:  # cogemos cada fila
        for num_columna in fila:  # cogemos cada elemento de la fila
            if type(num_columna) != int:  # si alguno no es int
                return False  # ya no vale
    return (
        True  # este return va FUERA de los dos for: solo se llega aquí si TODOS son int
    )


def fila_correcta(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    for fila in sudoku:  # cogemos cada fila
        if len(fila) != len(
            set(fila)
        ):  # set quita repetidos: si cambia la longitud, había repetidos
            return False  # fila con números repetidos
    return True  # ninguna fila tiene repetidos


def columna_correcta(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    for i in range(len(sudoku)):  # i = posición de la columna
        numeros_vistos = []  # números que ya hemos visto en esta columna
        for fila in sudoku:  # bajamos por la columna, fila a fila
            numero = fila[i]  # elemento de la columna i en esta fila
            if numero in numeros_vistos:  # si ya lo habíamos visto
                return False  # columna con repetidos
            numeros_vistos.append(numero)  # lo apuntamos como visto
    return True  # ninguna columna tiene repetidos


def rango_correcto(sudoku):
    assert isinstance(sudoku, list), "sudoku tiene que ser una lista"  # precondición
    for fila in sudoku:  # cogemos cada fila
        for numero_buscado in range(
            1, len(sudoku) + 1
        ):  # números que deben estar: de 1 a n
            if numero_buscado not in fila:  # si falta alguno
                return False  # fila sin todos los números de 1 a n
    return True  # todas las filas tienen todos los números de 1 a n


def check_sudoku(sudoku):
    try:  # intentamos hacer las comprobaciones
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
    except (
        AssertionError,
        TypeError,
    ):  # si sudoku no es una lista (assert) o tiene datos raros (TypeError)
        return False  # no es un sudoku válido, pero el programa NO se rompe


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

    # casos test check sudoku
    assert check_sudoku(incorrecto1) is False
    assert check_sudoku(correcto) is True
    assert check_sudoku(incorrecto2) is False
    assert check_sudoku(incorrecto3) is False
    assert check_sudoku(incorrecto4) is False
    assert check_sudoku(incorrecto5) is False
    assert check_sudoku(incorrecto6) is False

    # casos test son_enteros
    assert son_enteros(incorrecto1) is True
    assert son_enteros(correcto) is True
    assert son_enteros(incorrecto2) is True
    assert son_enteros(incorrecto3) is True
    assert son_enteros(incorrecto4) is False
    assert son_enteros(incorrecto5) is False
    assert son_enteros(incorrecto6) is True

    # casos test fila_correcta
    assert fila_correcta(incorrecto1) is False
    assert fila_correcta(correcto) is True
    assert fila_correcta(incorrecto2) is True
    assert fila_correcta(incorrecto3) is True
    assert fila_correcta(incorrecto4) is True
    assert fila_correcta(incorrecto5) is True
    assert fila_correcta(incorrecto6) is False

    # casos test columna_correcta
    assert columna_correcta(correcto) is True
    assert columna_correcta(incorrecto1) is False
    assert columna_correcta(incorrecto2) is False
    assert columna_correcta(incorrecto3) is True
    assert columna_correcta(incorrecto4) is True
    assert columna_correcta(incorrecto5) is True
    assert columna_correcta(incorrecto6) is False

    # casos test rango_correcto
    assert rango_correcto(correcto) is True
    assert rango_correcto(incorrecto1) is False
    assert rango_correcto(incorrecto2) is True
    assert rango_correcto(incorrecto3) is False
    assert rango_correcto(incorrecto4) is False
    assert rango_correcto(incorrecto5) is False
    assert rango_correcto(incorrecto6) is False
