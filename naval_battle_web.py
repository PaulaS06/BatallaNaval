from flask import Flask, render_template, request, redirect, url_for

# import sys
# sys.path.append("src")

from src.Controller.NavalBattleController import Controller_NB
from src.Model.NavalBattleModel import Model_NB
from src.Model.logic.NavalBattle_logic import NonNumericValueError, EmptyStartingCodeError, InvalidLengthCodeError, InvalidTypeError, InvalidDimensionError, NonNumericValueErrorShots, InvalidScoreLimitError

naval_battle_web = Flask(__name__)

# Función de validación de código de partida
def validar_codigo(starting_code):
    if not starting_code:
        return str(EmptyStartingCodeError())
    if not starting_code.isdigit():
        return str(NonNumericValueError())
    if len(starting_code) != 5:
        return str(InvalidLengthCodeError())
    return None

# Función de validación de datos de la partida
def validar_datos_partida(starting_code, rows, columns, ship_count, hits, misses, score):
    error = validar_codigo(starting_code)
    if error:
        return error

    if not rows.isdigit() or not columns.isdigit():
        return str(InvalidTypeError())
    
    rows = int(rows)
    columns = int(columns)

    if not (5 <= rows <= 9 and 5 <= columns <= 9):
        return str(InvalidDimensionError())
    
    if not ship_count.isdigit() or int(ship_count) < 1 or int(ship_count) > min(rows, columns) - 1:
        return f"Error: El número de barcos debe estar entre 1 y {min(rows, columns) - 1}."

    if not hits.isdigit() or not misses.isdigit():
        return str(NonNumericValueErrorShots())

    if not score.isdigit() or not (0 <= int(score) <= 99999):
        return str(InvalidScoreLimitError())

    return None


class RouteApp:

    @naval_battle_web.route('/')
    def inicio():
        return render_template('inicio.html')

    @naval_battle_web.route('/menu')
    def elegir_opcion():
        return render_template('menu.html')

#Post method: Usado para enviar datos al servidor para ser procesados.
#Get method: Usado para solicitar datos del servidor.

    # Buscar partida
    @naval_battle_web.route('/buscar', methods=['GET', 'POST'])
    def buscar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            return redirect(url_for('resultado_buscar', starting_code=starting_code))
        return render_template('buscar_partida.html')
    
    @naval_battle_web.route('/resultado_buscar', methods=['GET'])
    def resultado_buscar():
        starting_code = request.args.get('starting_code')
    
        error = validar_codigo(starting_code)
        if error:
            return render_template('anuncio_buscar.html', result_message=error)
        
        try:
            partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
            if partida_buscada is None:
                result_message = f"Error: No se encontró el registro con el código {starting_code}."
                return render_template('anuncio_buscar.html', result_message=result_message)
        
        except Exception:
            result_message = f"Error: No se encontró la partida con código {starting_code}, asegúrese de que la partida exista."
            return render_template('anuncio_buscar.html', result_message=result_message)
    
        return render_template('resultado_buscar.html', 
                               partida=partida_buscada.starting_code,
                               tablero=f"{partida_buscada.rows}x{partida_buscada.columns}",
                               impactos=partida_buscada.hits,
                               fallos=partida_buscada.misses,
                               disparos_totales=partida_buscada.total_shots,
                               barcos=partida_buscada.ship_count,
                               puntaje=partida_buscada.score)


    # Eliminar partida
    @naval_battle_web.route('/eliminar', methods=['GET', 'POST'])
    def eliminar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            return redirect(url_for('resultado_eliminacion', starting_code=starting_code))
        return render_template('eliminar_partida.html')
    
    @naval_battle_web.route('/anuncio_eliminar', methods=['GET'])
    def resultado_eliminacion():
        starting_code = request.args.get('starting_code')
        
        error = validar_codigo(starting_code)
        if error:
            return render_template('anuncio_eliminar.html', result_message=error)
        
        try:
            Controller_NB.EliminarPartida(starting_code)
            result_message = f"Se eliminó la partida con código {starting_code} exitosamente."
        except Exception:
            result_message = f"Error: No se encontró la partida con código {starting_code}."
        
        return render_template('anuncio_eliminar.html', result_message=result_message)
    

    # Insertar nueva partida
    @naval_battle_web.route('/insertar', methods=['GET', 'POST'])
    def insertar_partida():
        if request.method == 'POST':
            try:
                starting_code = request.form.get('starting_code')
                rows = request.form.get('rows')
                columns = request.form.get('columns')
                ship_count = request.form.get('ship_count')
                hits = request.form.get('hits')
                misses = request.form.get('misses')
                score = request.form.get('score')
    
                error = validar_datos_partida(starting_code, rows, columns, ship_count, hits, misses, score)
                if error:
                    return render_template('anuncio_insertar.html', result_message=error, starting_code=starting_code)
    
                # starting_code_in_db = Controller_NB.BuscarCodigoPartida(starting_code)
                # if starting_code_in_db is not None:
                #     result_message = f'Error: El código {starting_code} ya está en uso. Por favor, ingrese otro código.'
                #     return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                    
                rows = int(rows)
                columns = int(columns)
                ship_count = int(ship_count)
                hits = int(hits)
                misses = int(misses)
                total_shots = hits + misses
                max_possible_shots = rows * columns
                score = int(score)
                
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
    
                Controller_NB.Insertar(nueva_partida)
                result_message = f'Partida {starting_code} insertada exitosamente.'
                return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
    
            except Exception:
                result_message = f'Error al insertar la partida.'
                return render_template('anuncio_insertar.html', result_message=result_message)
        return render_template('insertar_partida.html')
    
    @naval_battle_web.route('/anuncio_insertar', methods=['GET'])
    def resultado_insertar():
        result_message = request.args.get('result_message')
        starting_code = request.args.get('starting_code')
        return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)


    # Actualizar partida
    @naval_battle_web.route('/actualizar', methods=['GET', 'POST'])
    def actualizar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            return redirect(url_for('informacion_sin_actualizar', starting_code=starting_code))
        return render_template('actualizar_partida.html')
    
    @naval_battle_web.route('/informacion_sin_actualizar', methods=['GET', 'POST'])
    def informacion_sin_actualizar():
        starting_code = request.args.get('starting_code')

        error = validar_codigo(starting_code)
        if error:
            return render_template('anuncio_actualizar.html', result_message=error)
        
        try:
            partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
            if partida_buscada is None:
                result_message = f"Error: No se encontró el registro con el código {starting_code}."
                return render_template('anuncio_actualizar.html', result_message=result_message)
    
        except Exception:
            result_message = f"Error: No se encontró la partida con código {starting_code}, asegúrese de que la partida exista."
            return render_template('anuncio_actualizar.html', result_message=result_message)
        
        return render_template('informacion_sin_actualizar.html', 
                               starting_code=partida_buscada.starting_code,
                               tablero=f"{partida_buscada.rows}x{partida_buscada.columns}",
                               impactos=partida_buscada.hits,
                               fallos=partida_buscada.misses,
                               disparos_totales=partida_buscada.total_shots,
                               barcos=partida_buscada.ship_count, 
                               puntaje=partida_buscada.score)
    
    @naval_battle_web.route('/informacion_actualizar', methods=['GET', 'POST'])
    def informacion_actualizar():
        if request.method == 'POST':
            try:
                starting_code = request.form.get('starting_code')
                rows = request.form.get('rows')
                columns = request.form.get('columns')
                ship_count = request.form.get('ship_count')
                hits = request.form.get('hits')
                misses = request.form.get('misses')
                score = request.form.get('score')

                error = validar_datos_partida(starting_code, rows, columns, ship_count, hits, misses, score)
                if error:
                    return render_template('anuncio_actualizar.html', result_message=error)

                rows = int(rows)
                columns = int(columns)
                ship_count = int(ship_count)
                hits = int(hits)
                misses = int(misses)
                total_shots = hits + misses
                max_possible_shots = rows * columns
                score = int(score)
                
                partida_actualizada = Model_NB(
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

                Controller_NB.Actualizar(starting_code, partida_actualizada)
                return render_template('anuncio_actualizada.html', starting_code=starting_code)

            except Exception:
                result_message = f'Error al actualizar la partida.'
                return render_template('anuncio_actualizar.html', result_message=result_message)
        return render_template('informacion_actualizar.html')
    
    @naval_battle_web.route('/anuncio_actualizada', methods=['GET'])
    def anuncio_actualizada():
        starting_code = request.args.get('starting_code')
        return render_template('anuncio_actualizada.html', starting_code=starting_code)
    
    @naval_battle_web.route('/informacion_actualizada/<starting_code>', methods=['GET'])
    def informacion_actualizada(starting_code):
        partida_actualizada = Controller_NB.BuscarCodigoPartida(starting_code)
    
        return render_template('informacion_actualizada.html', 
                    starting_code=partida_actualizada.starting_code,
                    tablero=partida_actualizada.rows + "x" + partida_actualizada.columns,
                    impactos=partida_actualizada.hits,
                    fallos=partida_actualizada.misses,
                    disparos_totales=partida_actualizada.total_shots,
                    barcos=partida_actualizada.ship_count, 
                    puntaje=partida_actualizada.score)

    if __name__ == '__main__':
        naval_battle_web.run(debug=True)
