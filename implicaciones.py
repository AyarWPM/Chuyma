# -*- coding: utf-8 -*-
#Como científicos comenzamos observando nuestro entorno, nos preguntamos sobre
#los fenómenos que se producen en la naturaleza, entre nosotros y la naturaleza
#o entrelos elementos de la naturaleza. Con la lógica de lo no-contradictorio
#podemos abstraer la relación que existe entre los elementos y declarar su
#existencia tautológica, sin necesidad de relativizar su identificación,
#"existen por sí mismos". En cambio con la lógica de lo contradictorio tenemos
#que ir identificando las cadenas deductivas a las cuales pertenecen e ir
#definiendo aquellos fenómenos como dinamismos congelados.

#Por lo tanto, lo primero que definimos es un elemento que luego lo "transf_
#formamos" en un dinamismo (una operación pura) y tratamos de darle su lugar
#en el sistema deductivo...

import elementos


class Implicacion(elementos.Elemento):

    """Una Implicacion es un Elemento que posee otros dos atributos: un elemento
    antecedente (ant) y otro consecuente (con): ant Elemento con. De ahí que
    heredamos las calidades de la clase Elemento. Antecedente y Consecuente
    ya deben existir..."""
    def __init__(self, nombre, abrev):
        "Descripcion"
        self.nombre = nombre
        self.abrev = abrev
        self.estadoC = True
        self.estadoR = True
        self.estado = [self.estadoC, self.estadoR]

    def relaciona(self, ant, con):
        self.correctorEstados(ant, con)
        self.antecedente = ant
        self.consecuente = con

    def correctorEstados(self, el1, el2):
        '''Si el1(A) => el2(P), si el1(P) => el2(A), si el1(T) => el2(T). El
        primer argumento -el1- tiene la prioridad.'''
        if (el1.estadoC is True) and (el2.estadoC is False):
            el2.cambiarEstado("T")
        elif (el1.estadoC is False) and (el2.estadoC is True):
            el2.cambiarEstado("T")
        elif (el1.estadoC is False) and (el2.estadoC is False):
            if (el1.estadoR is True) and (el2.estadoR is True):
                el2.cambiarEstado("P")
            if (el1.estadoR is False) and (el2.estadoR is False):
                el2.cambiarEstado("A")

    def cambiarAntecedente(self, nuevoAnt):
        self.antecedente = nuevoAnt
        self.correctorEstados(nuevoAnt, self.consecuente)

    def cambiarConsecuente(self, nuevoCon):
        self.consecuente = nuevoCon
        self.correctorEstados(self.antecedente, nuevoCon)

    def infoElemento(self):
        return [self.nombre, self.abrev, [self.estadoC, self.estadoR],
        [getattr(self.antecedente, "nombre"),
        getattr(self.consecuente, "nombre")]]