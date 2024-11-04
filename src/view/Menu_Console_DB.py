import sys
sys.path.append("src")

from controller.CRUD_BD import Insertar_Partida 
from controller.CRUD_BD import Eliminar_Partida
from controller.CRUD_BD import Buscar_Partida
from controller.CRUD_BD import Actualizar_Partida 


def mostrar_menu():
    print("---- Menú Principal ----")
    print("Ingrese la opción de número correspondiente a la función que desea realizar")
    print("- INSERTAR: '1' ")
    print("- ELIMINAR: '2' ")
    print("- BUSCAR: '3' ")
    print("- ACTUALIZAR: '4' ")
    print("- SALIR: '5'")
    print("---------------------------------------------")

def ejecutar_opcion(opcion):
    if opcion == '1':
        # Llamar a la función para insertar 
        Insertar_Partida.Insertar()
    elif opcion == '2':
        # Llamar a la función para eliminar 
        Eliminar_Partida.Eliminar()
    elif opcion == '3':
        # Llamar a la función para buscar 
        Buscar_Partida.Buscar()
    elif opcion == '4':
        # Llamar a la función para actualizar 
        Actualizar_Partida.Actualizar()
    elif opcion == '5':
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción de 1 a 5 según su solicitud: ")
        ejecutar_opcion(opcion)
