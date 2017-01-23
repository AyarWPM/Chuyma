#Chuyma
![Chuyma](https://github.com/AyarWPM/Chuyma/blob/master/logo.png?raw=true)

Chuyma es un programa que genera Tablas de deducciones de la lógica de lo contradictorio.

31/01/2017
¡Atención! Este proyecto ha sido rebautizado Amuyaña porque he reescrito completamente el programa en java y cambiado la lógica de las clases.

#INSTALACIÓN

##Windows y linux
El programa se ejecuta sin instalación ya que se trata de un simple script. Los binarios para Windows y Linux se encuentran en sourceforge: http://chuyma.sourceforge.net/

[Descargar la última version para Windows (V.1.0.2)](http://sourceforge.net/projects/chuyma/files/Windows/chuyma_v.1.0.2.exe/download)

[Descargar la última version para Linux (V.1.0.2)](http://sourceforge.net/projects/chuyma/files/Linux/chuyma_v.1.0.2/download)

Lo siento pero no he generado los binarios para Mac OS. Los usuarios de Mac OS pueden ejecutar directamente el código fuente, ver abajo.

##Ejecución desde la fuente
El código fuente que se encuentra en el repositorio de github (https://github.com/AyarWPM/Chuyma/) ha sido desarrollado con python v.2.7.9. Para "ejecutarlo" necesita tener instalado:

* Python 2.7.9 (no se hizo la prueba con ninguna otra versión)

Además de los módulos para python que he instalado utilizando python-pip:

* easygui
* PrettyTable
* pickle

Luego basta con ejecutar el archivo 'chuyma.py' con python, por ejemplo en Linux he hecho:

$ python chuyma.py

#¿QUE HACE EL PROGRAMA?
El programa permite definir eventos lógicos en el sentido de la lógica de Stéphane Lupasco, es decir fenómenos, elementos o eventos lógicos que satisfacen el Principio de antagonismo. La lógica de Lupasco es una lógica ternaria, es decir que representa las cosas por tres valores y no solo dos como el verdadero y falso. Entonces Chuyma nos permite construir esos elementos de esta lógica (llamada lógica de lo contradictorio) por medio de la generación de la Tabla de deducciones.

Actualmente el proyecto Chuyma está construido con una interfaz gráfica simple únicamene con el objetivo de demostrar de que manera puede utilizarse la generación de Tablas de deducciones. Por ejemplo un proyect posterior será el de aplicar el código generador de estas tablas a un programa específico para dinamizar una economía de reciprocidad.

#DOCUMENTACIÓN
Toda la documentación relativa al funcionamiento del programa y a su fundamento teórico se encuentra albergado en esta dirección: [http://www.transbordered.cf](http://www.transbordered.cf)

#NOVEDADES

##VERSION 1.0.2 (11/11/2015)
En la impresión de la Tabla de deducciones se utilizan subíndices a, p y t (y ya no _A, _P, _T).

##VERSION 1.0.1 (9/11/2015)
Corrección de bugs.

Se ha aumentado una opción de demostración de la manera en la que se desarrollara el registro de datos estadísticos.

##VERSION 1.0 (25/10/2015)
Posee una interfaz gráfica capaz de diseñar la Tabla de deducciones.

Bugs conocidos: Si se generan dos ramificaciones a partir de un solo elemento el programa no puede generar la Tabla de deducciones.

#CONSIDERACIONES
Para el desarrollo del código fuente he utilizado tres módulos de python además de los que ya venían integrados: easygui (para la interfaz visual), PrettyTable (para la constucción de la tabla de deduccioens) y pickle (para guardar y abrir la base de datos). Sin esos módulos no habría tenido ni la mas remota idea de como desarrollar el programa, por lo menos tal y cual lo tenía en mente.

Para el logo he utilizado el emblema del famoso Chapulín Colorado albergado en wikimedia: https://commons.wikimedia.org/wiki/File:El_Chapul%C3%ADn_Colorado_logo.svg

#SOBRE EL AUTOR
El autor es Ayar WPM, un economista que trabaja sobre temas relacionados a la lógica formal empleada en los razonamientos económicos y la formalización de la economía de reciprocidad. Contacto: ayarWPM@protonmail.com
