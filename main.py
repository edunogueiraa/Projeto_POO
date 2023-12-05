from action import contar_compra
#from action import ultima_compra
#from action import cadastrar_compra
#from action import listar_produtos
#from action import deletar_compra
#from action import buscar_compra
#from action import atualizar_precos
#from action import buscar_produto
from action import emitir_nota_fiscal
#from action import cadastrar_produto
from action import sair

# função menu inicial terá um while 
# que enquando continuar no menu for 
# true ele executará o menu

#Essa parte: {'-' * 64} escreve 64 vezes esse caractere

def menuInicial():
     
    continuarMenu: str = 's'
     
    while continuarMenu == 's': 
        opcao = input(f'''
        {'-' * 64}
                    PROJETO LOJA DE TINTAS (POO)            
        {contar_compra()} COMPRAS CADASTRADAS\n
        ÚLTIMA COMPRA: \n 

        MENU PRINCIPAL:

        [1] CADASTRAR COMPRA       \t[6] ATUALIZAR PREÇOS
        [2] LISTAR COMPRAS         \t[7] BUSCAR PRODUTO POR NOME
        [3] DELETAR COMPRA         \t[8] EMITIR NOTA FISCAL
        [4] BUSCAR COMPRA          \t[9] CADASTRAR PRODUTO
        [5] EMITIR NOTA FISCAL     \t[0] SAIR DO MENU
                                    
        {'-' * 64}

        ESCOLHA UMA OPÇÃO: ''')

        if opcao == "1":
            cadastrar_compra()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            deletar_compra()
        elif opcao == "4":
            buscar_compra()
        elif opcao == "5":
            emitir_nota_fiscal()
        elif opcao == "6":
            atualizar_precos()
        elif opcao == "7":
            buscar_produto()
        elif opcao == "8":
            emitir_nota_fiscal()
        elif opcao == "9":
            cadastrar_produto()
        elif opcao == '0':
            sair()
        else:
            print('\t\tEssa opção não está disponivel!')
                
            continuarMenu = input('\t\tDeseja voltar ao menu principal? (s/n)').lower() #converte strings para minúsculas

         
         
if __name__ == '__main__':
        
    menuInicial() #Executa o menu inicial