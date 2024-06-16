import os
import xmltodict
import pandas as pd
import json
import openpyxl


# Função para ler informações de um arquivo XML e extrair dados específicos
def ler_informacoes(nome_arquivo, valores):
    print(f'Processando arquivo: {nome_arquivo}')
    try:
        # Abre o arquivo XML para leitura
        with open(f'cte/{nome_arquivo}', 'rb') as arquivo_xml:
            # Converte o conteúdo XML para um dicionário Python
            dicionario_arquivo = xmltodict.parse(arquivo_xml)
            # Imprime o dicionário para depuração
            print(json.dumps(dicionario_arquivo, indent=4))

            # Acessa a seção específica do XML ( Personalizável )
            if "cteProc" in dicionario_arquivo:
                infos_nf = dicionario_arquivo["cteProc"]
                id = infos_nf["CTe"]["infCte"]["@Id"]

                # Verifica se existe a seção infoNFe e se é uma lista
                info_nfe = infos_nf["CTe"]["infCte"]["infCTeNorm"]["infDoc"].get("infNFe", [])

                # Verifica o tipo de info_nfe para evitar erros
                if not isinstance(info_nfe, list):
                    info_nfe = [info_nfe]

                # Extrai as chaves
                chave_nfe_1 = info_nfe[0]["chave"] if len(info_nfe) > 0 else None
                chave_nfe_2 = info_nfe[1]["chave"] if len(info_nfe) > 1 else None


                # Adiciona os valores extraídos à lista de valores
                # valores.append([id, chave_nfe_1, chave_nfe_2])
                # return id, chave_nfe_1, chave_nfe_2
                if chave_nfe_2:
                    valores.append([id, chave_nfe_1, chave_nfe_2])
                else:
                    valores.append([id, chave_nfe_1, None])

                # return id,chave_nfe_1, chave_nfe_2
                # info_nfe = infos_nf["CTe"]["infCte"]["infCTeNorm"]["infDoc"]["infNFe"]
            else:
                print(f'Seção "cteProc" não encontrada no arquivo: {nome_arquivo}')
                # return None

    except Exception as e:
        # Tratamento de erro caso ocorra algum problema ao processar o arquivo
        print(f'Erro ao processar {nome_arquivo}: {e}')
        # return None


# Lista todos os arquivos no diretório 'cte'
lista_arquivos = os.listdir('cte')
# Define as colunas para o DataFrame
colunas = ['Chave CTe', 'Chave NFe1', 'Chave NFe2']
valores = []
# Itera sobre cada arquivo na lista de arquivos
for arquivo in lista_arquivos:
    ler_informacoes(arquivo, valores)  # Chama a função para ler e extrair informações do arquivo

# Cria uma tabela com os dados extraídos
tabela = pd.DataFrame(columns=colunas, data=valores)

# Verifique se a tabela contém dados
print(tabela)

# Salva a tabela em uma planilha Excel
tabela.to_excel('CTes_colunas.xlsx', index=False)