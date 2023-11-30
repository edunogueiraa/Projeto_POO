print(f'''
{'-' * 40}
             NOTA FISCAL             
Número: {nota_fiscal.numero}
Data: {nota_fiscal.data}
Produtos: {", ".join(nota_fiscal.produtos)}
Total: R${nota_fiscal.total:.2f}
{'-' * 40}
''')