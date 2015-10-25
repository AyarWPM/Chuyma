# -*- coding: utf-8 -*-

import copy
import elementos


class Contador:
    __cuentaPrivada = 0

    def cuenta(self):
        self.__cuentaPrivada += 1
        return self.__cuentaPrivada

diccElem = {}
contador = Contador()


def nuevoElem():
    diccElem["elemento" + str(contador.cuenta())] =\
    elementos.Elemento("Nuevo nombre", "Nueva abreviación")
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
    elementos.Elemento("Nuevo nombre", "Nueva abreviación")
    if orientacion == 1:
        diccElem["elemento" +
        str(getattr(contador, "_Contador__cuentaPrivada"))].\
        relaciona(elem, antiElem, orientacion)
    elif orientacion == -1:
        diccElem["elemento" +
        str(getattr(contador, "_Contador__cuentaPrivada"))].\
        relaciona(antiElem, elem, orientacion)
    elif orientacion == 0:
        diccElem["elemento" +
        str(getattr(contador, "_Contador__cuentaPrivada"))].\
        relaciona(elem, antiElem, orientacion)
    return diccElem["elemento" +
    str(getattr(contador, "_Contador__cuentaPrivada"))]


def nuevaRama(impliPura):
    for i in [1, -1, 0]:
        diccElem["elemento" + str(contador.cuenta())] = copy.copy(impliPura)
        tempCuenta = getattr(contador, "_Contador__cuentaPrivada")
        setattr(diccElem["elemento" + str(tempCuenta)], "orientacion", i)
        setattr(diccElem["elemento" + str(tempCuenta)], "padre", impliPura)
        crearAnti(diccElem["elemento" + str(tempCuenta)])
        if i == 1:
            nuevaImpli(diccElem["elemento" + str(tempCuenta)],
            diccElem["elemento" + str(tempCuenta + 1)], i)
        elif i == -1:
            nuevaImpli(diccElem["elemento" + str(tempCuenta + 1)],
            diccElem["elemento" + str(tempCuenta)], i)
        elif i == 0:
            nuevaImpli(diccElem["elemento" + str(tempCuenta)],
            diccElem["elemento" + str(tempCuenta + 1)], i)


def corregirEstado(el1, el2):
    if (el1.estadoC is True) and (el2.estadoC is False):
        el2.esTercero()
    if ((el1.estadoC is False) and (el2.estadoC is False)) or\
    ((el1.estadoC is False) and (el2.estadoC is True)):
        if (el1.estadoR is True) and (el2.estadoR is True):
            el2.esPotencial()
        if (el1.estadoR is False) and (el2.estadoR is False):
            el2.esActual()