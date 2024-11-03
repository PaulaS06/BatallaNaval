def Eliminar():    
    import sys
    sys.path.append(".") 
    sys.path.append("src")


    from Model.NavalBattleModel import Model_NB
    from Controller.NavalBattleController import Controller_NB
    from Program import NavalBattle

    def validar_numero(valor):
        """Función que verifica si el valor es un número."""
        if not valor.isdigit():
            raise NavalBattle.NonNumericValueError("** Error: Se ingresó un valor no numérico.")

    try:
        print("\nSeleccionó la opción de ELIMINAR. Siga los siguientes pasos:")

        # Validación del código de partida
        while True:
            try:
                starting_code = input("Ingrese el código de la partida que desea eliminar (5 dígitos): ")
                validar_numero(starting_code)
                
                if len(starting_code) != 5:
                    raise NavalBattle.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")
                
                # Intentar eliminar la partida si el código es válido
                partida_eliminar = Controller_NB.EliminarPartida(starting_code)
                break  # Salir del ciclo si no hay errores

            except NavalBattle.NonNumericValueError as e:
                print(e)
            except NavalBattle.InvalidStartingCodeError as e:
                print(e)
            except Exception as err:
                print(f"** Error: No se pudo eliminar la partida con código {starting_code}.")
                raise err

        # Mostrar mensaje de éxito
        print(" .  .  .  .  .  .  .")
        print(f"La partida {starting_code} ha sido eliminada exitosamente.\n")

    except Exception as err:
        print("** Error: Asegúrese de que la partida exista en la base de datos.")
        print(str(err))