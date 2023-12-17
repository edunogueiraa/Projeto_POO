from action import buscar_compra_pelo_cliente
from action import deletar_compra
from action import listar_compra
from action import contar_compra
from action import cadastrar_compra
from action import resetar_arquivo
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
                    PROJETO LOJA DE TINTAS (POO)\n            
        {contar_compra()} COMPRAS CADASTRADAS\n
        ÚLTIMA COMPRA: \n 

        MENU PRINCIPAL:

        [1] CADASTRAR COMPRA$       \t[6] MISTURADOR DE CORES
        [2] LISTAR COMPRAS$         \t[7] BUSCAR COMPRA POR CLIENTE$
        [3] DELETAR COMPRA$         \t[0] SAIR DO MENU$
        [4] RESETAR ARQUIVO$        
        [5] SOBRE O CLIENTE     
                                    
        {'-' * 64}

        ESCOLHA UMA OPÇÃO: ''')

        if opcao == "1":
            cadastrar_compra()
        elif opcao == "2":
            listar_compra()
        elif opcao == "3":
            deletar_compra()
        elif opcao == "4":
            resetar_arquivo()
        elif opcao == "5":
            emitir_nota_fiscal()
        elif opcao == "6":
            paleta_e_mistura_cores()
        elif opcao == "7":
            buscar_compra_pelo_cliente()
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