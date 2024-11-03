# src/Console/Functions_DB.py
import sqlite3

def obtener_partida_por_id(partida_id):
    # Conecta a la base de datos y obtiene los datos de una partida específica
    conn = sqlite3.connect("naval_battle.db")
    cursor = conn.cursor()
    cursor.execute("SELECT jugador1, jugador2, fecha, estado FROM partidas WHERE id = ?", (partida_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'jugador1': row[0],
            'jugador2': row[1],
            'fecha': row[2],
            'estado': row[3]
        }
    return None

def obtener_todas_las_partidas():
    # Conecta a la base de datos y obtiene el resumen de todas las partidas
    conn = sqlite3.connect("naval_battle.db")
    cursor = conn.cursor()
    cursor.execute("SELECT jugador1, jugador2, fecha, estado FROM partidas")
    rows = cursor.fetchall()
    conn.close()
    return [{'jugador1': r[0], 'jugador2': r[1], 'fecha': r[2], 'estado': r[3]} for r in rows]
