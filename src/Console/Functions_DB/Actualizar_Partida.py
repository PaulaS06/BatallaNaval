def Actualizar():
    import sys
    sys.path.append("src")

    from Model.NavalBattleModel import Model_NB
    from Controller.NavalBattleController import Controller_NB
    from Program import NavalBattle

    def validar_numero(valor):
        """Función que verifica si el valor es un número."""
        if not valor.isdigit():
            raise NavalBattle.NonNumericValueError("* Error: Se ingresó un valor no numérico.")

    try:
        updated_game = Model_NB(starting_code=0, rows=0, columns=0, ship_count=0, hits=0, misses=0, total_shots=0, max_possible_shots=0, score=0)
        print("\nSeleccionó la opción de ACTUALIZAR. Siga los siguientes pasos:")

        # Validación del código de partida existente
        while True:
            try:
                starting_code = input("Ingrese el código de la partida que desea actualizar (5 dígitos): ")
                validar_numero(starting_code)
                if len(starting_code) != 5:
                    raise NavalBattle.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")
                partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
                print(f"* Partida {starting_code} encontrada: Tablero de {partida_buscada.rows}x{partida_buscada.columns}, Barcos: {partida_buscada.ship_count}, Puntaje obtenido: {partida_buscada.score}")
                break
            except NavalBattle.NonNumericValueError as e:
                print(e)
            except NavalBattle.InvalidStartingCodeError as e:
                print(e)
            except Exception as err:
                print(f"**Error: No se encontró la partida con código {starting_code}.")
                raise err

        print(" .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .")
        print(f" * * * Ingrese los nuevos datos para actualizar la partida {starting_code}")

        # Validación de filas y columnas
        while True:
            try:
                updated_game.rows = input("Ingrese el nuevo número de filas del tablero (entre 5 y 9): ")
                validar_numero(updated_game.rows)
                updated_game.columns = input("Ingrese el nuevo número de columnas del tablero (entre 5 y 9): ")
                validar_numero(updated_game.columns)

                updated_game.rows = int(updated_game.rows)
                updated_game.columns = int(updated_game.columns)

                if not (5 <= updated_game.rows <= 9 and 5 <= updated_game.columns <= 9):
                    raise NavalBattle.InvalidDimensionError("** Error: El número de filas y columnas debe estar entre 5 y 9.")
                break
            except NavalBattle.NonNumericValueError as e:
                print(e)
            except NavalBattle.InvalidDimensionError as e:
                print(e)

        # Validación del número de barcos
        while True:
            try:
                updated_game.ship_count = input(f"Ingrese el nuevo número de barcos (entre 1 y {min(updated_game.rows, updated_game.columns) - 1}): ")
                validar_numero(updated_game.ship_count)

                updated_game.ship_count = int(updated_game.ship_count)
                max_ship_count = min(updated_game.rows, updated_game.columns) - 1

                if not (1 <= updated_game.ship_count <= max_ship_count):
                    raise NavalBattle.InvalidShipCountError(f"** Error: El número de barcos debe estar entre 1 y {max_ship_count}.")
                break
            except NavalBattle.NonNumericValueError as e:
                print(e)
            except NavalBattle.InvalidShipCountError as e:
                print(e)

        # Validación del puntaje
        while True:
            try:
                updated_game.score = input("Ingrese el nuevo puntaje de la partida (máximo 5 dígitos, mínimo 0): ")
                validar_numero(updated_game.score)

                updated_game.score = int(updated_game.score)

                if not (0 <= updated_game.score <= 99999):
                    raise NavalBattle.InvalidScoreError("** Error: El puntaje debe ser un número entre 0 y 9999.")
                break
            except NavalBattle.NonNumericValueError as e:
                print(e)
            except NavalBattle.InvalidScoreError as e:
                print(e)

        # Actualizar la partida
        partida_update = Controller_NB.Actualizar(starting_code, updated_game)

        # Verificar la actualización
        partida_actualizada = Controller_NB.BuscarCodigoPartida(starting_code)
        print(" .  .  .  .  .  .  .")
        print(f"* Partida {starting_code} actualizada con éxito: Nuevo Tablero: {partida_actualizada.rows}x{partida_actualizada.columns}, Barcos: {partida_actualizada.ship_count}, Nuevo puntaje: {partida_actualizada.score}\n")

    except Exception as err:
        print("** Error: Asegúrese de que la partida exista.")
        print(str(err))

