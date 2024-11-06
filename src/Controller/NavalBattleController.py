import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2

from model.NavalBattleModel import Model_NB
import SecretConfig

class Controller_NB:

    def BorrarTodo():
        """ Borra todos las filas de la tabla tarjetas """
        cursor = Controller_NB.ObtenerCursor()
        cursor.execute(  "delete from navalbattle;")
        cursor.connection.commit()

    def CrearTabla():
        """ Crea la tabla de navalbattle en la BD """
        cursor = Controller_NB.ObtenerCursor()

        cursor.execute("""create table navalbattle (
        starting_code varchar(5) primary key not null,
        rows varchar(1) not null,
        columns varchar(1) not null,
        ship_count varchar(1) ,
        hits int ,
        misses int ,
        total_shots int ,
        max_possible_shots int ,
        score int not null
        ); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla navalbattle de la BD """
        cursor = Controller_NB.ObtenerCursor()

        cursor.execute("""drop table if exists navalbattle""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def Insertar( game : Model_NB) :
        """ Recibe un a instancia de la clase Model_NB y la inserta en la tabla respectiva"""
        cursor = Controller_NB.ObtenerCursor()
        cursor.execute( f"""insert into navalbattle (starting_code, rows, columns, ship_count, hits, misses, total_shots, max_possible_shots, score) 
                        values ('{game.starting_code}', '{game.rows}', '{game.columns}', '{game.ship_count}', '{game.hits}', {game.misses}, 
                        {game.total_shots}, {game.max_possible_shots}, {game.score})""" )

        cursor.connection.commit()

    def EliminarPartida(starting_code):
        """ Elimina un registro de la tabla navalbattle dado el starting_code """
        cursor = Controller_NB.ObtenerCursor()
        
        # Verificar si el registro existe
        cursor.execute(f"""select starting_code, rows, columns, ship_count, hits, misses, total_shots, max_possible_shots, score 
                       from navalbattle where starting_code = '{starting_code}'""")
        fila = cursor.fetchone()

        Controller_NB.ValidarExistenciaDeRegistro(fila,starting_code )

        # Ejecutar la consulta DELETE
        cursor.execute(f"DELETE FROM navalbattle WHERE starting_code = '{starting_code}'")
        
        # Confirmar los cambios
        cursor.connection.commit()

    def BuscarCodigoPartida( starting_code ) -> Model_NB:
        """ Trae los datos del juego dado su codigo de partida """
        cursor = Controller_NB.ObtenerCursor()

        cursor.execute(f"""select starting_code, rows, columns, ship_count, hits, misses, total_shots, max_possible_shots, score
        from navalbattle where starting_code = '{starting_code}'""" )
        fila = cursor.fetchone()

        Controller_NB.ValidarExistenciaDeRegistro(fila,starting_code )
        
        resultado = Model_NB( starting_code=fila[0], rows=fila[1], columns=fila[2], ship_count=fila[3], hits=fila[4], misses=fila[5], 
                             total_shots=fila[6], max_possible_shots=fila[7], score=fila[8] )
        return resultado
    
    def Actualizar(starting_code, updated_game: Model_NB):
        """ Actualiza los datos del juego en la base de datos dado su código de partida """
        cursor = Controller_NB.ObtenerCursor()

        Controller_NB.ValidarRegistroDeAcualizacion(starting_code )

        # Ejecutar la actualización de los datos con el código de partida proporcionado
        cursor.execute(f"""
            UPDATE navalbattle
            SET rows = '{updated_game.rows}',
                columns = '{updated_game.columns}',
                ship_count = '{updated_game.ship_count}',
                hits = {updated_game.hits},
                misses = {updated_game.misses},
                total_shots = {updated_game.total_shots},
                max_possible_shots = {updated_game.max_possible_shots},
                score = {updated_game.score}
            WHERE starting_code = '{starting_code}';
        """)

        # Confirmar los cambios
        cursor.connection.commit()

    def ValidarExistenciaDeRegistro(fila,starting_code):

        if not fila:
            raise Exception(f"No se encontró el registro con el código {starting_code}")  

    def ValidarRegistroDeAcualizacion (starting_code):  
        
        try:
            Controller_NB.BuscarCodigoPartida(starting_code)  # Intentar buscar el registro
        except Exception as e:
            raise Exception(f"No se encontró el registro con el código {starting_code}") from e

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor