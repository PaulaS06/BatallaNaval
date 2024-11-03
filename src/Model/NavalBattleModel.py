
class Model_NB :
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa los datos de una partida en la aplicación
    """
    
    def __init__(self, starting_code: int ,
        rows : int,
        columns : int,
        ship_count : int,
        hits : int,
        misses : int,
        total_shots: int,
        max_possible_shots: int,
        score : int):
         
        """  Representa los datos de una partida del juego que se almacenana en la tabla navalbattle """
        self.starting_code = starting_code
        self.rows = rows
        self.columns = columns
        self.ship_count = ship_count
        self.hits = hits
        self.misses = misses
        self.total_shots = total_shots
        self.max_possible_shots = max_possible_shots
        self.score = score
        
    def EsIgual( self, comparar_con ):
        """ Verifica si esta instancia de la clase es igual a otra """

        assert(self.starting_code  == comparar_con.starting_code)
        assert(self.rows  == comparar_con. rows)
        assert(self.columns  == comparar_con. columns)
        assert(self.ship_count  == comparar_con. ship_count)
        assert(self.hits  == comparar_con. hits)
        assert(self.misses  == comparar_con. misses)
        assert(self.total_shots  == comparar_con. total_shots)
        assert(self.max_possible_shots == comparar_con. max_possible_shots)
        assert(self.score  == comparar_con. score)
             
        return True
        