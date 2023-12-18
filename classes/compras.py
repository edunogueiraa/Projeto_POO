class Descrição:
    def __init__(self, descricao: str):
        
        self.__descricao = descricao

    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao



#Vai herdar uma descrição
class Compra(Descrição):
    def __init__(self, id_compra: str, nome_cliente: str, telefone_cliente: str, endereco_cliente: str, nome_produto: str, valor_compra: str, quantidade_compra: str ):

        
        self.__id_compra = id_compra
        self.__nome_cliente = nome_cliente
        self.__telefone_cliente = telefone_cliente
        self.__endereco_cliente = endereco_cliente
        self.__nome_produto = nome_produto
        self.__valor_compra = valor_compra
        self.__quantidade_compra = quantidade_compra

    # getters
    def get_id_compra(self):
        return self.__id_compra

    def get_nome_cliente(self):
        return self.__nome_cliente

    def get_telefone_cliente(self):
        return self.__telefone_cliente

    def get_endereco_cliente(self):
        return self.__endereco_cliente
    
    def get_nome_produto(self):
        return self.__nome_produto

    def get_valor_compra(self):
        return self.__valor_compra

    def get_quantidade_compra(self):
        return self.__quantidade_compra

    # Setters
    def set_id_compra(self, id_novo):
        self.__id_compra = id_novo

    def set_nome_cliente(self, novo_nome_cliente):
        self.__nome_cliente = novo_nome_cliente

    def set_telefone_cliente(self, novo_telefone_cliente):
        self.__telefone_cliente = novo_telefone_cliente

    def set_endereco_cliente(self, novo_endereco_cliente):
        self.__endereco_cliente = novo_endereco_cliente

    def set_nome_produto(self, nome_novo):
        self.__nome_produto = nome_novo

    def set_valor_compra(self, novo_valor):
        self.__valor_compra = novo_valor

    def set_quantidade_compra(self, nova_quantidade):
        self.__quantidade_compra = nova_quantidade


    #Calcular preço pela quantidade de latas compradas com o padra de preço de cada lata
    def calcular_preco(self):
        quantidade = self.get_quantidade_compra()

        preco = self.get_valor_compra()

        preco_total = (preco * quantidade)
        return preco_total
