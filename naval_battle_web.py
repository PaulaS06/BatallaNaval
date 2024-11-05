from flask import Flask, render_template, request, redirect, url_for, session, flash

from src.controller.NavalBattleController import Controller_NB
from src.model.logic import NavalBattle_logic
from src.model.NavalBattleModel import Model_NB

def validar_numero(valor):
    """Función que verifica si el valor es un número."""
    if not valor.isdigit():
        raise NavalBattle_logic.NonNumericValueError("** Error: Se ingresó un valor no numérico.")
    if len(valor) != 5:
        raise NavalBattle_logic.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")

naval_battle_web = Flask(__name__)
naval_battle_web.secret_key = b'\xf0\xd1\x06\xb5_\x88\xec\x12=\x03b\xe75U\xd8\xa5'

class RouteApp:

    @naval_battle_web.route('/')
    def inicio():
        return render_template('inicio.html')

    @naval_battle_web.route('/menu')
    def elegir_opcion():
        return render_template('menu.html')


    @naval_battle_web.route('/buscar', methods=['GET', 'POST'])
    def buscar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            session['starting_code'] = starting_code
            return redirect(url_for('reporte'))
        return render_template('buscar_partida.html')

    @naval_battle_web.route('/reporte', methods=['GET'])
    def reporte():
        starting_code = session.get('starting_code')
        validar_numero(starting_code)

        if not starting_code:
            return "Error: starting_code no proporcionado"
        try:
            partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
            if partida_buscada is None: 
                return "Error: No se encontró el registro con el código proporcionado"
        except Exception as err:
            print(f"** Error: No se encontró la partida con código {starting_code}.")
            raise err

        return render_template('reporte_partida.html', 
                            partida=partida_buscada.starting_code,
                            tablero=partida_buscada.rows + "x" + partida_buscada.columns,
                            disparos_efectivos = partida_buscada.hits,
                            disparos_perdidos = partida_buscada.misses,
                            disparos_totales = partida_buscada.total_shots,
                            barcos=partida_buscada.ship_count, 
                            puntaje=partida_buscada.score)


    @naval_battle_web.route('/eliminar', methods=['GET', 'POST'])
    def eliminar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            session['starting_code'] = starting_code
            return redirect(url_for('resultado_eliminacion'))
        return render_template('eliminar_partida.html')
    
    @naval_battle_web.route('/anuncio_eliminar', methods=['GET'])
    def resultado_eliminacion():
        starting_code = session.get('starting_code')
        validar_numero(starting_code)
        
        if not starting_code:
            return "Error: starting_code no proporcionado"
        
        try:
            validar_numero(starting_code)
            Controller_NB.EliminarPartida(starting_code)
            result_message = f"Se eliminó la partida con código {starting_code} exitosamente."
        except Exception as err:
            result_message = f"Error: No se encontró la partida con código {starting_code}."
            print(err)  # Log the error for debugging purposes
        
        return render_template('anuncio_eliminar.html', 
                               partida=starting_code, 
                               result_message=result_message)
        
    @naval_battle_web.route('/insertar', methods=['GET', 'POST'])
    def insertar_partida():
        if request.method == 'POST':
            try:
                # Obtener los valores del formulario
                starting_code = request.form.get('starting_code')
                validar_numero(starting_code)
                if len(starting_code) != 5:
                    raise NavalBattle_logic.InvalidStartingCodeError("** Error: El código de partida debe ser un número de exactamente 5 dígitos.")
    
                rows = request.form.get('rows')
                rows = int(rows)
                columns = request.form.get('columns')
                columns = int(columns)
                ship_count = request.form.get('ship_count')
                hits = request.form.get('hits')
                hits = int(hits)
                misses = request.form.get('misses')
                misses = int(misses)
                total_shots = hits + misses
                max_possible_shots = rows * columns
                score = request.form.get('score')
    
                nueva_partida = Model_NB(
                    starting_code=starting_code,
                    rows=rows,
                    columns=columns,
                    ship_count=ship_count,
                    hits=hits,
                    misses=misses,
                    total_shots=total_shots,
                    max_possible_shots=max_possible_shots,
                    score=score
                )
                # Guardar en la base de datos
                Controller_NB.Insertar(nueva_partida)
                flash('Partida insertada exitosamente', 'success')
                return redirect(url_for('anuncio_insertar'))
            except Exception as e:
                flash(str(e), 'error')
                return redirect(url_for('anuncio_insertar'))
        return render_template('insertar_partida.html')
    
    @naval_battle_web.route('/anuncio_insertar', methods=['GET'])
    def anuncio_insertar():
        return render_template('anuncio_insertar.html')

    
if __name__ == '__main__':
    naval_battle_web.run(debug=True)