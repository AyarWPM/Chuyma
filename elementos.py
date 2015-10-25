# -*- coding: utf-8 -*-
#textoUnicode = u'\u0305\u2283'


class Elemento:
    '''Esta es la clase de los elementos, fenómenos o eventos lógicos
    e y anti-e por ejemplo.'''

    def __init__(self, nombre, abrev, descripcion=""):
        '''Por defecto el estado de una nueva instancia es Actual. i.e.
        Contradicción potencial y no-contradicción actual (estadoC: falso)
        y por otro lado Actualización (estadoR verdadero)'''
        self.nombre = nombre
        self.abrev = abrev
        self.descripcion = descripcion
        self.estadoC = None
        self.estadoR = None
        self.orientacion = None
        self.padre = None

    def esActual(self):
        self.estadoC = False
        self.estadoR = True

    def esPotencial(self):
        self.estadoC = False
        self.estadoR = False

    def esTercero(self):
        self.estadoC = True

    def relaciona(self, el1, el2, dedu):
        if dedu == 1:
            el1.esActual()
            el2.esPotencial()
            self.orden(el1, el2)
            self.orientacion = dedu
        elif dedu == -1:
            el1.esPotencial()
            el2.esActual()
            self.orden(el2, el1)
            self.orientacion = dedu
        elif dedu == 0:
            el1.esTercero()
            el2.esTercero()
            self.orden(el1, el2)
            self.orientacion = dedu

    def orden(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente