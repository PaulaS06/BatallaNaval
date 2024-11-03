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

- **Librerías:** Las únicas librerías usadas para este desarrollo son "random" y "kivy", "random" está incluida por defecto en pyhon; debes instalar "kivy" para poder correr la aplicación desde una interfaz gráfica.

- **Código del Juego:** Asegúrate de tener todos los archivos necesarios del proyecto en una carpeta organizada.

- **Ejecución del juego en consola:**
Navega a la carpeta: Una vez que hayas clonado el archivo, abre el cmd y navega a la carpeta en la que guardaste el archivo, por ejemplo:
```C:\Users\durre\Documentos\Universidad\Semestre4\CodigoLimpio\NavalBattleGame```

**Ejecuta el script main:**
```python src\Console\NavalBattleConsole.py```


### **Ejecución del juego en interfaz gráfica de kivy**

- **Navega a la carpeta:** Una vez que hayas clonado el archivo, abre el cmd y navega a la carpeta en la que guardaste el archivo, por ejemplo:
```C:\Users\durre\Documentos\Universidad\Semestre4\CodigoLimpio\NavalBattleGame```

- **Ejecuta el script main:**
```python src\NavalBattleGui\NavalBattle-gui.py```

- **Instrucciones en Pantalla:** 
Una vez ejecutado, sigue las instrucciones que aparecerán en la consola para jugar. El juego interactuará contigo a través de mensajes de texto y comandos de teclado. 

## ¿Cómo está hecho?

**Arquitectura del Proyecto:**

- **Clases y Excepciones Personalizadas:**

El proyecto define varias excepciones personalizadas para manejar errores específicos relacionados con la configuración y ejecución del juego, como NotEnoughSpace, BoardIsTooSmall, BoardIsTooBig, InvalidCoordinate, entre otras.

- *Clase Principal - NavalBattle:* Esta es la clase principal que gestiona toda la lógica del juego.

- *Ejecución Principal:* En el bloque if __name__ == "__main__":, el programa interactúa con el usuario para configurar el tamaño del tablero y la cantidad de barcos, y luego permite al jugador realizar disparos hasta que todos los barcos enemigos sean hundidos.

- *Bibliotecas Usadas:* random: Se utiliza para generar posiciones aleatorias para los barcos en el tablero.

- *Dependencias de Otros Proyectos:* No hay dependencias externas de otros proyectos o librerías adicionales más allá de las excepciones personalizadas y la biblioteca estándar random. Todo el juego está contenido dentro de una única clase y conjunto de excepciones personalizadas definidas en el mismo script.

- **Organización de los Módulos:**
*Carpeta Principal: "NAVAL BATTLE GAME"*

Contiene archivos y carpetas esenciales para el proyecto.

- ```.gitignore:``` Define qué archivos o carpetas deben ser ignorados por el sistema de control de versiones (Git).

- ```LICENSE:``` Contiene la licencia del proyecto, especificando los términos de uso, distribución y contribución.

- ```__init__.py:``` Permite que la carpeta se trate como un paquete Python, facilitando la importación de módulos internos.
- ```__pycache__:``` Carpeta generada automáticamente por Python para almacenar archivos compilados en bytecode (.pyc), lo que mejora la velocidad de carga de los módulos.


## Estructura sugerida

- **Carpeta src:**
Esta carpeta contiene el código fuente del proyecto, dividido en módulos organizados.
Subcarpetas:

1.*Console*

- **Functions_DB.py:** Este archivo incluye funciones relacionadas con la base de datos del juego, como la creación o modificación de registros.

- **Crear_partida.py:** Se encarga de gestionar la creación de nuevas partidas

- **Menu_Console_DB.py**: Contiene la lógica del menú que permite realizar operaciones relacionadas con la base de datos del juego.

- **NavalBattleConsole.py:** Contiene la lógica del juego interactuando con la consola.

2. *Controller:*

- **NavalBattleController.py:** Archivo que es el responsable de actuar como intermediario entre la lógica del juego y la interfaz de usuario (tanto consola como GUI)

3. *Model:*

- **NavalBattleModel.py:** Contiene el modelo del juego

4. *NavalBattleGui*

- **NavalBattle-gui.py:** Contiene la lógica del juego interactuando en una interfaz gráfica de kivy

5. *Program*

- **NavalBattle.py:** Contiene la implementación principal del juego de Batalla Naval, incluyendo clases y lógica relacionadas con la gestión del tablero, la colocación de barcos, y las mecánicas del juego.

6. *tests*

- **NavalBattleTests.py:** Contiene los casos de prueba para la clase NavalBattle y sus métodos, probablemente utilizando un framework de pruebas como unittest o pytest.

- **Test_DB.py:** Contiene las pruebas relacionadas con las funcionalidades de la base de datos

## Uso de las Pruebas Unitarias 

Para ejecutar las pruebas unitarias desde el directorio raíz, ejecuta el archivo ```Test_DB.py``` con el siguiente comando:

- **Casos de prueba para el juego de batalla naval:**
```python tests/NavalBattleTests.py``` 

- **Casos de prueba de la base de datos:**
```python tests/Test_DB.py```  

## Como hago funcionar la base de datos?

**Prerrequisitos:** Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso.

Luego, realiza los siguientes pasos

1. Duplica el archivo ``` Secret_Config-sample.py```  y renómbralo como ``` Secret_Config.py``` . Luego, configura los datos de conexión a tu base de datos dentro de este nuevo archivo.

2. Instala el paquete psycopg2 utilizando el siguiente comando:
```pip install psycopg2```



`
