from time import sleep
from classes.compras import Compra, Tinta
from classes.arquivo import Arquivo

def misturar_cores():
    id_compra = int(input('\t\tDigite o ID da compra para adicionar uma mistura: '))
    if not id_existente(id_compra):
        print(f'\t\tCompra com ID {id_compra} não encontrada.')
        return

    print(f'Cores Disponíveis para Mistura:\n'
          f'[1] Vermelho\n'
          f'[2] Amarelo\n'
          f'[3] Azul\n'
          f'[4] Preto\n'
          f'[5] Rosa\n'
          f'[6] Laranja\n'
          f'[7] Roxo\n')

    escolha1 = int(input("Digite o número da primeira cor: "))
    escolha2 = int(input("Digite o número da segunda cor: "))

    cores_disponiveis = ["vermelho", "amarelo", "azul", "preto", "rosa", "laranja", "roxo"]

    try:
        tinta1 = Tinta(cores_disponiveis[escolha1 - 1])
        tinta2 = Tinta(cores_disponiveis[escolha2 - 1])
    except IndexError:
        print("Escolha apenas uma cor disponível!")
        return

    combinacoes = {
        ("vermelho", "amarelo"): "laranja",
        ("amarelo", "vermelho"): "laranja",
        ("vermelho", "azul"): "roxo",
        ("azul", "vermelho"): "roxo",
        ("amarelo", "azul"): "verde",
        ("azul", "amarelo"): "verde",
        ("vermelho", "vermelho"): "vermelho",
        ("amarelo", "amarelo"): "amarelo",
        ("azul", "azul"): "azul",
        ("preto", "preto"): "preto",
        ("vermelho", "preto"): "borgonha",
        ("preto", "vermelho"): "borgonha",
        ("amarelo", "preto"): "marrom",
        ("preto", "amarelo"): "marrom",
        ("azul", "preto"): "azul escuro",
        ("preto", "azul"): "azul escuro",
        ("rosa", "rosa"): "rosa",
        ("rosa", "laranja"): "salmao",
        ("laranja", "rosa"): "salmao",
        ("rosa", "roxo"): "violeta",
        ("roxo", "rosa"): "violeta",
        ("laranja", "laranja"): "laranja",
        ("laranja", "roxo"): "marrom",
        ("roxo", "laranja"): "marrom",
    }

    if (tinta1.get_resultado_mistura(), tinta2.get_resultado_mistura()) in combinacoes:
        cor_resultante = combinacoes[(tinta1.get_resultado_mistura(), tinta2.get_resultado_mistura())]
    elif (tinta2.get_resultado_mistura(), tinta1.get_resultado_mistura()) in combinacoes:
        cor_resultante = combinacoes[(tinta2.get_resultado_mistura(), tinta1.get_resultado_mistura())]
    else:
        cor_resultante = "cor indefinida"

    print(f'\t\tCor resultante ({cor_resultante}) adicionada à compra no ID: {id_compra}.')

    # Atualizar a compra com a nova cor misturada
    arquivo = open('lista.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    for i in range(len(linhas)):
        partes = linhas[i].split(',')
        if int(partes[0]) == id_compra:
            # Substituir o nenhuma parão pela cor misturada
            linhas[i] = linhas[i].replace(" Nenhuma", cor_resultante)
            break

    arquivo = open('lista.txt', 'w', encoding='utf-8')
    arquivo.writelines(linhas)
    arquivo.close()
    
def cadastrar_compra():
    id_compra = contar_compra() + 1
    while id_existente(id_compra):
        id_compra += 1

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
        valor_compra,
        quantidade_compra,
        cor_misturada = "Nenhuma"
    )

    try:
        lista = open('lista.txt', 'a', encoding='utf-8')
        dados = (
            f'{nova_compra.get_id_compra()}, {nova_compra.get_nome_cliente()},'
            f'{nova_compra.get_telefone_cliente()}, {nova_compra.get_endereco_cliente()},'
            f'{nova_compra.get_nome_produto()}, {nova_compra.get_quantidade_compra()}, '
            f'{nova_compra.calcular_preco()}, {nova_compra.get_resultado_mistura()}\n'  # Include mixed color
        )

        lista.write(dados)
        lista.close()

        print('\t\tCompra cadastrada com sucesso!!!\n')
    except FileNotFoundError as e:
        print(f'\t\tArquivo de lista não foi encontrado!\n{e}')
    except IOError as e:
        print(f'\t\tOcorreu um erro de entrada de dados!\n{e}')
    except Exception as e:
        print(f'\t\tOcorreu um erro ao salvar a compra!\n{e}')


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
    partes = compra.split(',')
    
    if len(partes) >= 8:
        cor_misturada = partes[7].strip()
    else:
        cor_misturada = "Nenhum"

    print(f'Id: {partes[0]}\n'
          f'Nome: {partes[1]}\n'
          f'Telefone: {partes[2]}\n'
          f'Endereço: {partes[3]}\n'
          f'Cores: {partes[4]}\n'
          f'Quantidade: {partes[5]}\n'
          f'Cor Misturada: {cor_misturada}\n'
          f'Valor: {partes[6]}\n')


def id_existente(id):

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
    try:
        with open(arquivo, 'r', encoding='utf-8') as lista:
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
        with open('lista.txt', 'r', encoding='utf-8') as arquivo:
            ultima_compra = arquivo.readlines()[-1].strip().split(',')
            id_compra = ultima_compra[0]
            nome_cliente = ultima_compra[1]
            telefone_cliente = ultima_compra[2]
            endereco_cliente = ultima_compra[3]
            cores = ultima_compra[4]
            quantidade = ultima_compra[5]
            valor = ultima_compra[6]

            if len(ultima_compra) >= 8:
                cor_misturada = ultima_compra[7].strip()
            else:
                cor_misturada = "Nenhum"

            ultima_compra_txt = (
                f'\n\n\t\tId: {id_compra}\n'
                f'\t\tNome: {nome_cliente}\n'
                f'\t\tTelefone: {telefone_cliente}\n'
                f'\t\tEndereço: {endereco_cliente}\n'
                f'\t\tCores: {cores}\n'
                f'\t\tQuantidade: {quantidade}\n'
                f'\t\tValor: {valor}\n'
                f'\t\tCor Misturada: {cor_misturada}'
            )

            return ultima_compra_txt

    except IndexError:
        return '\t\tNenhuma compra foi cadastrada.'
    except FileNotFoundError:
        return '\t\tArquivo "lista.txt" não encontrado.'

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