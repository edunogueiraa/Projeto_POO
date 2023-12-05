class Produto:
    def __init__(self, id_produto: int, nome_produto: str, cor_tinta: str, preco_produto: float, quantidade_produto: int
    ):
        self.__id_produto = id_produto
        self.__nome_produto = nome_produto
        self.__cor_tinta = cor_tinta
        self.__preco_produto = preco_produto
        self.__quantidade_produto = quantidade_produto

    # getters
    def get_id_produto(self):
        return self.__id_produto

    def get_nome(self):
        return self.__nome_produto

    def get_cor(self):
        return self.__cor_tinta

    def get_preco(self):
        return self.__preco_produto

    def get_quantidade(self):
        return self.__quantidade_produto
    
    # Setters

    def set_id_produto(self, novo_id):
        self.__id_produto = novo_id

    def set_nome(self, novo_nome):
        self.__nome_produto = novo_nome

    def set_cor(self, nova_cor):
        self.__cor_tinta = nova_cor

    def set_preco(self, novo_preco):
        self.__preco_produto = novo_preco

    def set_quantidade(self, nova_quantidade):
        self.__quantidade_produto = nova_quantidade


    def descricao(self):
        pass