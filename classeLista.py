from classeCandidato import *
from classeBem import *
from classeControle import *

class No:
    def __init__(self, item=None, ante=None, prox=None):
        self.item = item
        self.ante = ante
        self.prox = prox

class ListaDupla:
    def __init__(self, contador = 0):
        self.cabeca = self.rabo = None
        self.contador = contador

    def __str__(self):
        elemento = self.cabeca
        string = ''
        while elemento != None:
            string += str(elemento.item) + ','
            elemento = elemento.prox
        return string[:len(string) - 1]

    def __repr__(self):
        return 'ListaDupla([' + self.__str__() + '])'

    def __getitem__(self, indice):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if cont == indice:
                return elemento.item
            else:
                elemento = elemento.prox
                cont += 1
        raise IndexError('list index out of range :( penah')

    def __setitem__(self, indice, novoItem):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if cont == indice:
                elemento.item = novoItem
                return
            else:
                elemento = elemento.prox
                cont += 1
        raise IndexError('list index out of range :( penah')

    def indice(self, valor):
        cont = 0
        elemento = self.cabeca
        while elemento != None:
            if valor == elemento.item:
                return cont
            else:
                elemento = elemento.prox
                cont +=1
        raise ValueError('this value can not be found. penah')

    def selecionar(self, indice=None):
        self.indice = indice
        aux = 0
        elemento = self.cabeca
        if self.indice != None and self.indice >= self.contador:
            raise IndexError('list index out of range :( penah')
        elif self.indice == None and self.contador == 0:
            raise IndexError('list index out of range :( penah')
        else:
            if self.contador == 1:
                antigoElemento = self.cabeca
                self.cabeca = self.rabo = None
                self.contador -= 1
                return antigoElemento.item

            elif self.indice == self.contador - 1 or self.indice == None:
                antigoRabo = self.rabo
                novoRabo = self.rabo.ante
                novoRabo.prox = None
                self.rabo = novoRabo
                self.contador -= 1
                return antigoRabo.item

            elif self.indice == 0:
                antigaCabeca = self.cabeca
                novaCabeca = self.cabeca.prox
                novaCabeca.ante = None
                self.cabeca = novaCabeca
                self.contador -= 1
                return antigaCabeca.item
            
            else:
                for x in range(0, self.contador - 1):
                    if self.indice == x:
                        elemento.ante.prox = elemento.prox
                        elemento.prox.ante = elemento.ante
                        self.contador -= 1
                        return elemento.item
                    else:
                        elemento = elemento.prox
                
    def anexar(self, initItem):
        self.item = initItem
        novoNo = No(self.item, None, None)
        if self.rabo == None:
            self.cabeca = novoNo
            self.rabo = novoNo
            self.contador += 1
        else:
            self.rabo.prox = novoNo
            novoNo.ante = self.rabo
            self.rabo = self.rabo.prox
            self.contador += 1

    def concatenar(self, initLista):
        self.lista = initLista
        for x in self.lista:
            self.anexar(x)
        #for x in range(0, len(self.lista) -1):
            #self.lista.selecionar()

    def comparar(self, objeto1, objeto2):
        if type(objeto1) != type(objeto2):
            raise TypeError
        if alfabeticamenteCrescente(objeto1, objeto2):
            return -1
        elif alfabeticamenteDecrescente(objeto1, objeto2):
            return 1
        return 0
        

    def vazio(self):
        return self.cabeca == self.rabo

    def inserirOrdenado(self, item):
        if self.vazio():
            self.cabeca = No(item, None, None)
            self.rabo = No(item, None, None)
            self.contador += 1
            return
        anterior = self.cabeca
        atual = self.cabeca.prox
        while atual is not None and self.comparar(atual.item, item) == -1:
            anterior = atual
            atual = anterior.prox
        anterior.prox = No(item, anterior, atual)
        self.contador += 1
        if atual is None:
            self.rabo = anterior.prox