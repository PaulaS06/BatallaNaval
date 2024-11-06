from flask import Flask, render_template, request, redirect, url_for, session, flash

from src.controller.NavalBattleController import Controller_NB
from src.model.logic import NavalBattle_logic
from src.model.NavalBattleModel import Model_NB

naval_battle_web = Flask(__name__)
naval_battle_web.secret_key = b'\xf0\xd1\x06\xb5_\x88\xec\x12=\x03b\xe75U\xd8\xa5'


class RouteApp:

    @naval_battle_web.route('/')
    def inicio():
        return render_template('inicio.html')

    @naval_battle_web.route('/menu')
    def elegir_opcion():
        return render_template('menu.html')


#Post method: Usado para enviar datos al servidor para ser procesados.
#Get method: Usado para solicitar datos del servidor.


    @naval_battle_web.route('/buscar', methods=['GET', 'POST'])
    def buscar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            return redirect(url_for('reporte', starting_code=starting_code))
        return render_template('buscar_partida.html')

    @naval_battle_web.route('/reporte')
    def resultado_buscar():
        starting_code = request.args.get('starting_code')

        if not starting_code:
            result_message = "Error: código no proporcionado"
            return render_template('anuncio_buscar.html', result_message=result_message)
        if not starting_code.isdigit():
            result_message = "Error: Debe ingresar un valor numérico."
            return render_template('anuncio_buscar.html', result_message=result_message)
        if len(starting_code) != 5:
            result_message = "Error: El código de partida debe ser un número de exactamente 5 dígitos."
            return render_template('anuncio_buscar.html', result_message=result_message)
        
        try:
            partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
            if partida_buscada is None: 
                result_message = f"Error: No se encontró el registro con el código {starting_code}."
                return render_template('anuncio_buscar.html', result_message=result_message)
        
        except Exception:
            result_message = f"Error: No se encontró la partida con código {starting_code}, asegúrese de que la partida exista."
            return render_template('anuncio_buscar.html', result_message=result_message)

        return render_template('resultado_partida.html', 
                            partida=partida_buscada.starting_code,
                            tablero=partida_buscada.rows + "x" + partida_buscada.columns,
                            impactos = partida_buscada.hits,
                            fallos = partida_buscada.misses,
                            disparos_totales = partida_buscada.total_shots,
                            barcos=partida_buscada.ship_count, 
                            puntaje=partida_buscada.score)



    @naval_battle_web.route('/eliminar', methods=['GET', 'POST'])
    def eliminar_partida():
        if request.method == 'POST':
            starting_code = request.form['starting_code']
            return redirect(url_for('resultado_eliminacion', starting_code=starting_code))
        return render_template('eliminar_partida.html')
    
    @naval_battle_web.route('/anuncio_eliminar', methods=['GET'])
    def resultado_eliminacion():
        starting_code = request.args.get('starting_code')
        
        if not starting_code:
            result_message = "Error: código no proporcionado"
            return render_template('anuncio_eliminar.html', result_message=result_message)
        if not starting_code.isdigit():
            result_message = "Error: Debe ingresar un valor numérico."
            return render_template('anuncio_eliminar.html', result_message=result_message)
        if len(starting_code) != 5:
            result_message = "Error: El código de partida debe ser un número de exactamente 5 dígitos."
            return render_template('anuncio_eliminar.html', result_message=result_message)
        
        try:
            Controller_NB.EliminarPartida(starting_code)
            result_message = f"Se eliminó la partida con código {starting_code} exitosamente."
            return render_template('anuncio_eliminar.html', result_message=result_message)
        except Exception:
            result_message = f"Error: No se encontró la partida con código {starting_code}."
            return render_template('anuncio_eliminar.html', result_message=result_message)
        
        

    @naval_battle_web.route('/insertar', methods=['GET', 'POST'])
    def insertar_partida():
        if request.method == 'POST':
            try:
                
                starting_code = request.form.get('starting_code')

                if not starting_code:
                    result_message = "Error: código no proporcionado"
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                if not starting_code.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                if len(starting_code) != 5:
                    result_message = "Error: El código de partida debe ser un número de exactamente 5 dígitos."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)

                rows = request.form.get('rows')
                columns = request.form.get('columns')

                if not rows.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                if not columns.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                
                rows = int(rows)
                columns = int(columns)

                if not (5 <= rows <= 9 and 5 <= columns <= 9):
                    result_message = "Error: El número de filas y columnas debe estar entre 5 y 9."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)

                ship_count = request.form.get('ship_count')
                if not ship_count.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                ship_count = int(ship_count)
                max_ship_count = min(rows, columns) - 1

                if not (1 <= ship_count <= max_ship_count):
                    result_message = f"Error: El número de barcos debe estar entre 1 y {max_ship_count}."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)

                hits = request.form.get('hits')
                if not hits.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                hits = int(hits)
            
                misses = request.form.get('misses')
                if not misses.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                misses = int(misses)
            
                total_shots = hits + misses
                max_possible_shots = rows * columns
            
                score = request.form.get('score')
                if not score.isdigit():
                    result_message = "Error: Debe ingresar un valor numérico."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
                score = int(score)
            
                if not (0 <= score <= 99999):
                    result_message = "Error: El puntaje debe ser un número entre 0 y 9999."
                    return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
            
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
                result_message = f'Partida {starting_code} insertada exitosamente'
                return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
            
            except Exception as e:
                result_message = f'Error al insertar la partida, intentelo de nuevo. Detalles del error: {str(e)}'
                return render_template('anuncio_insertar.html', result_message=result_message, starting_code=starting_code)
        return render_template('insertar_partida.html')

    

if __name__ == '__main__':
    naval_battle_web.run(debug=True)