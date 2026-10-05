"""#listas encadeadas

class Node:
    def __init__(self, init_data):

        self.__data = init_data
        self.__next = None


    def get_data(self):
        return self.__data

    
    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

class LinkdList:
    def __init__(self):
        self.head = head"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.cabeca
        self.cabeca = novo
        self.tamanho += 1

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def __len__(self):
        return self.tamanho

    def __str__(self):
        valores = []
        atual = self.cabeca
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores) + " -> None"


def get_lenght(lista):
    contador = 0
    atual = lista.cabeca
    while atual:
        contador += 1
        atual = atual.proximo
    return contador


# Teste
lista = ListaEncadeada()
lista.inserir_fim(10)
lista.inserir_fim(20)
lista.inserir_inicio(5)

print(lista)              # 5 -> 10 -> 20 -> None
print(get_lenght(lista))  # 3

lista.remover(10)
print(lista)              # 5 -> 20 -> None
print(get_lenght(lista))  # 2
def get_lenght(lista):
    contador = 0
    atual = lista.head
    while atual:
        contador += 1
        atual = atual.next 
    return contador

lista = ListaEncadeada()
lista.inserir_fim(10)
lista.inserir_fim(20)
lista.inserir_fim(30)

print(get_lenght(lista)) 