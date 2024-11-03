import unittest
import sys
sys.path.append( "." )

from src.Model.NavalBattleModel import Model_NB
from src.Controller.NavalBattleController import Controller_NB

class Test_DB( unittest.TestCase ):

    #Test Fixture
    def setUpClass():
        # Llamar a la clase COntrolador para que cree la tabla
        Controller_NB.EliminarTabla()
        Controller_NB.CrearTabla()
    
    def test_insert( self ):
        
        # Crear una partida del juego
        game = Model_NB( starting_code="12345", rows="6", columns="7", ship_count="3", hits=9, misses=10, total_shots=19,
                        max_possible_shots=42,  score=18763)
        
        # Guardarla en la BD
        Controller_NB.Insertar( game )
        
        # Buscarla
        starting_search = Controller_NB.BuscarCodigoPartida( starting_code="12345" )
        
        # Verificar si la trajo bien
        self.assertTrue(  starting_search.EsIgual( game )  )

    def test2_insert( self ):
        Controller_NB.BorrarTodo()
        
        # Crear una partida del juego
        game2 = Model_NB( starting_code="09876", rows="9", columns="7", ship_count="6", hits=18, misses=29, total_shots=50,
                        max_possible_shots=63,  score=9900)
        
        # Guardarla en la BD
        Controller_NB.Insertar( game2 )
        
        # Buscarla
        starting_search2 = Controller_NB.BuscarCodigoPartida( starting_code="09876" )
        
        # Verificar si la trajo bien
        self.assertTrue(  starting_search2.EsIgual( game2 )  )

    def test_Error_PrimaryKey(self):
        # Inserta una partida en la tabla
        codigo_prueba  = Model_NB( starting_code="55555", rows="5", columns="5", ship_count="3", hits=11, misses=3, total_shots=14,
                        max_possible_shots=25,  score=20000 )
        Controller_NB.Insertar( codigo_prueba )

        # Inserta una partida en la tabla
        codigo_otro  = Model_NB( starting_code="55555", rows="8", columns="8", ship_count="5", hits=15, misses=23, total_shots=38,
                        max_possible_shots=64,  score=15555  )
        
        self.assertRaises( Exception, Controller_NB.Insertar, codigo_otro )

    def test_delete( self ):

        #Codigo de partida se desea eliminar
        game = Model_NB( starting_code="09876", rows="9", columns="7", ship_count="6", hits=18, misses=29, total_shots=50,
                        max_possible_shots=63,  score=9900)
                     
        # Guardarla en la BD
        Controller_NB.EliminarPartida( game.starting_code )

    def test_delete_error(self):
        # Código de partida que no existe en la BD
        game = Model_NB( starting_code="09876", rows="9", columns="7", ship_count="6", hits=18, misses=29, total_shots=50,
                        max_possible_shots=63,  score=9900)
        
        # Verificar que lanzar excepción al intentar eliminar un registro inexistente
        self.assertRaises(Exception, Controller_NB.EliminarPartida, game.starting_code)

    def test_buscar_partida(self):
        # Buscar una partida en la tabla
        busqueda_prueba  = Model_NB( starting_code="55555", rows="5", columns="5", ship_count="3", hits=11, misses=3, total_shots=14,
                        max_possible_shots=25,  score=20000 )
        
        busqueda = Controller_NB.BuscarCodigoPartida( busqueda_prueba.starting_code )    

         # Verificar si la trajo bien
        self.assertTrue(  busqueda.EsIgual( busqueda_prueba )  )

    def test_error_buscar_partida(self):
        # Buscar una partida en la tabla
        busqueda_prueba  = Model_NB( starting_code="66666", rows="5", columns="5", ship_count="3", hits=11, misses=3, total_shots=14,
                        max_possible_shots=25,  score=20000 )
                 
        self.assertRaises(Exception, Controller_NB.BuscarCodigoPartida, busqueda_prueba.starting_code)  


    def test_actualizar_partida(self):
        #Insertar un registro en la base de datos
        partida_inicial = Model_NB(
            starting_code="11111", rows="5",  columns="5", ship_count="3", hits=10, misses=5, total_shots=15, 
            max_possible_shots=20, score=5000 )
        
        Controller_NB.Insertar(partida_inicial)

        # Actualizar el registro ingresado anteriormente con nuevos valores
        partida_actualizada = Model_NB(
            starting_code="11111",  rows="9", columns="9", ship_count="8", hits=20, misses=10, total_shots=30, 
            max_possible_shots=40, score=10000)
        
        Controller_NB.Actualizar(partida_inicial.starting_code, partida_actualizada)

        # Buscar el registro actualizado
        partida_busqueda = Controller_NB.BuscarCodigoPartida(partida_inicial.starting_code)

        # Verificar que los cambios se realizaron correctamente
        self.assertTrue(partida_busqueda.EsIgual(partida_actualizada))

    def test_actualizar_partida_inexistente(self):
        # Intentar actualizar un registro que no existe en la base de datos
        partida_inexistente = Model_NB(starting_code="99999", rows="7", columns="7", ship_count="5", hits=15, misses=10, total_shots=25,
            max_possible_shots=35, score=7000)
        
        self.assertRaises(Exception, Controller_NB.Actualizar, partida_inexistente.starting_code, partida_inexistente)    
                  
if __name__ == '__main__':
    unittest.main()        