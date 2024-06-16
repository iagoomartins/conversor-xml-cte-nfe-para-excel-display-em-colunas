- Este repositório contém um script Python para converter arquivos XML em um formato de planilha Excel. O script lê arquivos XML de um diretório específico, extrai dados específicos e armazena essas informações em um arquivo Excel.

** Requisitos **
Python
- Bibliotecas Python:
os
xmltodict
pandas
json
openpyxl

** Funcionalidades **:
- Lê arquivos XML de um diretório específico.
- Extrai dados específicos dos arquivos XML.
- Armazena os dados extraídos em um DataFrame do Pandas.
- Exporta os dados do DataFrame para um arquivo Excel.

** Como Usar **:
Coloque seus arquivos XML no diretório cte.
Execute o script.
O script irá gerar um arquivo Excel chamado CTes_colunas.xlsx no mesmo diretório do script, contendo as chaves extraídas dos arquivos XML.

** Observações **:
Certifique-se de que os arquivos XML estejam no formato esperado pelo script.
O script espera que a estrutura XML contenha as seções cteProc e subsequentes conforme descrito no código.
