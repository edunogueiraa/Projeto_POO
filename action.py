from time import sleep
from classes.compras import Compra
from classes.arquivo import Arquivo

def adicionar_descricao():
    # Obtenha o ID da compra e a descrição do usuário
    id_compra = int(input('\t\tDigite o ID da compra: '))
    descricao = input('\t\tDigite a descrição: ')

    # Abra o arquivo e leia as linhas
    with open('lista.txt', 'r', encoding='utf-8') as compras:
        linhas = compras.readlines()

    # Encontre a compra com o ID fornecido e atualize sua descrição
    for i, linha in enumerate(linhas):
        partes = linha.split(',')
        if int(partes[0]) == id_compra:
            compra = Compra(*partes)
            compra.set_descricao(descricao)
            linhas[i] = str(compra) + '\n'  # Supondo que você tenha um método __str__ adequado na classe Compra

    # Escreva as linhas de volta no arquivo
    with open('lista.txt', 'w', encoding='utf-8') as compras:
        compras.writelines(linhas)

def cadastrar_compra():

    id_compra = contar_compra() + 1
    while id_existente(id_compra):
        id_compra +=1

    print(f'\t\tIdentificador de nova compra: {id_compra}')
    nome_cliente = input('\t\tEscreva o nome do cliente: ')
    telefone_cliente = input('\t\tEscreva o telefone do cliente: ')
    endereco_cliente = input('\t\tEscreva o endereço do cliente: ')
    nome_produto = input('\t\tDigite as cores (separadas -): ')
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

def id_existente(id):
    # Verifica se o id existe no arquivo
    if verifica_arquivo_existente('lista.txt'):
        with open('lista.txt', 'r', encoding='utf-8') as compras:
            linhas = compras.readlines()
            for linha in linhas:
                partes = linha.split(',')
                id_compra = int(partes[0])
                if id_compra == id:
                    return True
    return False

def buscar_compra_pelo_cliente():
    nome = input('\t\tDigite o nome do cliente: ')
    arquivo = open('lista.txt', 'r', encoding='utf-8')

    for elemento in arquivo:
        if nome.lower() in elemento.split(',')[1].lower():
            exibe_compra(elemento)

    arquivo.close()

def contar_compra() -> int:
    if verifica_arquivo_existente('lista.txt'):
        num_compras = 0

        with(open('lista.txt', 'r', encoding='utf-8')) as compras:
            linhas = compras.readlines()

        for _ in linhas:
            num_compras += 1

        return num_compras
    else:
        print('\t\tNão existir compras ...')
        return 0
    
def deletar_compra(id_deletado=-1):
    if id_deletado == -1:
        id_deletado = input('\t\tDigite o ID  da compra para ser deletado: ')
    else:
        id_deletado = id_deletado

    arquivo = open('lista.txt', 'r', encoding='utf-8')
    aux, aux2 = [], []

    for i in arquivo:
        aux.append(i)

    for i in range(0, len(aux)):
        id_temp = aux[i].split(",")[0]

        if id_deletado != id_temp:
            aux2.append(aux[i])

    arquivo.close()
    arquivo = open('lista.txt', 'w', encoding='utf-8')

    for j in aux2:
        arquivo.write(j)

    arquivo.close()

    print('\t\tCompra removida com sucesso!!!')


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

def atualizar_compra():
    id_compra_atualizar = int(input('\t\tDigite o id da compra para atualizar: '))
    deletar_compra(id_compra_atualizar)
    listar_compra()

    arquivo = open('lista.txt', 'r', encoding='utf-8')
    aux, aux2 = [], []

    for i in arquivo:
        aux.append(i)

    for i in range(0, len(aux)):
        id_temp = int(aux[i].split(",")[0])

        if id_compra_atualizar != id_temp:
            aux2.append(aux[i])

    arquivo.close()

    arquivo = open('lista.txt', 'w', encoding='utf-8')

    for i in aux2:
        arquivo.write(i)

    # Obter os novos dados da compra
    id_compra = id_compra_atualizar
    nome_cliente = input('\t\tEscreva o nome do cliente: ')
    telefone_cliente = input('\t\tEscreva o telefone do cliente: ')
    endereco_cliente = input('\t\tEscreva o endereço do cliente: ')
    nome_produto = input('\t\tDigite as cores (separadas -): ')
    quantidade_compra = int(input('\t\tQuantidade de latas de tinta: '))
    valor_compra = float(input('\t\tDigite o valor atual de uma lata de tinta: '))

    try:
        arquivo = open('lista.txt', 'a', encoding='utf-8')
        dados = (
            f'{id_compra}, {nome_cliente},'
            f'{telefone_cliente}, {endereco_cliente},'
            f'{nome_produto}, {quantidade_compra}, '
            f'{valor_compra}\n'
        )
        arquivo.write(dados)
        arquivo.close()
        print('\t\tCompra atualizada com sucesso')
    except FileNotFoundError as e:
        print(f'\t\tOcorreu um erro ao salvar a compra!\n{e}')

def ultima_compra():
    try:
        with(open('lista.txt', 'r', encoding='utf-8')) as Arquivo:
            ultima_compra = Arquivo.readlines()[-1]
            ultimo_contato_txt = (
                f'\n\n\t\tId: {ultima_compra.split(",")[0]}\n'
                f'\t\tNome: {ultima_compra.split(",")[1]}\n'
                f'\t\tTelefone: {ultima_compra.split(",")[2]}\n'
                f'\t\tEndereço: {ultima_compra.split(",")[3]}\n'
                f'\t\tCores: {ultima_compra.split(",")[4]}\n'
                f'\t\tQuantidade: {ultima_compra.split(",")[5]}\n'
                f'\t\tValor: {ultima_compra.split(",")[6]}'
            )

            return ultimo_contato_txt
    except IndexError:
        return '\t\tNenhuma compra foi cadastrada.'

def resetar_arquivo():
    f = open('lista.txt', 'r+', encoding='utf-8')
    f.truncate(0)

def sair():
    print(f'''
██╗░░░██╗░█████╗░██╗░░░░░████████╗███████╗  ░██████╗███████╗███╗░░░███╗██████╗░██████╗░███████╗██╗██╗██╗
██║░░░██║██╔══██╗██║░░░░░╚══██╔══╝██╔════╝  ██╔════╝██╔════╝████╗░████║██╔══██╗██╔══██╗██╔════╝██║██║██║
╚██╗░██╔╝██║░░██║██║░░░░░░░░██║░░░█████╗░░  ╚█████╗░█████╗░░██╔████╔██║██████╔╝██████╔╝█████╗░░██║██║██║
░╚████╔╝░██║░░██║██║░░░░░░░░██║░░░██╔══╝░░  ░╚═══██╗██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══╝░░╚═╝╚═╝╚═╝
░░╚██╔╝░░╚█████╔╝███████╗░░░██║░░░███████╗  ██████╔╝███████╗██║░╚═╝░██║██║░░░░░██║░░██║███████╗██╗██╗██╗
░░░╚═╝░░░░╚════╝░╚══════╝░░░╚═╝░░░╚══════╝  ╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝╚═╝
        ''')
    sleep(1)
    print('Saindo ...')
    sleep(0.5)
    exit()