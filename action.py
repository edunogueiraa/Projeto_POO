from time import sleep
from classes.compras import Compra
from classes.arquivo import Arquivo

def cadastrar_compra():
    id_compra = contar_compra() + 1
    print(f'\t\tIdentificador de nova compra: {id_compra}')
    nome_cliente = input('\t\tEscreva o nome do cliente: ')
    telefone_cliente = input('\t\tEscreva o telefone do cliente: ')
    endereco_cliente = input('\t\tEscreva o endereço do cliente: ')
    nome_produto = input('\t\tDigite as cores *(azul - rosa): ')
    quantidade_compra = int(input('\t\tQuantidade de latas de tinta: '))
    valor_compra = float(input('\t\tDigite o valor atual de uma lata de tinta: '))

    nova_compra = Compra(
        id_compra,
        nome_cliente,
        telefone_cliente,
        endereco_cliente,
        nome_produto,
        quantidade_compra,
        valor_compra
    )

    try:
        arquivo = Arquivo('lista.txt', 'a')
        lista = arquivo.abrir_arquivo()
        dados = (        
            f'{nova_compra.get_id_compra()}, {nova_compra.get_nome_cliente()},' 
            f'{nova_compra.get_telefone_cliente()}, {nova_compra.get_endereco_cliente()},' 
            f'{nova_compra.get_nome_produto()}, {nova_compra.get_quantidade_compra()}, ' 
            f'{nova_compra.calcular_preco()}\n')

        lista.write(dados)
        arquivo.fechar_arquivo(lista)

    except FileNotFoundError as e:
        print(f'\t\tArquivo de lista não foi encontrado!\n{e}')
    except IOError as e:
        print(f'\t\tOcorreu um erro de entrada de dados!\n{e}')
    except Exception as e:
        print(f'\t\tOcorreu um erro ao salvar a compra!\n{e}')
    else:
        print('\t\tCompra cadastrada com sucesso!!!\n')

def listar_compra():
    arquivo = open('lista.txt', 'r', encoding='utf-8')

    if contar_compra() > 0:
        print('\n\t\tListando compras:\n'.upper())
        for compra in arquivo:
            exibe_compra(compra)
    else:
        print('\t\tNão existem compras cadastradas!')
    
    arquivo.close()

def exibe_compra(compra):

    print(f'Id: {compra.split(",")[1]}\n '
          f'Nome: {compra.split(",")[2]}\n '
          f'Telefone: {compra.split(",")[3]}\n '
          f'Endereço: {compra.split(",")[4]}\n '
          f'Cores: {compra.split(",")[0]}\n '
          f'Quandidade: {compra.split(",")[5]}\n '
          f'valor: {compra.split(",")[6]}\n\n ', end=''
          )


def contar_compra() -> int:
    if verifica_arquivo_existente('lista.txt'):
        num_compras = 0

        with(open('lista.txt', 'r', encoding='utf-8')) as compras:
            linhas = compras.readlines()

        # Se a variável de iteração do for (i) não for ser usada na iteração, usar um underscore ao invés.
        for _ in linhas:
            num_compras += 1

        return num_compras
    else:
        print('\t\tNão existir compras ...')
        return 0

def verifica_arquivo_existente(arquivo: str) -> bool:
    # se arquivo não existir, retorne False
    # caso contrário, retorne True

    try:
        lista = open('lista.txt', encoding='utf-8')  # 'r' pé o modo padrão de abertura de arquivo
        lista.close()
        return True

    except FileNotFoundError:
        print(f'Arquivo {arquivo} não existe :/')
        return False


def resetar_arquivo():
    f = open('lista.txt', 'r+', encoding='utf-8')
    f.truncate(0)

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