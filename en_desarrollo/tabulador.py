#-*- coding:utf-8 -*-
import constructores
import ecuaciones
from prettytable import PrettyTable


class GrupoYaExiste(RuntimeError):
    pass


class Trio(PrettyTable):

    def __init__(self, origenEcu):
        """Componentes 1,2 y 3 son los nombres de las ecuaciones que
        componen la instancia (ej: ecuacion1, ecuacion2 y ecuacion3).
        nivel es el nivel de la tabla de deducciones en el que se
        encuentra. Origen es el nombre de la ecuacion de la cual provienen
        y deduccion es un vector indicando la orientacion del origen, ej.
        si origen es una ecuacion de orientacion T deduccion = [0, 1, 0]"""
        PrettyTable.__init__(self)
        self.header = False
        self.nivel = None
        self.deduccion = None
        self.componentes = []
        self.origenEcu = origenEcu
        self.creacion(self.origenEcu)
        self.cualDeduccion()
        self.cualNivel(self.componentes)

    def creacion(self, origenEcu):
        orientaciones = [1, 0, -1]
        compo = []
        for ori in orientaciones:
            for eq in ecuaciones.diccEcu:
                if (ecuaciones.diccEcu[eq].madre ==
                ecuaciones.diccEcu[origenEcu].suElemento) and\
                (constructores.diccElem[ecuaciones.diccEcu[eq].suElemento].
                orientacion == ori):
                    self.add_row([ecuaciones.diccEcu[eq].ecuacion])
                    compo.append(eq)
        self.componentes = compo
        if len(self.componentes) < 3:
            raise GrupoYaExiste()
        return self

    def cualDeduccion(self):
        dedu = [""] * 3
        if constructores.diccElem[ecuaciones.diccEcu[self.origenEcu].
        suElemento].orientacion == 1:
            dedu[0] = 1
        elif constructores.diccElem[ecuaciones.diccEcu[self.origenEcu].
        suElemento].orientacion == 0:
            dedu[1] = 1
        elif constructores.diccElem[ecuaciones.diccEcu[self.origenEcu].
        suElemento].orientacion == -1:
            dedu[2] = 1
        self.deduccion = dedu

    def cualNivel(self, componentes):
        ecuacion = componentes[0]
        n = 1
        while 1:
            if constructores.diccElem[ecuaciones.diccEcu[ecuacion].madre].\
            antecedente:
                for ecu in ecuaciones.diccEcu:
                    if ecuaciones.diccEcu[ecu].suElemento ==\
                    ecuaciones.diccEcu[ecuacion].madre:
                        ecuacion = ecu
                        n += 1
            else:
                break
        self.nivel = n

    def laLlave(self, objElemento):
        for z in constructores.diccElem:
            if constructores.diccElem[z] == objElemento:
                return z


def creacionDeGrupos():
    n = 1
    gruposTrios = {}
    for ecuacion in ecuaciones.diccEcu:
        if ecuaciones.diccEcu[ecuacion].nivelDeductivo < nMax():
            try:
                gruposTrios["grupo" + str(n)] = Trio(ecuacion)
                n += 1
            except GrupoYaExiste:
                pass
    return gruposTrios


def nMax():
    niveles = []
    for x in ecuaciones.diccEcu:
        niveles.append(ecuaciones.diccEcu[x].nivelDeductivo)
    f = (lambda x, y: x if (x > y) else y)
    valor = reduce(f, niveles)
    return valor


def creaListaDedu(tabla):
    lista = [""] * 3
    for tabla2 in tablasTrio:
        if tablasTrio[tabla2].nivel == (tablasTrio[tabla].nivel + 1):
            if tablasTrio[tabla2].origenEcu in tablasTrio[tabla].componentes:
                #añadir tabla2 en una lista de tres elementos con índice
                #igual a su deduccion
                for i in range(3):
                    if tablasTrio[tabla2].deduccion[i] == 1:
                        lista[i] = tablasTrio[tabla2]
    return lista


def tablaFinal():
    global tablasTrio
    tablasTrio = creacionDeGrupos()
    for cadaTabla in tablasTrio:
        tablasTrio[cadaTabla].add_column("", creaListaDedu(cadaTabla))

    tablaInicial = PrettyTable()
    tablaInicial.header = False

    for ori in [1, 0, -1]:
        for x in ecuaciones.diccEcu:
            if ecuaciones.diccEcu[x].madre == "elemento1":
                if constructores.diccElem[ecuaciones.diccEcu[x].suElemento].\
                orientacion == ori:
                    tablaInicial.add_row([ecuaciones.diccEcu[x].ecuacion])

    columnaInicial = [""] * 3
    for tabla in tablasTrio:
        if tablasTrio[tabla].nivel == 2:
            for j in range(3):
                if tablasTrio[tabla].deduccion[j] == 1:
                    columnaInicial[j] = tablasTrio[tabla]

    tablaInicial.add_column("", columnaInicial)

    tablaInicial.valign["Field 1"] = "m"
    tablaInicial.align = "l"

    for tabla in tablasTrio:
        tablasTrio[tabla].valign["Field 1"] = "m"
        tablasTrio[tabla].align = "l"

    return tablaInicial