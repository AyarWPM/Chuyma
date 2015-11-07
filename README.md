# Chuyma

Chuyma es un programa que genera Tablas de deducciones de la lógica de lo contradictorio.

INSTALACIÓN
===========
- Windows y linux

El programa se ejecuta sin instalación ya que se trata de un simple script. Los binarios para Windows y Linux se encuentran en sourceforge: http://chuyma.sourceforge.net/

Windows: http://sourceforge.net/projects/chuyma/files/Windows/chuyma.exe/download

Linux: http://sourceforge.net/projects/chuyma/files/Linux/chuyma/download

- Instalación desde la fuente

El código fuente que se encuentra en el repositorio de github (https://github.com/AyarWPM/Chuyma/) ha sido desarrollado con python v.2.7.9. Para "instalarlo" tendrá que descargarlo y utilizar algún utilitario para "congelar" el código python, por ejemplo pyinstaller o py2exe.

¿QUE HACE EL PROGRAMA?
=====================
El programa permite definir eventos lógicos en el sentido de la lógica de Stéphane Lupasco, es decir fenómenos, elementos o eventos lógicos que satisfacen el Principio de antagonismo. La lógica de Lupasco es una lógica ternaria, es decir que representa las cosas por tres valores y no solo dos como el verdadero y falso. Entonces Chuyma nos permite construir esos elementos de esta lógica (llamada lógica de lo contradictorio) por medio de la generación de la Tabla de deducciones.

NOVEDADES
=========
VERSION 1.0.
Posee una interfaz gráfica capaz de diseñar la Tabla de deducciones.
Bugs conocidos: Si se generan dos ramificaciones a partir de un solo elemento el programa no puede generar la Tabla de deducciones.

CONSIDERACIONES
===============
Para el desarrollo del código fuente he utilizado tres módulos de python además de los que ya venían integrados: easygui (para la interfaz visual), PrettyTable (para la constucción de la tabla de deduccioens) y pickle (para guardar y abrir la base de datos). Sin esos módulos no habría tenido ni la mas remota idea de como desarrollar el programa, por lo menos tal y cual lo tenía en mente.

Para el logo he utilizado el emblema del famoso Chapulín Colorado albergado en wikimedia: https://commons.wikimedia.org/wiki/File:El_Chapul%C3%ADn_Colorado_logo.svg

CONTACTO Y SUGERENCIAS
======================
Contacto: ayarWPM@protonmail.com


