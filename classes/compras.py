class Compras:

    def __init__(self,id_compra: int, nome_cliente: str, nome_produto: list, valor_compra: float, quantidade_compra: int):

        self.__id_compra = id_compra 
        self.__nome_cliente = nome_cliente
        self.__nome_produtos = nome_produto
        self.__valor_compra = valor_compra
        self.__quantidade_compra = quantidade_compra

    #getters  

    def get_id_compra(self):
        return self.__id_compra

    def get_nome_cliente(self):
        return self.__nome_cliente
    
    def get_nome_produtos(self):
        return self.__nome_produtos
    
    def get_valor_compra(self):
        return self.__valor_compra
    
    def get_quantidade_compra(self):
        return self.__quantidade_compra
    
    # Setters

    def set_id_compra(self, id_novo):
        self.__id_compra = id_novo
    
    def set_nome_cliente(self, novo_nome_cliente):
        self.__nome_cliente = novo_nome_cliente
    
    def set_nome_produtos(self, nome_novo):
        self.__nome_produtos = nome_novo

    def set_valor_compra(self,novo_valor):
        self.__valor_compra = novo_valor

    def set_quantidade_compra(self, nova_quantidade):
        self.__quantidade_compra = nova_quantidade