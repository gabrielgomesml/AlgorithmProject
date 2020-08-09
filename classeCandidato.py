from classeLista import *
from classeBem import *
from classeControle import *

class Candidato:
    def __init__(self, ano_da_eleicao, sigla_da_uf, codigo_do_cargo, descricao_do_cargo, nome_do_candidato, id_do_candidato, numero_na_urna, cpf, nome_na_urna, numero_do_partido, sigla_do_partido, codigo_de_ocupacao, descricao_da_ocupacao, data_de_nascimento, sexo_do_candidato, grau_de_instrucao, estado_civil, uf_de_nascimento, municipio_de_nascimento, situacao_do_candidato, situacao_da_candidatura, lista_de_bens):
        self.ano_da_eleicao = ano_da_eleicao
        self.sigla_da_uf = sigla_da_uf
        self.codigo_do_cargo = codigo_do_cargo
        self.descricao_do_cargo = descricao_do_cargo
        self.nome_do_candidato = nome_do_candidato
        self.id_do_candidato = id_do_candidato
        self.numero_na_urna = numero_na_urna
        self.cpf = cpf
        self.nome_na_urna = nome_na_urna
        self.numero_do_partido = numero_do_partido
        self.sigla_do_partido = sigla_do_partido
        self.codigo_de_ocupacao = codigo_de_ocupacao
        self.descricao_da_ocupacao = descricao_da_ocupacao
        self.data_de_nascimento = data_de_nascimento
        self.sexo_do_candidato = sexo_do_candidato
        self.grau_de_instrucao = grau_de_instrucao
        self.estado_civil = estado_civil
        self.uf_de_nascimento = uf_de_nascimento
        self.municipio_de_nascimento = municipio_de_nascimento
        self.situacao_do_candidato = situacao_do_candidato
        self.situacao_da_candidatura = situacao_da_candidatura
        self.lista_de_bens = lista_de_bens

    def __getAnoEleicao__(self):
        return self.ano_da_eleicao
    def __getSiglaUF__(self):
        return self.sigla_da_uf
    def __getCodCargo__(self):
        return self.codigo_do_cargo
    def __getDescCargo__(self):
        return self.descricao_do_cargo
    def __getNomeCandidato__(self):
        return self.nome_do_candidato
    def __getIdCandidato__(self):
        return self.id_do_candidato
    def __getNumUrna__(self):
        return self.numero_na_urna
    def __getCPF__(self):
        return self.cpf
    def __getNomeUrna__(self):
        return self.nome_na_urna
    def __getNumPartido__(self):
        return self.numero_do_partido
    def __getSiglaPartido__(self):
        return self.sigla_do_partido
    def __getCodOcupacao__(self):
        return self.codigo_de_ocupacao
    def __getDescOcupacao__(self):
        return self.descricao_da_ocupacao
    def __getDataNascimento__(self):
        return self.data_de_nascimento
    def __getSexoCandidato__(self):
        return self.sexo_do_candidato
    def __getGrauInstrucao__(self):
        return self.grau_de_instrucao
    def __getEstadoCivil__(self):
        return self.estado_civil
    def __getUFNascimento__(self):
        return self.uf_de_nascimento
    def __getMunicipioNascimento__(self):
        return self.municipio_de_nascimento
    def __getSituacaoCandidato__(self):
        return self.situacao_do_candidato
    def __getSituacaoCandidatura__(self):
        return self.situacao_da_candidatura
    def __getBens__(self):
        return self.lista_de_bens

    def __setAnoEleicao__(self, novoAno):
        self.ano_da_eleicao = novoAno
    def __setSiglaUF__(self, novaSigla):
        self.sigla_da_uf = novaSigla
    def __setCodCargo__(self, novoCodigo):
        self.codigo_do_cargo = novoCodigo
    def __setDescCargo__(self, novaDescricao):
        self.descricao_do_cargo = novaDescricao
    def __setNomeCandidato__(self, novoNome):
        self.nome_do_candidato = novoNome
    def __setIdCandidato__(self, novoId):
        self.id_do_candidato = novoId
    def __setNumUrna__(self, novoNumero):
        self.numero_na_urna = novoNumero
    def __setCPF__(self, novoCPF):
        self.cpf = novoCPF
    def __setNomeUrna__(self, novoNome):
        self.nome_na_urna = novoNome
    def __setNumPartido__(self, novoNumero):
        self.numero_do_partido = novoNumero
    def __setSiglaPartido__(self, novaSigla):
        self.sigla_do_partido = novaSigla
    def __setCodOcupacao__(self, novoCodigo):
        self.codigo_de_ocupacao = novoCodigo
    def __setDescOcupacao__(self, novaDescricao):
        self.descricao_da_ocupacao = novaDescricao
    def __setDataNascimento__(self, novaData):
        self.data_de_nascimento = novaData
    def __setSexoCandidato__(self, novoSexo):
        self.sexo_do_candidato = novoSexo
    def __setGrauInstrucao__(self, novoGrau):
        self.grau_de_instrucao = novoGrau
    def __setEstadoCivil__(self, novoEstado):
        self.estado_civil = novoEstado
    def __setUFNascimento__(self, novaUF):
        self.uf_de_nascimento = novaUF
    def __setMunicipioNascimento__(self, novoMunicipio):
        self.municipio_de_nascimento = novoMunicipio
    def __setSituacaoCandidato__(self, novaSituacao):
        self.situacao_do_candidato = novaSituacao
    def __setSituacaoCandidatura__(self, novaSituacao):
        self.situacao_da_candidatura = novaSituacao

    def incluirBem(self, bem):
        if type(bem) is not Bem:
            raise TypeError('O argumento deve ser do tipo Bem.')
        self.lista_de_bens.append(bem)

    def printarBens(self):
        if type(self.__getBens__()) is str:
            print(self.__getBens__())
        for x in self.__getBens__():
            print(x.__getDescricaoTipo__().upper() + ': ' + x.__getDescricaoDetalhada__())

    def totalDeBens(self):
        valorTotal = 0
        if type(self.__getBens__()) is str:
            return None
        for x in self.__getBens__():
            valorTotal += float(x.__getValor__())
        return valorTotal

    def resumoBens(self):
        valorTotal = 0
        valorTipos = {}
        for x in self.__getBens__():
            valorTotal += float(x.__getValor__())
            if x.__getCodigo__() not in valorTipos:
                valorTipos[x.__getCodigo__()] = float(x.__getValor__())
            else:
                valorTipos[x.__getCodigo__()] = float(x.__getValor__())
        valorTipos2 = ''
        for y in valorTipos:
            valorTipos2 += 'Bens tipo ' + y + ': ' + str(valorTipos[y]) + '\n'
        return 'Valor Total: ' + str(valorTotal) + '\n' + valorTipos2
            

    def __str__(self):
        string1 = f'{self.__getNomeUrna__()} -- {self.__getNumUrna__()} -- {self.__getSiglaPartido__()}\n{self.__getDescCargo__()} ({self.__getSiglaUF__()}) {self.__getMunicipioNascimento__()} ({self.__getUFNascimento__()})\nResumo dos bens:\n\n'
        if type(self.__getBens__()) is str:
            return string1 + 'Sem bens declarados.'
        string2 = self.resumoBens()
        return string1 + string2
    
    def __repr__(self):
        return 'Candidato' + str((self.ano_da_eleicao, self.sigla_da_uf, self.codigo_do_cargo, self.descricao_do_cargo, self.nome_do_candidato, self.id_do_candidato, self.numero_na_urna, self.cpf, self.nome_na_urna, self.numero_do_partido, self.sigla_do_partido, self.codigo_de_ocupacao, self.descricao_da_ocupacao, self.data_de_nascimento, self.sexo_do_candidato, self.grau_de_instrucao, self.estado_civil, self.uf_de_nascimento, self.municipio_de_nascimento, self.situacao_do_candidato, self.situacao_da_candidatura, self.lista_de_bens))

    def __eq__(candidato1, candidato2):
        if type(candidato1) != type(candidato2):
            raise TypeError
        else:
            if candidato1.__getNomeCandidato__() is candidato2.__getNomeCandidato__() and candidato1.__getCPF__() is candidato2.__getCPF__():
                return True
            return False
        
    def __ne__(candidato1, candidato2):
        if type(candidato1) != type(candidato2):
            raise TypeError
        else:
            if candidato1.__getNomeCandidato__() is not candidato2.__getNomeCandidato__() and candidato1.__getCPF__() is not candidato2.__getCPF__():
                return True
            return False