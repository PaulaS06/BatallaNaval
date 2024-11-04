import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = self.connect()
        self.create_table_if_not_exists()

    def connect(self):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="batalla_naval",
                user="usuario",
                password="contraseña"
            )
            return connection
        except Exception as e:
            print("Error al conectar a la base de datos:", e)

    def create_table_if_not_exists(self):
        """Crea la tabla `partidas` si no existe."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS partidas (
            id SERIAL PRIMARY KEY,
            jugador1 VARCHAR(100) NOT NULL,
            jugador2 VARCHAR(100) NOT NULL,
            fecha DATE NOT NULL,
            estado VARCHAR(50) DEFAULT 'En curso'
        );
        """
        with self.connection.cursor() as cursor:
            cursor.execute(create_table_query)
            self.connection.commit()
        print("Tabla `partidas` verificada o creada exitosamente.")

    def fetch_one(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
