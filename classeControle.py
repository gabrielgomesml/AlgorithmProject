from classeCandidato import *
from classeBem import *
from classeLista import *

class Controle:
    def __init__(self, arquivo, arquivoBens):
        self.arquivoBens = arquivoBens
        self.arquivo = arquivo
        self.candidatos = ListaDupla()
        self.bens = {}

    def lerArquivo(self, arquivo):
        arq = open(arquivo, 'r')
        linhas = arq.readlines()
        arq.close()
        return linhas

    def carregar(self):
        self.carregarBens(self.arquivoBens)
        self.carregarCandidatos(self.arquivo)

    def carregarCandidatos(self, arquivo):
        #dados = self.lerArquivo(arquivo)
        palavra = ''
        lista = ListaDupla()
        for n in open(self.arquivo, 'r'):
            for x in n:
                if x != ';':
                    palavra += x
                else:
                    lista.anexar(palavra[1:len(palavra)-1])
                    palavra = ''
            if lista[15] in self.bens:
                self.candidatos.inserirOrdenado(Candidato(lista[2], lista[10], lista[13], lista[14], lista[17], lista[15], lista[16], lista[20], lista[18], lista[27], lista[28], lista[49], lista[50], lista[38], lista[42], lista[44], lista[46], lista[35], lista[37], lista[53], lista[25], self.bens[lista[15]]))
            else:
                self.candidatos.inserirOrdenado(Candidato(lista[2], lista[10], lista[13], lista[14], lista[17], lista[15], lista[16], lista[20], lista[18], lista[27], lista[28], lista[49], lista[50], lista[38], lista[42], lista[44], lista[46], lista[35], lista[37], lista[53], lista[25], 'Sem bens declarados'))
            lista = ListaDupla()


    def carregarBens(self, arquivo):
        #dados = self.lerArquivo(arquivo)
        palavra = ''
        lista = ListaDupla()
        for n in open(self.arquivoBens, 'r'):
            for x in n:
                if x != ';':
                    palavra += x
                else:
                    lista.anexar(palavra[1:len(palavra)-1])
                    palavra = ''
            if lista[11] not in self.bens:
                self.bens[lista[11]] = [Bem(lista[13], lista[14], lista[15], lista[16])]
            else:
                self.bens[lista[11]].append(Bem(lista[13], lista[14], lista[15], lista[16]))
            lista = ListaDupla()


    def candidatosPartido(self, siglaDoPartido):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getSiglaPartido__() == siglaDoPartido.upper():
                lista.anexar(x)
        return lista

    def candidatosUF(self, siglaDaUF):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getSiglaUF__() == siglaDaUF.upper():
                lista.anexar(x)
        return lista

    def candidatosMunicipio(self, nomeDoMunicipio):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getMunicipioNascimento__() == nomeDoMunicipio.upper():
                lista.anexar(x)
        return lista

    def candidatosCargo(self, nomeDoCargo):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getDescCargo__() == nomeDoCargo.upper():
                lista.anexar(x)
        return lista

    def candidatosBens(self, totalDosBens):
        lista = ListaDupla()
        for x in self.candidatos:
            try:
                if x.totalDeBens() > float(totalDosBens):
                    lista.anexar(x)
            except:
                x.totalDeBens == None
        return lista

    def candidatosEleitos(self):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getSituacaoCandidato__() == 'ELEITO':
                lista.anexar(x)
        return lista

    def candidatosNaoEleitos(self):
        lista = ListaDupla()
        for x in self.candidatos:
            if x.__getSituacaoCandidato__() == 'NÃO ELEITO':
                lista.anexar(x)
        return lista

    def mediaCargo(self, nomeDoCargo):
        cont = 0
        total = 0
        for x in self.candidatos:
            try:
                if x.__getDescCargo__() == nomeDoCargo.upper():
                    cont += 1
                    total += x.totalDeBens()
            except:
                x.totalDeBens() == None
        return total/cont

    def mediaUF(self, siglaDaUF):
        cont = 0
        total = 0
        for x in self.candidatos:
            try:
                if x.__getSiglaUF__() == siglaDaUF.upper():
                    cont += 1
                    total += x.totalDeBens()
            except:
                x.totalDeBens() == None
        return total/cont

    def mediaPartido(self, siglaDoPartido):
        cont = 0
        total = 0
        for x in self.candidatos:
            try:
                if x.__getSiglaPartido__() == siglaDoPartido.upper():
                    cont += 1
                    total += x.totalDeBens()
            except:
                x.totalDeBens() == None
        return total/cont

    def mediaOcupacao(self, ocupacao):
        cont = 0
        total = 0
        for x in self.candidatos:
            try:
                if x.__getDescOcupacao__() == ocupacao.upper():
                    cont += 1
                    total += x.totalDeBens()
            except:
                x.totalDeBens() == None
        return total/cont

    def mediaAnoDeNascimento(self, dataDeNascimento):
        cont = 0
        total = 0
        for x in self.candidatos:
            try:
                if x.__getDataNascimento__() == dataDeNascimento.upper():
                    cont += 1
                    total += x.totalDeBens()
            except:
                x.totalDeBens() == None
        return total/cont

    def remover(self):
        criterio=input('Digite o código de um desses critérios:\n\n 1- Candidatos indeferidos;\n 2- Candidatos não-eleitos;\n 3- Candidatos sem ensino superior completo;\n 4- Candidatos homens;\n 5- Candidatas mulheres;\n 6- Candidatos solteiros.\n')
        while criterio not in ['1','2','3','4','5','6']:
            criterio = input('Digite um critério válido!')
        no = self.candidatos.cabeca
        if criterio == '1':
            while no != None:
                if no.item.__getSituacaoCandidatura__() == 'INDEFERIDO':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
            no = no.prox
        
        if criterio == '2':
            while no != None:
                if no.item.__getSituacaoCandidato__() == 'NÃO ELEITO':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
                no = no.prox

        if criterio == '3':
            while no != None:
                if no.item.__getGrauInstrucao__() != 'SUPERIOR COMPLETO':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
                no = no.prox

        if criterio == '4':
            while no != None:
                if no.item.__getSexoCandidato__() == 'MASCULINO':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
                no = no.prox

        if criterio == '5':
            while no != None:
                if no.item.__getSexoCandidato__() == 'FEMININO':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
                no = no.prox

        if criterio == '6':
            while no != None:
                if no.item.__getEstadoCivil__() == 'SOLTEIRO(A)':
                    if no == self.candidatos.cabeca:
                        no.prox.ante = no.ante
                        self.candidatos.contador -=1
                        self.candidatos.cabeca = no.prox
                    elif no == self.candidatos.rabo:
                        no.ante.prox = no.prox
                        self.candidatos.contador -=1
                        self.candidatos.rabo = no.ante
                    else:
                        no.ante.prox = no.prox
                        no.prox.ante = no.ante
                        self.candidatos.contador -= 1
                no = no.prox

                
def alfabeticamenteCrescente(candidato1, candidato2):
    if candidato1.__getNomeCandidato__() == candidato2.__getNomeCandidato__():
        return False
    if candidato1.__getNomeCandidato__() == min(candidato1.__getNomeCandidato__(), candidato2.__getNomeCandidato__()):
        return True
    return False

def alfabeticamenteDecrescente(candidato1, candidato2):
    if candidato1.__getNomeCandidato__() == max(candidato1.__getNomeCandidato__(), candidato2.__getNomeCandidato__()):
        return True
    return False

def bensCrescente(candidato1, candidato2):
    if candidato1.totalDeBens() == min(candidato1.totalDeBens(), candidato2.totalDeBens()):
        return True
    return False

def bensDecrescente(candidato1, candidato2):
    if candidato1.totalDeBens() == max(candidato1.totalDeBens(), candidato2.totalDeBens()):
        return True
    return False

def partidoCrescente(candidato1, candidato2):
    if candidato1.__getNumPartido__() == min(candidato1.__getNumPartido__(), candidato2.__getNumPartido__()):
        return True
    return False

def partidoDecrescente(candidato1, candidato2):
    if candidato1.__getNumPartido__() == max(candidato1.__getNumPartido__(), candidato2.__getNumPartido__()):
        return True
    return False

def dataNascimentoCrescente(candidato1, candidato2):
    if int(candidato1.__getDataNascimento__()[6:] + candidato1.__getDataNascimento__()[3:5] + candidato1.__getDataNascimento__()[:2]) == min(int(candidato1.__getDataNascimento__()[6:] + candidato1.__getDataNascimento__()[3:5] + candidato1.__getDataNascimento__()[:2]), int(candidato2.__getDataNascimento__()[6:] + candidato2.__getDataNascimento__()[3:5] + candidato2.__getDataNascimento__()[:2])):
        return True
    return False

def dataNascimentoDecrescente(candidato1, candidato2):
    if int(candidato1.__getDataNascimento__()[6:] + candidato1.__getDataNascimento__()[3:5] + candidato1.__getDataNascimento__()[:2]) == max(int(candidato1.__getDataNascimento__()[6:] + candidato1.__getDataNascimento__()[3:5] + candidato1.__getDataNascimento__()[:2]), int(candidato2.__getDataNascimento__()[6:] + candidato2.__getDataNascimento__()[3:5] + candidato2.__getDataNascimento__()[:2])):
        return True
    return False


if __name__ == '__main__':
    import time
    x = time.time()
    teste = Controle('consulta_cand_2014_BRASIL.csv', 'bem_candidato_2014_BRASIL.csv')
    teste.carregar()
    z = time.time()
    print(z - x)
