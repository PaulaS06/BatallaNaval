from flask import Flask, render_template, request, redirect, url_for, session

from src.controller.NavalBattleController import Controller_NB


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

        if not starting_code:
            return "Error: starting_code no proporcionado"

        partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
        if partida_buscada is None: 
            return "Error: No se encontró el registro con el código proporcionado"

        return render_template('reporte_partida.html', 
                            partida=partida_buscada.starting_code,
                            tablero=partida_buscada.rows + "x" + partida_buscada.columns,
                            disparos_efectivos = partida_buscada.hits,
                            disparos_perdidos = partida_buscada.misses,
                            disparos_totales = partida_buscada.total_shots,
                            barcos=partida_buscada.ship_count, 
                            puntaje=partida_buscada.score)


if __name__ == '__main__':
    naval_battle_web.run(debug=True)