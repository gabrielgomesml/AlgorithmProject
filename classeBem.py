from classeCandidato import *
from classeLista import *
from classeControle import *

class Bem:
    def __init__(self, codigo_do_tipo_de_bem, descricao_do_tipo_de_bem, descricao_detalhada_do_bem, valor_do_bem):
        self.codigo_do_tipo_de_bem = codigo_do_tipo_de_bem
        self.descricao_do_tipo_de_bem = descricao_do_tipo_de_bem
        self.descricao_detalhada_do_bem = descricao_detalhada_do_bem
        self.valor_do_bem = valor_do_bem

    def __getCodigo__(self):
        return self.codigo_do_tipo_de_bem.replace(',', '.')
    def __getDescricaoTipo__(self):
        return self.descricao_do_tipo_de_bem
    def __getDescricaoDetalhada__(self):
        return self.descricao_detalhada_do_bem
    def __getValor__(self):
        return self.valor_do_bem.replace(',', '.')

    def __setCodigo__(self, novoCodigo):
        self.codigo_do_tipo_de_bem = novoCodigo
    def __setDescricaoTipo__(self, novaDescricao):
        self.descricao_do_tipo_de_bem = novaDescricao
    def __setDescricaoDetalhada__(self, novaDescricao):
        self.descricao_detalhada_do_bem = novaDescricao
    def __setValor__(self, novoValor):
        self.valor_do_bem = novoValor

    def __str__(self):
        string = f'{self.__getCodigo__()} -- {self.__getDescricaoTipo__()} -- {self.__getValor__()}\n{self.__getDescricaoDetalhada__()}'
        return string

    def __repr__(self):
        return 'Bem' + str((self.__getCodigo__(), self.__getDescricaoTipo__(), self.__getDescricaoDetalhada__(), self.__getValor__()))
        
    def __it__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() == bem2.__getCodigo__() and bem1.__getDescricaoDetalhada__() < bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() < bem2.__getCodigo__():
                return True
            elif float(bem1.__getValor__()) < float(bem2.__getValor__()):
                return True
            return False

    def __gt__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() == bem2.__getCodigo__() and bem1.__getDescricaoDetalhada__() > bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() > bem2.__getCodigo__():
                return True
            elif float(bem1.__getValor__()) > float(bem2.__getValor__()):
                return True
            return False

    def __le__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if float(bem1.__getValor__()) == float(bem2.__getValor__()) and bem1.__getDescricaoDetalhada__() == bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() == bem2.__getCodigo__() and bem1.__getDescricaoDetalhada__() < bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() < bem2.__getCodigo__():
                return True
            elif float(bem1.__getValor__()) < float(bem2.__getValor__()):
                return True
            return False

    def __ge__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if float(bem1.__getValor__()) == float(bem2.__getValor__()) and bem1.__getDescricaoDetalhada__() == bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() == bem2.__getCodigo__() and bem1.__getDescricaoDetalhada__() > bem2.__getDescricaoDetalhada__():
                return True
            elif bem1.__getValor__() == bem2.__getValor__() and bem1.__getCodigo__() > bem2.__getCodigo__():
                return True
            elif float(bem1.__getValor__()) > float(bem2.__getValor__()):
                return True
            return False

    def __eq__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if float(bem1.__getValor__()) == float(bem2.__getValor__()) and bem1.__getDescricaoDetalhada__() == bem2.__getDescricaoDetalhada__():
                return True
            return False

    def __ne__(bem1, bem2):
        if type(bem1) != type(bem2):
            raise TypeError
        else:
            if bem1.__getValor__() != bem2.__getValor__() and bem1.__getDescricaoDetalhada__() != bem2.__getDescricaoDetalhada__():
                return True
            return False