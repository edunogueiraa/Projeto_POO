from time import sleep
from classes.arquivo import Arquivo

#        [1] CADASTRAR COMPRA       \t[6] ATUALIZAR PREÇOS
#        [2] LISTAR COMPRAS         \t[7] BUSCAR PRODUTO EM ESTOQUE
#        [3] DELETAR COMPRA         \t[8] EMITIR NOTA FISCAL
#        [4] BUSCAR COMPRA          \t[9] CADASTRAR PRODUTO
#        [5] EMITIR NOTA FISCAL     \t[0] SAIR

#def cadastrar_compra():
def listar_compras(): #Resolva--------------
    nota_fiscal = open('Nota_fiscal.txt', 'r', encoding='utf-8')

    if contar_compras() > 0:
        print('\n\t\tListando compras:\n'.upper())
        for contato in nota_fiscal:
            exibe_compras(Compras)
    else:
        print('\t\tNão existem contatos cadastrados')

    nota_fiscal.close()

def exibe_compras(Compras): #Resolva--------------
    print(f'\t\tId: {contato.split(";")[0]} '
          f'Nome: {contato.split(";")[1]} '
          f'Telefone: {contato.split(";")[2]} '
          f'Email: {contato.split(";")[3]}', end=''
          )

def contar_compras() -> int:
    if verifica_arquivo_existente('Nota_fiscal.txt'):
        num_compras = 0

        with(open('Nota_fiscal.txt', 'r', encoding='utf-8')) as compras:
            linhas = compras.readlines()

        for _ in linhas:
            num_compras += 1

        return num_compras
    else:
        print('\t\tNão existem contatos ...')
        return 0

def verifica_arquivo_existente(arquivo: str) -> bool: #Verifica se o arquivo existre ou não
    try:
        nota_fiscal = open('Nota_fiscal.txt', encoding='utf-8')
        nota_fiscal.close()
        return True

    except FileNotFoundError:
        print(f'Arquivo {arquivo} não existe!')
        return False

def sair():
    print(f'''
░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░░
        ''')
    sleep(1)
    print('Saindo ...')
    sleep(0.5)
    exit()