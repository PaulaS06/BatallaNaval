def Insertar():

    import sys
    sys.path.append("src")

    from Model.NavalBattleModel import Model_NB
    from Controller.NavalBattleController import Controller_NB
    from Program import NavalBattle

    # Crear una instancia del Modelo    

    game = Model_NB(starting_code=0, rows=0, columns=0, ship_count=0, hits=0, misses=0, total_shots=0, max_possible_shots=0, score=0)

    print("\n Seleccionó la opción de INSERTAR. Siga los siguientes pasos:")

    def validar_numero(valor):
        """Función que verifica si el valor es un número."""
        if not valor.isdigit():
            raise NavalBattle.NonNumericValueError("** Error: Se ingresó un valor no numérico.")

    # Validación para starting_code (número de 5 dígitos)
    while True:
        try:
            game.starting_code = input("Ingrese el código de la partida (5 dígitos): ")
            validar_numero(game.starting_code)
            if len(game.starting_code) != 5:
                raise NavalBattle.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")
            game.starting_code = int(game.starting_code)
            break
        except NavalBattle.NonNumericValueError as e:
            print(e)
        except NavalBattle.InvalidStartingCodeError as e:
            print(e)

    # Validación para rows y columns (entre 5 y 9)
    while True:
        try:
            game.rows = input("Ingrese el número de filas del tablero (entre 5 y 9): ")
            validar_numero(game.rows)
            game.columns = input("Ingrese el número de columnas del tablero (entre 5 y 9): ")
            validar_numero(game.columns)

            game.rows = int(game.rows)
            game.columns = int(game.columns)

            if not (5 <= game.rows <= 9 and 5 <= game.columns <= 9):
                raise NavalBattle.InvalidDimensionError("** Error: El número de filas y columnas debe estar entre 5 y 9.")
            break
        except NavalBattle.NonNumericValueError as e:
            print(e)
        except NavalBattle.InvalidDimensionError as e:
            print(e)

    # Validación para ship_count (mínimo 1 y máximo menor entre rows y columns - 1)
    while True:
        try:
            game.ship_count = input(f"Ingrese el número de barcos (entre 1 y {min(game.rows, game.columns) - 1}): ")
            validar_numero(game.ship_count)

            game.ship_count = int(game.ship_count)
            max_ship_count = min(game.rows, game.columns) - 1

            if not (1 <= game.ship_count <= max_ship_count):
                raise NavalBattle.InvalidShipCountError(f"** Error: El número de barcos debe estar entre 1 y {max_ship_count}.")
            break
        except NavalBattle.NonNumericValueError as e:
            print(e)
        except NavalBattle.InvalidShipCountError as e:
            print(e)

    # Validación para score (número de máximo 4 cifras y mínimo 0)
    while True:
        try:
            game.score = input("Ingrese el puntaje de la partida (máximo 5 dígitos, mínimo 0): ")
            validar_numero(game.score)

            game.score = int(game.score)

            if not (0 <= game.score <= 99999):
                raise NavalBattle.InvalidScoreError("** Error: El puntaje debe ser un número entre 0 y 9999.")
            break
        except NavalBattle.NonNumericValueError as e:
            print(e)
        except NavalBattle.InvalidScoreError as e:
            print(e)

    # Llamar al controlador para que inserte en la BD
    Controller_NB.Insertar(game)
    print(" .  .  .  .  .  .  .")
    print("Los datos de la partida se ingresaron exitosamente! \n")
