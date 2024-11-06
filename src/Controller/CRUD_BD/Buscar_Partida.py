def Buscar():    
    import sys
    sys.path.append("src")

    from Controller.NavalBattleController import Controller_NB
    from Model.logic import NavalBattle_logic

    def validar_numero(valor):
        """Función que verifica si el valor es un número."""
        if not valor.isdigit():
            raise NavalBattle_logic.NonNumericValueError("** Error: Se ingresó un valor no numérico.")
        if len(valor) != 5:
            raise NavalBattle_logic.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")

    try:
        print("\nSeleccionó la opción de BUSCAR. Siga los siguientes pasos:")

        # Validación del código de partida
        while True:
            try:
                starting_code = input("Ingrese el código de la partida que desea buscar (5 dígitos): ")
                validar_numero(starting_code)
                
                partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
                break  # Salir del ciclo si no hay errores

            except NavalBattle_logic.NonNumericValueError as e:
                print(e)
            except NavalBattle_logic.InvalidStartingCodeError as e:
                print(e)
            except Exception as err:
                print(f"** Error: No se encontró la partida con código {starting_code}.")
                raise err

        # Mostrar información de la partida encontrada
        print(" .  .  .  .  .  .  .")
        print(f"* Partida encontrada: Tablero de {partida_buscada.rows}x{partida_buscada.columns}, Barcos: {partida_buscada.ship_count}, Puntaje obtenido: {partida_buscada.score}\n")

    except Exception as err:
        print("** Error: Asegúrese de que la partida exista.")
        print(str(err))