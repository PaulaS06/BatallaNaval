from flask import Flask, render_template, request, redirect, url_for

from src.controller.NavalBattleController import Controller_NB


naval_battle_web = Flask(__name__)

@naval_battle_web.route('/')
def inicio():
    return render_template('inicio.html')

@naval_battle_web.route('/menu')
def elegir_opcion():
    return render_template('menu.html')

@naval_battle_web.route('/buscar')
def buscar_partida():
    return render_template('buscar.html')


@naval_battle_web.route('/reporte', methods=['GET'])
def reportar():
    starting_code = request.args.get('starting_code')
    if starting_code is None:
        return "Error: starting_code no proporcionado", 400
    
    partida_buscada = Controller_NB.BuscarCodigoPartida(starting_code)
    if partida_buscada is None:
        return "Error: No se encontró el registro con el código proporcionado", 404
    
    return render_template('reporte.html', partida=partida_buscada)


    # if partida_buscada:
    #     # Redirigir a la ruta /reporte pasando los datos de la partida
    #     return redirect(url_for('reporte', 
    #                             partida=partida_buscada,
    #                             tablero =  partida_buscada.rows + "x" + partida_buscada.columns,
    #                             barcos=partida_buscada.ship_count, 
    #                             puntaje=partida_buscada.score))
    # else:
    #     return render_template('buscar_partida.html', error="Partida no encontrada")

# @naval_battle_web.route('/reporte')
# def reporte():
#     partida = request.args.get('partida')
# #    tablero = request.args.get('tablero')
#     barcos = request.args.get('barcos')
#     puntaje = request.args.get('puntaje')

#     return render_template('partida_reporte.html', partida=partida, barcos=barcos, puntaje=puntaje)




if __name__ == '__main__':
    naval_battle_web.run(debug=True)