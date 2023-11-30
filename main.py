
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

        ÚLTIMA COMPRA:\n 

        MENU PRINCIPAL:

        [1] CADASTRAR COMPRA       \t[6] ATUALIZAR PREÇOS
        [2] LISTAR COMPRAS         \t[7] BUSCAR PRODUTO EM ESTOQUE
        [3] DELETAR COMPRA         \t[8] EMITIR NOTA FISCAL
        [4] BUSCAR COMPRA          \t[9] CADASTRAR PRODUTO
        [5] EMITIR NOTA FISCAL     \t[0] SAIR DO MENU
                                    
        {'-' * 64}

        ESCOLHA UMA OPÇÃO: ''')

        if opcao == '1':
            print("")
        elif opcao == '2':
            print("")
        elif opcao == '3':
            print("")
        elif opcao == '4':
            print("")
        elif opcao == '5':
            print("")
        elif opcao == '6':
            print("")
        elif opcao == '7':
            print("")
        elif opcao == '8':
            print("")
        elif opcao == '9':
            print("")
        elif opcao == '0':
            print("")
        else:
            print('\t\tEssa opção não está disponivel!')
                
            continuarMenu = input('\t\tDeseja voltar ao menu principal? (s/n)').lower()

         
         
if __name__ == '__main__':
        
    menuInicial()