from flask import Flask, render_template

import sys
sys.path.append('src')
from controller.NavalBattleController import NavalBattleController


web = Flask(__name__)

@web.route('/')
def inicio():
    return render_template('inicio.html')

@web.route('/reporte')
def reporte():
    return render_template('partida_reporte.html')




if __name__ == '__main__':
    web.run(debug=True)