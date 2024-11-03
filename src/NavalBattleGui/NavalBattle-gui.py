import sys
sys.path.append("src")
# Importar NavalBattle desde donde está definido
from Program.NavalBattle import NavalBattle
from Controller.NavalBattleController import Controller_NB
from Model.NavalBattleModel import Model_NB


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class NavalBattleApp(App):
    def build(self):
        self.title = 'Batalla Naval'
        
        # Mostrar el popup para que el usuario ingrese las dimensiones del tablero y el número de barcos
        self.show_board_size_popup()

        return BoxLayout()  # Retornamos un layout vacío mientras tanto

    def show_board_size_popup(self):
        # Layout para el Popup
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text='Ingrese las dimensiones del tablero (min: 5, max: 9)'))

        # Entrada para las filas
        self.row_input = TextInput(hint_text='Número de filas', input_filter='int', multiline=False)
        box.add_widget(self.row_input)

        # Entrada para las columnas
        self.col_input = TextInput(hint_text='Número de columnas', input_filter='int', multiline=False)
        box.add_widget(self.col_input)

        # Entrada para el número de barcos
        self.ship_input = TextInput(hint_text='Número de barcos', input_filter='int', multiline=False)
        box.add_widget(self.ship_input)

        # Botón para confirmar
        confirm_button = Button(text='Confirmar')
        confirm_button.bind(on_press=self.on_confirm_board_size)
        box.add_widget(confirm_button)

        # Crear y mostrar el Popup
        self.popup = Popup(title='Configuración del Tablero',
                           content=box,
                           size_hint=(0.75, 0.5),
                           auto_dismiss=False)
        self.popup.open()

    def on_confirm_board_size(self, instance):
        # Obtener y validar las dimensiones ingresadas
        try:
            rows = int(self.row_input.text)
            cols = int(self.col_input.text)
        except ValueError:
            self.show_error_popup('Por favor, ingrese números válidos.')
            return

        # Validar que las dimensiones estén entre 5 y 9
        if not (5 <= rows <= 9) or not (5 <= cols <= 9):
            self.show_error_popup('Las dimensiones deben estar entre 5 y 9.')
            return
        
        # Obtener el número máximo de barcos
        max_ships = min(rows, cols) - 1  # El límite máximo de barcos

        # Obtener y validar el número de barcos
        try:
            ships = int(self.ship_input.text)
        except ValueError:
            self.show_error_popup(f'Por favor, ingrese un número de barcos válido (1 a {max_ships}).')
            return

        # Validar que el número de barcos esté dentro del rango permitido
        if not (1 <= ships <= max_ships):
            self.show_error_popup(f'El número de barcos debe estar entre 1 y {max_ships}.')
            return
        
        # Si todo es válido, cerrar el Popup y empezar el juego
        self.popup.dismiss()
        rows_db = rows
        column_db = cols 
        self.start_game(rows, cols, ships)  # Iniciar el juego con el número de barcos


    def start_game(self, rows, cols, ships):
        # Crear una instancia del juego
        self.game = NavalBattle()  

        self.game.reset_stats() 
        
        # Generar el tablero con las dimensiones ingresadas
        self.game.generateBoard(w=cols, h=rows)
        
        # Añadir los barcos de acuerdo al número especificado
        self.game.addShips(ships)

        # Crear el tablero visual en la interfaz
        self.create_game_board(rows, cols)

    def create_game_board(self, rows, cols):
        # Configuraciones del tablero con las dimensiones ingresadas
        self.board_width = cols
        self.board_height = rows
        self.buttons = {}  # Diccionario para almacenar los botones

        # Crear un layout de cuadrícula para el tablero
        layout = GridLayout(cols=self.board_width, rows=self.board_height)
        
        # Crear botones para representar cada casilla del tablero
        for row in range(self.board_height):
            for col in range(self.board_width):
                btn = Button(text='?', font_size=32, background_normal='', background_color=[.5, .5, 1, .5])
                btn.bind(on_press=self.on_button_click)  # Vincular a evento
                self.buttons[(row, col)] = btn
                layout.add_widget(btn)

        # Añadir el layout del tablero al root widget
        self.root.clear_widgets()
        self.root.add_widget(layout)

    def on_button_click(self, instance):
        # Obtener la posición del botón clicado
        for pos, button in self.buttons.items():
            if button == instance:
                row, col = pos
                break

        # Lógica que manejará el clic de un botón
        hit = self.game.shoot(row, col)  # Suponiendo que shoot actualiza el tablero y devuelve True si acierta

        if hit:
            self.game.board[row][col] = 0  # Reemplazar con 0 ya que fue un impacto
            
            # Cambiar el color del botón
            instance.background_color = [1, 36/255, 26/255, 5]  # Rojo para un disparo acertado
            instance.text = 'X'
            
            # Verificar si el barco fue hundido
            if self.game.check_ship_sunk(self.game.last_hit):
                self.show_sunk_ship_popup(self.game.last_hit, lambda: self.show_victory_popup() if self.game.all_ships_sunk() else None)

        else:
            instance.background_color = [127/255, 181/255, 246/255, 5]  # Azul para un disparo fallido
            instance.text = '~'
        
        instance.disabled = True  # Deshabilitar el botón después de un disparo

    def show_popup(self, title, message, size_hint=(0.75, 0.5), restart_button=False, upload_db = False,  callback=None):
        """Método unificado para mostrar popups."""
        content = BoxLayout(orientation='vertical')
        msg_label = Label(text=message)
        close_button = Button(text='Cerrar', size_hint=(1, 0.2))
        
        content.add_widget(msg_label)
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=size_hint, auto_dismiss=False)

        close_button.bind(on_press=popup.dismiss)

        # Si el botón de reinicio es True, se añade el botón de reinicio
        if restart_button and  upload_db :
            restart_button = Button(text='Reiniciar', size_hint=(1, 0.2))
            upload_db = Button(text='Cargar datos al DB', size_hint=(1, 0.2))
            content.add_widget(restart_button)
            content.add_widget(upload_db)
            
            # Función para reiniciar el juego
            def restart_game(instance):
                popup.dismiss()  # Cerrar el popup
                self.show_board_size_popup()  # Volver a mostrar el popup para ingresar dimensiones

            def upload_data (instance):
                summary = self.game.get_summary() 
  
                game = Model_NB( starting_code=summary['id'], rows=str(summary['row']), columns=str(summary['column']), ship_count=str(summary['ship_count']),
                                 hits=int(summary['hits']), misses=int(summary['misses']), total_shots= int(summary['total_shots']),
                        max_possible_shots=int(summary['max_possible_shots']),  score=int(summary['score']) )
        
                # Guardar partida en la BD
                Controller_NB.Insertar( game )

                popup.dismiss()
                self.show_uploaded_db()

            restart_button.bind(on_press=restart_game)  # Vincular el botón a la función de reinicio
            upload_db.bind(on_press=upload_data)

        # Vincular el cierre del popup al callback, si se proporciona
        popup.bind(on_dismiss=lambda instance: callback() if callback else None)

        popup.open()  # Mostrar el popup

    def show_sunk_ship_popup(self, ship_length, callback):
        """Muestra un popup cuando se hunde un barco."""
        remaining_ships = self.game.get_remaining_ships()  # Llama a la función sin argumentos
        message = f"¡Has hundido un barco de longitud {ship_length}! Quedan {remaining_ships} barcos restantes."
        
        # Muestra el popup y ejecuta el callback después de que se cierra
        self.show_popup(title='¡Barco hundido!', message=message, callback=callback)
    
    def check_victory(self):
        if self.game.all_ships_sunk():
            self.show_victory_popup()  # Mostrar popup de victoria si no quedan barcos

    def show_uploaded_db(self):
        """ Muestra un popup cuando se cargan los datos."""
        message = "Se han cargado los datos de la partida correctamente"
        self.show_popup(title='¡Carga exitosa!', message=message, callback=None)


    def show_victory_popup(self):
        """Muestra un popup para la victoria con estadísticas de la partida."""
        summary = self.game.get_summary()  # Obtener el resumen de la partida
        message = (f'¡Felicidades! Has hundido todos los barcos.\n'
                f'ID de la partida: {summary["id"]}\n'
                f'Tiros acertados: {summary["hits"]}\n'
                f'Tiros fallidos: {summary["misses"]}\n'
                f'Total de tiros realizados: {summary["total_shots"]}\n'
                f'Máximo de tiros posibles: {summary["max_possible_shots"]}\n'
                f'Numero de barcos derribados: {summary["ship_count"]}\n'
                f'Puntaje: {summary["score"]:.2f}'
                                )  # Formato del puntaje
        
        self.show_popup(title='¡VICTORIA!', message=message, restart_button=True, upload_db =True)


    def show_error_popup(self, error_message):
        """Muestra un popup para errores del tablero."""
        self.show_popup(title='Error dato inválido ', message=error_message)
  
if __name__ == '__main__':
    NavalBattleApp().run()