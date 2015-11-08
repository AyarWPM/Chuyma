#-*- coding:utf-8 -*-
import constructores
import re


class Contador:
    __cuentaPrivada = 0

    def cuenta(self):
        self.__cuentaPrivada += 1
        return self.__cuentaPrivada

diccEcu = {}
contaEcu = Contador()


class Ecuacion:

    def __init__(self, suElemento, madre):
        self.suElemento = suElemento
        self.madre = madre
        self.ecuacion =\
        self.laTabla(self.expansion(constructores.diccElem[suElemento]))

    def sim(self, elemento, signoA):
        if signoA == 1:
            if (getattr(elemento, "estadoC") is False) and\
            (getattr(elemento, "estadoR") is True):
                return u' \u2283' + '[' + elemento.abrev + u']_A'
            elif (getattr(elemento, "estadoC") is False) and\
            (getattr(elemento, "estadoR") is False):
                return u' \u2283' + '[' + elemento.abrev + u']_P'
            elif (getattr(elemento, "estadoC") is True):
                return u' \u2283' + '[' + elemento.abrev + u']_T'
        elif signoA == 0:
            if (getattr(elemento, "estadoC") is False) and\
            (getattr(elemento, "estadoR") is True):
                return u' \u0305\u2283' + '[' + elemento.abrev + u']_A'
            elif (getattr(elemento, "estadoC") is False) and\
            (getattr(elemento, "estadoR") is False):
                return u' \u0305\u2283' + '[' + elemento.abrev + u']_P'
            elif (getattr(elemento, "estadoC") is True):
                return u' \u0305\u2283' + '[' + elemento.abrev + u']_T'

    def simPuro(self):
        return u' \u2283 '

    def laLlave(self, objElemento):
        for z in constructores.diccElem:
            if constructores.diccElem[z] == objElemento:
                return z

    def nivel(self, elemento):
        n = {}
        for x in constructores.diccElem:
            i = 0
            y = x
            while 1:
                if constructores.diccElem[x].consecuente:
                    x = self.laLlave(constructores.diccElem[x].consecuente)
                    i += 1
                else:
                    break
            n[y] = i
        return n[self.laLlave(elemento)]

    def numImpl(self, nivel):
        """Devuelve el número de implicaciones (signos de implicación o anti-
        implicación) que aparecen en una línea"""
        n = 0
        val = 1
        while n < nivel:
            val = val * 2 + 1
            n += 1
        return val

    def expansion(self, elemento):
        n = self.nivel(elemento)
        self.nivelDeductivo = n
        casillas = self.numImpl(n)
        enLista = [1] * casillas
        enLista[((casillas - 1) / 2)] = self.simPuro()
        posInicial = 0
        for i in range(n):
            if i == 0:
                posInicial = 0
            elif i == 1:
                posInicial = 1
            elif i > 1:
                posInicial = posInicial + 2 ** (i - 1)
            recurrencia = 2 ** (i + 1)
            ind = 1
            for j in range(posInicial, len(enLista), recurrencia):
                losDos = self.determinaElem(elemento, n - i)
                if losDos[2] == 1:
                    if ind % 2 == 1:
                        enLista[j] = self.sim(losDos[0], 1)
                    elif ind % 2 == 0:
                        enLista[j] = self.sim(losDos[1], 0)
                if losDos[2] == 0:
                    if ind % 2 == 1:
                        enLista[j] = self.sim(losDos[0], 0)
                    elif ind % 2 == 0:
                        enLista[j] = self.sim(losDos[1], 1)
                ind += 1
        return enLista

    def determinaElem(self, elemento, grado):
        """Corrige los estados de los elementos (A, P o T) y devuelve ant, cons
        y un indicador de si se trata implicacion o exclusion"""
        g = 0
        elementos = []
        while g < grado:
            preElem = elemento
            elemento = elemento.antecedente
            g += 1
        if preElem.orientacion == 1:
            preElem.antecedente.esActual()
            preElem.consecuente.esPotencial()
            signoA = 1
        elif preElem.orientacion == -1:
            preElem.antecedente.esActual()
            preElem.consecuente.esPotencial()
            signoA = 0
        elif preElem.orientacion == 0:
            preElem.antecedente.esTercero()
            preElem.consecuente.esTercero()
            signoA = 1
        elementos.append(preElem.antecedente)
        elementos.append(preElem.consecuente)
        elementos.append(signoA)
        return elementos

    def laPreTabla(self, lista):
        i = "("
        d = ")"
        x = "x"
        largo3 = [i, x, x, x, d]
        largo7 = largo3 + [x] + largo3
        laLista = []
        if len(lista) == 3:
            return largo3
        if len(lista) == 7:
            return largo7
        if len(lista) > 7:
            laLista = largo7
            while len(laLista) < (len(lista) * 2) - 3:
                laLista = [i] + laLista + [d, x, i] + laLista + [d]
            return laLista

    def laTabla(self, lista):
        preTabla = self.laPreTabla(lista)
        z = 0
        for l in range(len(preTabla)):
            if preTabla[l] == "x":
                preTabla[l] = lista[z]
                z += 1
        laTabla = "".join(preTabla)
        laTabla = re.sub(r'\(\s', r'(', laTabla)
        laTabla = re.sub(r'  ', r' ', laTabla)
        laTabla = re.sub(r'(?P<exp>[APT])\(', r'\1 (', laTabla)
        return laTabla


def nuevaEcuacion(elElem, madre):
    diccEcu["ecuacion" + str(contaEcu.cuenta())] =\
    Ecuacion(elElem, madre)
    return diccEcu["ecuacion" +
    str(getattr(contaEcu, "_Contador__cuentaPrivada"))]