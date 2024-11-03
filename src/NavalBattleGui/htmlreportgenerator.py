# src/NavalBattleGui/HTMLReportGenerator.py
from jinja2 import Environment, FileSystemLoader
import webbrowser
import os

class HTMLReportGenerator:
    def __init__(self):
        # Configura el entorno de Jinja2 para buscar plantillas en el directorio 'templates'
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render_partida_reporte(self, partida):
        # Carga la plantilla 'partida_reporte.html'
        template = self.env.get_template("partida_reporte.html")
        # Renderiza la plantilla con los datos de la partida
        html_output = template.render(
            jugador1=partida['jugador1'],
            jugador2=partida['jugador2'],
            fecha=partida['fecha'],
            estado=partida['estado']
        )
        # Guarda el archivo HTML y lo abre en el navegador
        file_path = os.path.abspath("partida_reporte.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_output)
        webbrowser.open(f"file://{file_path}")

    def render_partidas_resumen(self, partidas):
        # Carga la plantilla 'partidas_resumen.html'
        template = self.env.get_template("partidas_resumen.html")
        # Renderiza la plantilla con el listado de partidas
        html_output = template.render(partidas=partidas)
        # Guarda el archivo HTML y lo abre en el navegador
        file_path = os.path.abspath("partidas_resumen.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_output)
        webbrowser.open(f"file://{file_path}")
