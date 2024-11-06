## ¿Quién hizo esto?

Entrega 1, 2, 3
- Daniel Calle
- Dilan Urrego

Entrega 4
- Steven Oviedo
- Sara Moncada

**Entrega 5**
- Mario Andrade
- Paula Meneses

## ¿Qué es y para qué es?

- El juego de Batalla Naval es un juego de estrategia en el que el objetivo es hundir los barcos del oponente (en este caso la máquina) adivinando sus ubicaciones en un tablero.
- El juego de Batalla Naval en modalidad individual proporciona un desafío de lógica y estrategia, ya que el jugador debe deducir la posición de los barcos enemigos basándose en los resultados de sus disparos. Además, es entretenido y puede mejorar la capacidad de razonamiento lógico y la toma de decisiones del jugador.

## ¿Cómo lo hago funcionar?

- **Prerrequisitos:**
Instalar Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo e instalarlo desde python.org.

- **Librerías:** Las librerías usadas para este desarrollo son "random" y "kivy", "random" está incluida por defecto en pyhon; debes instalar "kivy" para poder correr la aplicación desde una interfaz gráfica.


- **Ejecución del juego en consola:**
Navega a la carpeta: Una vez que hayas clonado el repositorio, abre el cmd busca la siguiente ruta que contiene la carpeta con el archivo:
```src\view\console\NavalBattleConsole.py```

- **Ejecución de la Base de Datos en consola:**
Navega a la carpeta: Una vez que hayas clonado el repositorio, abre el cmd busca la siguiente ruta que contiene la carpeta con el archivo:
```src\view\console\Menu_Console_DB.py```

- **Ejecución del juego en interfaz gráfica de kivy:**
Navega a la carpeta: Una vez que hayas clonado el repositorio, abre el cmd busca la siguiente ruta que contiene la carpeta con el archivo:
```src\view\GUI\NavalBattle-gui.py```

- ### **Ejecución de la Base de Datos en aplicación web**
Busca el archivo principal: Una vez que hayas clonado el repositorio, abre el cmd busca el siguiente archivo:
```naval_battle_web.py```

- **Librerías para la aplcación web:** Las librerías usadas para este desarrollo son "psycopg2" y "flask", para instalarlas ejecuta por consola: 
```pip install psycopg2```
```pip install flask```

Al correr el archivo principal, podrás obtener el link que deberás pegar en el explorador de tu preferencia para visualizar la aplicación web.
En la aplicación web podras elegir como quieras manipular las partidsa del juego:
- Insertar
- Buscar
- Eliminar
- Modificar



## ¿Cómo está hecho?

**Arquitectura del Proyecto:**

- **Clases y Excepciones Personalizadas:**

El proyecto define varias excepciones personalizadas para manejar errores específicos relacionados con la configuración y ejecución del juego, como NotEnoughSpace, BoardIsTooSmall, BoardIsTooBig, InvalidCoordinate, entre otras.

- *Clase Principal - NavalBattle:* Esta es la clase principal que gestiona toda la lógica del juego.

- *Ejecución Principal:* En el bloque if __name__ == "__main__":, el programa interactúa con el usuario para configurar el tamaño del tablero y la cantidad de barcos, y luego permite al jugador realizar disparos hasta que todos los barcos enemigos sean hundidos.

- *Bibliotecas Usadas:* random: Se utiliza para generar posiciones aleatorias para los barcos en el tablero.

- *Dependencias de Otros Proyectos:* No hay dependencias externas de otros proyectos o librerías adicionales más allá de las excepciones personalizadas y la biblioteca estándar random. Todo el juego está contenido dentro de una única clase y conjunto de excepciones personalizadas definidas en el mismo script.

**Organización de los Módulos:**
*Carpeta Principal: "NAVAL BATTLE"*

Contiene archivos y carpetas esenciales para el proyecto.

- ```.gitignore:``` Define qué archivos o carpetas deben ser ignorados por el sistema de control de versiones (Git).

- ```LICENSE:``` Contiene la licencia del proyecto, especificando los términos de uso, distribución y contribución.

- ```__init__.py:``` Permite que la carpeta se trate como un paquete Python, facilitando la importación de módulos internos.
- ```__pycache__:``` Carpeta generada automáticamente por Python para almacenar archivos compilados en bytecode (.pyc), lo que mejora la velocidad de carga de los módulos.

- ```SecretConfig_Sample.py:``` De este archivo deberas guiarte para la creación de tu archivo "SecretConfig.py" con tu información para la creación de tablas en la base de datos. 


## Estructura proyecto (MVC)

- **Carpeta src:**
Esta carpeta contiene el código fuente del proyecto, dividido en módulos organizados.
Subcarpetas:

1.*Model*

- **Logic:** Contiene la implementación principal del juego de Batalla Naval, incluyendo clases y lógica relacionadas con la gestión del tablero, la colocación de barcos, y las mecánicas del juego.

- **databaseconnection:** Se encarga de la lógica relacionada con la gestión de la conexión a la base de datos y la creación de nuevas partidas.

- **NavalBattleModel**: Contiene la lógica del menú que permite realizar operaciones relacionadas con la base de datos del juego.


2. *Controller:*

- **NavalBattleController.py:** Archivo que es el responsable de actuar como intermediario entre la lógica del juego y la interfaz de usuario (tanto consola como GUI)

- **CRUD:** Carpeta que contiene la lógical del manejo de Base de Datos (Insertas, Eliminar, Actualizar y Buscar)

3. *View:*

#### Console
- **Menu_Console_DB.py**: Contiene la lógica del menú que permite realizar operaciones relacionadas con la base de datos del juego.

- **NavalBattleConsole.py:** Contiene la lógica del juego interactuando con la consola.

#### GUI

- **NavalBattle-gui.py:** Contiene la lógica del juego interactuando en una interfaz gráfica de kivy


6. *tests*

- **NavalBattleTests.py:** Contiene los casos de prueba para la clase NavalBattle y sus métodos, probablemente utilizando un framework de pruebas como unittest o pytest.

- **Test_DB.py:** Contiene las pruebas relacionadas con las funcionalidades de la base de datos

7. *Templates*

Contiene los archivos html vinculados a flask para el desarrollo de la plicaión web.

## Uso de las Pruebas Unitarias 

Para ejecutar las pruebas unitarias desde el directorio raíz, ejecuta el archivo ```Test_DB.py``` con el siguiente comando:

- **Casos de prueba para el juego de batalla naval:**
```python tests\NavalBattle_test.py``` 

- **Casos de prueba de la base de datos:**
```python tests\DB_test.py```  


## Como hago funcionar la base de datos?

**Prerrequisitos:** Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso.

Luego, realiza los siguientes pasos

1. Duplica el archivo ``` Secret_Config-sample.py```  y renómbralo como ``` Secret_Config.py``` . Luego, configura los datos de conexión a tu base de datos dentro de este nuevo archivo.

2. Instala el paquete psycopg2 utilizando el siguiente comando:
```pip install psycopg2```
