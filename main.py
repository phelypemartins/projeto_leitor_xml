import xmltodict

def ler_xml_danfe(nota):

    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)

    dic_nota_fiscal = documento['nfeProc']['NFe']['infNFe']

    n_nota = dic_nota_fiscal['ide']['nNF']
    cnpj_emissor = dic_nota_fiscal['emit']['CNPJ']
    nome_emissor = dic_nota_fiscal['emit']['xNome']
    cnpj_comprador = dic_nota_fiscal['dest']['CNPJ']
    nome_comprador = dic_nota_fiscal['dest']['xNome']
    produto = dic_nota_fiscal['det']

    lista_produto = []

    for produto in produto:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['NCM']
        lista_produto.append((valor_produto, nome_produto))

    resposta = {
        'n_nota': n_nota,
        'cnpj_emissor': [cnpj_emissor],
        'nome_emissor': [nome_emissor],
        'cnpj_comprador': [cnpj_comprador],
        'nome_comprador': [nome_comprador],
        'lista_produto': [lista_produto],
    }

    return resposta


import os

        
import pandas as pd
arquivos = os.listdir('xml')
#
df_final = pd.DataFrame()
for arquivo in arquivos:
    if 'NFE' in arquivo:
        df = pd.DataFrame.from_dict(ler_xml_danfe(f'xml/{arquivo}'))
    df_final = pd.concat([df,df_final], ignore_index=1)
print(df_final)
df_final.to_excel('NFs.xlsx', index=False)
    
