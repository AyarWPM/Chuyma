# -*- coding: utf-8 -*-
#textoUnicode = u'\u0305\u2283'


class Elemento:
    '''Esta es la clase de los elementos, fenómenos o eventos lógicos
    e y anti-e por ejemplo.'''

    def __init__(self, nombre, abrev):
        '''Por defecto el estado de una nueva instancia es Actual. i.e.
        Contradicción potencial y no-contradicción actual (estadoC: falso)
        y por otro lado Actualización (estadoR verdadero)'''
        self.nombre = nombre
        self.abrev = abrev
        self.estadoC = False
        self.estadoR = True

    def esActual(self):
        self.estadoC = False
        self.estadoR = True

    def esPotencial(self):
        self.estadoC = False
        self.estadoR = False

    def esTercero(self):
        self.estadoC = True

    def cambiarEstado(self, nuevoEstado):
        if nuevoEstado == "A":
            self.esActual()
        if nuevoEstado == "P":
            self.esPotencial()
        if nuevoEstado == "T":
            self.esTercero()

    def infoElemento(self):
        return [self.nombre, self.abrev, [self.estadoC, self.estadoR]]

    def imprimirEstado(self):
        """Esta función es provisoria, solo para propósitos de debugging...
        la función imprimir será retrabajada."""
        if self.estadoC is True:
            print self.abrev + "(T)"
        else:
            if self.estadoR is True:
                print self.abrev + "(A)"
            else:
                print self.abrev + "(P)"