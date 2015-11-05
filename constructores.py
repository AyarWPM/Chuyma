# -*- coding: utf-8 -*-
import copy
import elementos
import ecuaciones


class Contador:
    __cuentaPrivada = 0

    def cuenta(self):
        self.__cuentaPrivada += 1
        return self.__cuentaPrivada

diccElem = {}
contador = Contador()


def nuevoElem(nombre, abrev, desc):
    diccElem["elemento" + str(contador.cuenta())] =\
    elementos.Elemento(nombre, abrev, desc)
    return diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))]


def crearAnti(elem):
    diccElem["elemento" + str(contador.cuenta())] = copy.copy(elem)
    setattr(diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))],
    "nombre", "anti-" + str(elem.nombre))
    corregirEstado(elem, diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))])
    return diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))]


def nuevaImpli(elem, antiElem, orientacion):
    diccElem["elemento" + str(contador.cuenta())] =\
    elementos.Elemento("Nuevo elemento " +
    str(getattr(contador, "_Contador__cuentaPrivada") + 1),
    "X", "Descripcion vacia.")
    diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))].\
    relaciona(elem, antiElem, orientacion)

    ecuaciones.nuevaEcuacion("elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada")), laLlave(elem))

    return diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))]


def nuevaRama(impliPura):
    antiImpliPura = crearAnti(impliPura)
    for i in [1, 0, -1]:
        nuevaImpli(impliPura, antiImpliPura, i)


def corregirEstado(el1, el2):
    if (el1.estadoC is True) and (el2.estadoC is False):
        el2.esTercero()
    if ((el1.estadoC is False) and (el2.estadoC is False)) or\
    ((el1.estadoC is False) and (el2.estadoC is True)):
        if (el1.estadoR is True) and (el2.estadoR is True):
            el2.esPotencial()
        if (el1.estadoR is False) and (el2.estadoR is False):
            el2.esActual()


def laLlave(objElemento):
    for z in diccElem:
        if diccElem[z] == objElemento:
            return z
