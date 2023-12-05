class Compras:

    def __init__(self,id_compra: int, nome_produtos: str, quantidade_produtos: int ):

        self.__id_compra = id_compra 
        self.__nome_produtos = nome_produtos
        self.__quantidade_produtos = quantidade_produtos

    #getters e setters 

    def get_id_compra(self):
        return self.__id_compra
    
    def set_id_compra(self, id_novo):
        self.__id_compra = id_novo
    
    def get_nome_produtos(self):
        return self.__nome_produtos
    
    def set_nome_produtos(self, nome_novo):
        self.__nome_produtos = nome_novo
    
    def get_quantidade_produtos(self):
        return self.__quantidade_produtos
    
    def set_quantidade_produtos(self, nova_quantidade):
        self.__quantidade_produtos = nova_quantidade


print(f'''
{'-' * 40}
             NOTA FISCAL             
Número: {nota_fiscal.numero}
Data: {nota_fiscal.data}
Produtos: {", ".join(nota_fiscal.produtos)}
Total: R${nota_fiscal.total:.2f}
{'-' * 40}
''')