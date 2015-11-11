# -*- coding: UTF-8 -*-
import sys
import os
import re
import constructores
import ecuaciones
import tabulador
import cPickle as pickle
from easygui import *


def iniciar():
    while 1:
        opc = menuBienvenida()
        if opc == "Abrir\narchivo":
            abrirArchivo = abrir()
            if abrirArchivo:
                ventanaPrincipal()
            else:
                pass
        elif opc == "Crear nueva tabla\nde deducciones":
            nuevoArchivo()
        else:
            sys.exit()


def menuBienvenida():
    msg = "Bienvenido a Chuyma, un programa para generar tablas de \
deducciones. Esta es una version beta, es decir una versión que cumple \
con su función general pero que aún contiene gran cantidad de bugs (errores de \
programación).\n\n\
LICENCIA\n\
========\n\
El programa tiene una licencia GPL (GNU General Public Licence), es decir que \
su código fuente está libremente disponible y cualquiera puede hacer uso de \
éste siempre y cuando comparta las modificaciones hechas en los mismos \
términos de la GPL.\n\n\
DATOS DEL PROGRAMA\n\
==================\n\
Nombre: Chuyma\n\
Autor: Ayar WPM\n\
Version: 1.0.2\n\
Código fuente: https://github.com/AyarWPM/Chuyma/\n\
Documentacion: https://github.com/AyarWPM/Chuyma/wiki"
    ttl = "Chuyma - Generador de tablas de deducciones"
    opciones = ["Abrir\narchivo", "Crear nueva tabla\nde deducciones"]
    return buttonbox(msg, ttl, image="logo.png", choices=opciones)


def abrir():
    msj = "Indicar la ubicación del archivo"
    ttl = "Abrir archivo"
    directorio = os.getcwd() + "/*.chuyma"
    direccion = enterbox(msj, ttl, directorio)
    try:
        if direccion:
            dicc = pickle.load(open(direccion, "rb"))
            for x in dicc:
                if re.match("elemento", x):
                    constructores.diccElem[x] = dicc[x]
                if re.match("ecuacion", x):
                    ecuaciones.diccEcu[x] = dicc[x]
            setattr(constructores.contador, "_Contador__cuentaPrivada",
                dicc["contador"])
            setattr(ecuaciones.contaEcu, "_Contador__cuentaPrivada",
                dicc["contaEcu"])
            return 1
        else:
            return None
    except:
        exceptionbox("""Algo no esta bien, no se puede abrir un archivo.\n
        Vuelve a intentarlo. Lo mas probable es que la direccion no exista.
        Si el error persiste, por favor copiar el mensaje que aparece en la
        ventana y enviarlo a ayarWPM@protonmail.com.""", "Error")
        iniciar()


def nuevoArchivo():
    msgbox("Paso 1 de 2\n===========\n\n\
El primer paso es definir un elemento, fenómeno o evento lógico \
cuyo significado es el de una implicación contradiccional a partir de la cual \
va a desarrollarse la Tabla de deducciones.\n\n\
En la siguiente ventana se le pedirá ingresar el nombre de este elemento, \
una abreviación (máximo 3 carácteres) y una descripción de dicho elemento. Por \
favor no utilizar acentos ni la letra ñ, el programa explotaría.",
        "Inicialización de una nueva Tabla")
    if "elemento1" in constructores.diccElem:
        msgbox("Ya ha definido un primer elemento. Se le dirigirá al paso 2. \
Si desea anular la creación de aquel elemento cierre el programa y ábralo \
nuevamente.")
        pass
    else:
        if crearElementos():
            print "Si ingresé datos"
            pass
        else:
            return
    msgbox("Paso 2 de 2\n===========\n\n\
A todo elemento, fenómeno o evento lógico le debe estar siempre \
asociado un anti-elemento, anti-fenómeno o anti-evento lógico de tal manera \
que su relación satisfasga el Postulado fundamental de la lógica de lo \
contradictorio.\n\n\
En la siguiente ventana se le pedirá definir este anti-elemento. Por \
favor no utilizar acentos ni la letra ñ, el programa explotaría.",
        "Inicialización de una nueva Tabla")
    if crearElementos():
        pass
    else:
        return
    primerNivel()
    msgbox("Felicidades!\n===========\n\n\
El primer elemento creado ha sido asociado según el Principio de Antagonismo \
al segundo elemento creado. Ya se ha generado el primer nivel de la tabla de \
deducciones, es decir se han generado automáticamente las tres implicaciones \
puras que relacionan ambos elementos en sus estados A-P, P-A y T-T \
respectivamente.", "Inicialización de una nueva Tabla")
    msgbox("Se le va a dirigir al menú principal.",
        "Inicialización de una nueva Tabla")
    ventanaPrincipal()


def ventanaPrincipal():
    while 1:
        opcMenu = menuPrincipal()
        if opcMenu == 0:
            mostrarElementos()
        elif opcMenu == 1:
            dibujarTabla()
        elif opcMenu == 2:
            guardar()
        elif opcMenu == 3:
            sys.exit()
        else:
            sys.exit()


def menuPrincipal():
    msj = "Menu principal\n==============\n\n\
- Ver elementos: Acá se enlistan los elementos creados. El usuario puede \
seleccionar un elemento y modificar sus datos (nombre, abreviacion o \
descripción) así como generar nuevas ramificaciones de la tabla de \
deducciones.\n\n\
- Ver la tabla de deducciones: Con esta opción se visualiza la Tabla de \
deducciones generada hasta el momento.\n\n\
- Guardar archivo: Puede guardar el archivo en su computadora para visualizar \
o modificar la tabla posteriormente.\n\n\
- Salir: Haga click aquí para salir del programa."
    ttl = "Chuyma - Nueva "
    opcs = ["Ver\nelementos", "Ver la tabla\nde deducciones",
        "Guardar\narchivo", "Salir"]
    return indexbox(msj, ttl, opcs)


def guardar():
    msj = "Indicar la ubicación del archivo"
    ttl = "Guardar archivo"
    direccion = os.getcwd() + "/*.chuyma"
    diccFinal = {}
    diccFinal.update(constructores.diccElem)
    diccFinal.update(ecuaciones.diccEcu)
    diccFinal["contador"] =\
    getattr(constructores.contador, "_Contador__cuentaPrivada")
    diccFinal["contaEcu"] =\
    getattr(ecuaciones.contaEcu, "_Contador__cuentaPrivada")
    try:
        direccion = enterbox(msj, ttl, direccion)
        if direccion is None:
            return
        pickle.dump(diccFinal, open(direccion, "wb"))
    except:
        exceptionbox("""Algo no esta bien, no se puede guardar el archivo.\n
        Vuelve a intentarlo. Lo mas probable es que la direccion no exista.
        Si el error persiste, por favor copiar el mensaje que aparece en la
        ventana y enviarlo a ayarWPM@protonmail.com.""", "Error")


def crearElementos():
    msj1 = "Por favor llene los datos del nuevo elemento."
    ttl1 = "Creación de nuevo elemento"
    campos = ["Nombre: ", "Abreviacion: ", "Descripción: "]
    resp = []
    resp = multenterbox(msj1, ttl1, campos)
    while 1:
        if resp is None:
            break
        msjErr = ""
        for i in range(len(campos)):
            if resp[i].strip() == "":
                msjErr = msjErr +\
                ('"%s" es un campo obligatorio.\n\n' % campos[i])
        if msjErr == "":
            break
        resp = multenterbox(msjErr, ttl1, campos, resp)
    if resp:
        return constructores.nuevoElem(resp[0], resp[1], resp[2])


def mostrarElementos():
    mensaje = "Los elementos creados están enlistados acá:"
    titulo = "Lista de elementos"
    while 1:
        seleccion1 = choicebox(mensaje, titulo, listaElem())
        if seleccion1:
            seleccion1 = nombreFiltrado(seleccion1)
            msj = detallesElem(seleccion1)
            ttl = 'Detalles de "' +\
            constructores.diccElem[seleccion1].nombre + '"'
            opciones = ["Modificar", "Registrar observacion\nestadistica",
                "Generar ramificacion", "Regresar"]
            seleccion2 = indexbox(msj, ttl, opciones)
            if seleccion2 == 0:
                modificarElemento(seleccion1)
            if seleccion2 == 1:
                registrarObservacion()
            if seleccion2 == 2:
                generarRama(seleccion1)
            if seleccion2 == 3:
                pass
        if seleccion1 is None:
            return


def modificarElemento(codElem):
    msj1 = "Modificar los datos del elemento."
    ttl1 = "Modificación de elemento existente"
    campos = ["Nombre: ", "Abreviacion: ", "Descripción: "]
    datos = [constructores.diccElem[codElem].nombre,
        constructores.diccElem[codElem].abrev,
        constructores.diccElem[codElem].descripcion]
    resp = []
    resp = multenterbox(msj1, ttl1, campos, datos)
    while 1:
        if resp is None:
            break
        msjErr = ""
        for i in range(len(campos)):
            if resp[i].strip() == "":
                msjErr = msjErr +\
                ('"%s" es un campo obligatorio.\n\n' % campos[i])
        if msjErr == "":
            break
        resp = multenterbox(msjErr, ttl1, campos, resp)
    if resp:
        setattr(constructores.diccElem[codElem], "nombre", resp[0])
        setattr(constructores.diccElem[codElem], "abrev", resp[1])
        setattr(constructores.diccElem[codElem], "descripcion", resp[2])


def primerNivel():
    for x in [1, 0, -1]:
        constructores.nuevaImpli(constructores.diccElem["elemento1"],
        constructores.diccElem["elemento2"], x)


def asignarAnti(codElem):
    """La diferencia entre asignarAnti y generarRama es que al primera función
    supone que los elementos no poseen antecedentes y consecuentes, en cambio
    la segunda va a hacer una copia de la primera implicación de tal manera
    que antecedente y consecuente sea el mismo en la implicacion y anti-.
    NOTA: ESTA FUNCIÓN YA NO ES UTILIZADA."""
    msj = "Seleccionar el anti-elemento que le es asociado."
    ttl = "Asignar anti-elemento"
    while 1:
        seleccion = choicebox(msj, ttl, listaElem())
        if seleccion:
            seleccion = nombreFiltrado(seleccion)
            if constructores.diccElem[seleccion].estadoC is None:
                if codElem != seleccion:
                    mensaje = "Implicaciones exitosamente creadas:\n\n"
                    for x in [1, 0, -1]:
                        nuevoEl = \
                        constructores.nuevaImpli(el(codElem), el(seleccion), x)
                        mensaje += nuevoEl.nombre +\
                        " Con orientación: " + str(x) + "\n"
                    mensaje += "\nNo olvidarse asignarles nuevos nombres, \
                    abreviaciones y descripciones."
                    titulo = "Elementos asociados"
                    msgbox(mensaje, titulo)
                    return
                else:
                    msgbox("Un elemento no puede asociarse consigo mismo.")
            else:
                msgbox("Este elemento ya está asociado a otro elemento.")
        if seleccion is None:
            msgbox("Regresando a la lista de elementos.",
                "Cancelado asignacion")
            return


def generarRama(implicacion):
    """Generar ramificación a partir de un elemento solamente si algunas
condiciones están satisfechas: tiene que ser una ecuacion (tener un
antecedente y consecuente) y no ser la raiz de una ramificacion (no pueden
haber dos ramas de una misma ecuacion)."""
    for x in ecuaciones.diccEcu:
        if ecuaciones.diccEcu[x].suElemento == implicacion:
            for y in ecuaciones.diccEcu:
                if ecuaciones.diccEcu[x].suElemento ==\
                ecuaciones.diccEcu[y].madre:
                    msgbox("No se puede generar una nueva ramificación a partir\
                    de este elemento.")
                    return
            constructores.nuevaRama(el(implicacion))
            break
    else:
        msgbox("No se puede generar una nueva ramificación a partir de \
este elemento.")


def dibujarTabla():
    msj = "Esta es la tabla de deducciones construida con los elementos de la \
base de datos del programa."
    ttl = "Tabla de deducciones"
    try:
        tabulador.creacionDeGrupos()
        laTabla = tabulador.tablaFinal()
        laTablaImpresa = laTabla.get_string()
        codebox(msj, ttl, laTablaImpresa)
    except:
        exceptionbox("Las ramificaciones no están bien formadas, no se puede \
generar la tabla de deducciones.\nPuede ayudar al desarrollo del programa \
enviando el mensaje que aparece en la ventana abajo a ayarWPM@protonmail.com",
"Error")


def el(codElem):
    "Esta función devuelve el objeto elemento a partir de su nombre en diccElem"
    return constructores.diccElem[codElem]


def laLlave(objElemento):
    """Esta función es la inversa de el(), recibe un objeto y devuelve su nombre
    en diccElem"""
    for z in constructores.diccElem:
        if constructores.diccElem[z] == objElemento:
            return z


def nombreFiltrado(texto):
    texto = re.match("elemento[0-9]*", texto)
    return texto.group()


def listaElem():
    """La función devuelve una lista de los elementos: elemento1:
        nombre (abrev) - descr"""
    lista = []
    for x in range(len(constructores.diccElem)):
        lista.append("elemento" + str(x + 1) + " : " +
        constructores.diccElem["elemento" + str(x + 1)].nombre +
        " (" + constructores.diccElem["elemento" + str(x + 1)].abrev + ") - " +
        constructores.diccElem["elemento" + str(x + 1)].descripcion)
    return lista


def detallesElem(codElem):
    detalles = ""
    for x in constructores.diccElem[codElem].__dict__:
        if x == "antecedente" and\
        (constructores.diccElem[codElem].antecedente is not None):
            detalles += str(x) + ": " +\
            str(constructores.diccElem[codElem].__dict__[x].nombre) + "\n"
        elif x == "consecuente" and\
        (constructores.diccElem[codElem].consecuente is not None):
            detalles += str(x) + ": " +\
            str(constructores.diccElem[codElem].__dict__[x].nombre) + "\n"
        else:
            detalles += str(x) + ": " +\
            str(constructores.diccElem[codElem].__dict__[x]) + "\n"
    return detalles


def registrarObservacion():
    ttl = "Ventana para registrar observaciones estadísticas."
    msj = "Esta ventana es un demostración de cómo se utilizará el programa \
para registrar datos."
    campos = ["Configuracion espacial (¿donde?): ", "Configuracion temporal \
(¿cuando?", "Criterio positivo 1: ", "Criterio negativo 1: ", "Valoracion \
de criterio 1: ", "Criterio positivo 2: ", "etc."]
    return multenterbox(msj, ttl, campos)