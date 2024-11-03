import sys
sys.path.append("src")

from NavalBattleGui.htmlreportgenerator import HTMLReportGenerator
from controller.CRUD_BD import Functions_DB as db_functions
from src.model.logic.NavalBattle_logic import NavalBattle, BoardError, BoardIsBigAndSmall, BoardIsTooSmall, BoardIsTooBig, NotEnoughSpace, InvalidCoordinate, RowOutOfRange, ColumnOutOfRange

def mostrar_menu():
    print("Bienvenido al juego de Batalla Naval")
    print("1. Jugar una nueva partida")
    print("2. Ver reporte de una partida")
    print("3. Ver resumen de todas las partidas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        # Lógica para iniciar una partida
        pass
    elif opcion == "2":
        partida_id = input("Ingrese el ID de la partida: ")
        partida = db_functions.obtener_partida_por_id(partida_id)  # Debes implementar esta función en Functions_DB
        if partida:
            report_generator = HTMLReportGenerator()
            report_generator.render_partida_reporte(partida)
        else:
            print("No se encontró la partida con ese ID.")
    elif opcion == "3":
        partidas = db_functions.obtener_todas_las_partidas()  # Debes implementar esta función en Functions_DB
        report_generator = HTMLReportGenerator()
        report_generator.render_partidas_resumen(partidas)
    elif opcion == "4":
        print("Gracias por jugar.")
        exit()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    navalBattle = NavalBattle()
    print("Enter the size of the board you want to play on:")
    print("(min:5, max:9)")

    # Control de entrada para las dimensiones del tablero
    while True:
        try:
            w = int(input("Columns: "))
            h = int(input("Rows: "))
            navalBattle.validateBoardDimensions(w, h)
            navalBattle.generateBoard(w, h)
            break
        except BoardError as e:
            print(f"Error: {e}")
        except BoardIsBigAndSmall as e:
            print(f"Error: {e} Board exceeds the limit in one dimension and isn't big enough in the other")
        except BoardIsTooSmall as e:
            print(f"Error: {e} Board doesn't have enough size")
        except BoardIsTooBig as e:
            print(f"Error: {e} Board exceeds the limit size")
        except ValueError:
            print("Please enter a valid number for columns and rows.")    

    # Control de entrada para el número de barcos
    while True:
        try:
            max_ships = h - 1 if w > h else w - 1
            print(f"Maximum {max_ships} ships allowed")
            num_ships = int(input("Enter the number of ships: "))
            navalBattle.addShips(num_ships, max_ships)
            break
        except NotEnoughSpace as e:
            print(f"Error: {e} That quantity wouldn't fit in the board")
        except BoardError as e:
            print(f"Error: {e} There's no board yet")
        except ValueError:
            print("Please enter a valid number for ships.")

    print("Enter the coordinate you want to attack in the format: C2")
    print("Where 'C' is the column and '2' is the row")
    navalBattle.showInfo()
    navalBattle.showPlayerBoard()
    
    while True:
        try:
            coordinate = input("Coordinate: ")
            if navalBattle.isCoordinateAlreadyShot(coordinate):
                print("Don't waste your shots")
            else:
                row, column = navalBattle.validateCoordinate(coordinate)
                if navalBattle.shoot(row, column):
                    print(navalBattle.EMOJIS["ship"], "HIT", navalBattle.EMOJIS["colition"])
                    if navalBattle.isShipDowned():
                        print("Downed Ship")
                        for i in range(navalBattle.last_hit):
                            print(navalBattle.EMOJIS["colition"], end=" ")
                        print("\n")
                else:
                    print(navalBattle.EMOJIS["water"], "WATER", navalBattle.EMOJIS["wave"])

            if navalBattle.ships_quantity == 0:
                navalBattle.showPlayerBoard()
                print("YOU WON!!")
                break
            navalBattle.showPlayerBoard()

        except InvalidCoordinate:
            print("Invalid coordinate format. Please use format like 'C2'.")
        except RowOutOfRange as e:
            print(f"Error: {e} Row out of range")
        except ColumnOutOfRange as e:
            print(f"Error: {e} Column out of range")
        except Exception as e:
            print(f"Error: {e}")
