import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('C:/pandas/case1_inconsistent_clientes_fornecedores.csv', sep=',')
pd.set_option('display.max_columns', None) #RECONHECER TODAS AS COLUNAS
pd.set_option('display.expand_frame_repr', False)


dropaBase = df.drop(['ID', 'Nome', 'Tipo', 'Documento', 'Email', 'Telefone', 'Endereco','Status'], axis = 1)
duplicados = df.drop_duplicates()

#PREENCHER VALORES EM BRANCO
df = df.fillna("Não Informado")

filtro2 = df['Status'].value_counts().fillna('Não informado')
stD = df[df['Status'] == 'Desativo']
qt2 = len(stD)

filtro1 = df['Email'].value_counts().fillna('Não informado')
stE = df[df['Email']== 'email_invalid']
qt1 = len(stE)


#CONVERSÃO DE VARÍAVEL
def clean_and_convert_to_int(telefone):
    # Remover todos os caracteres não numéricos (mantendo apenas os números)
    telefone_limpo = ''.join(filter(str.isdigit, str(telefone)))
    return int(telefone_limpo) if telefone_limpo else None  # Retorna o valor limpo como inteiro

df['Telefone'] = df['Telefone'].apply(clean_and_convert_to_int) #OBJECT PRA INT E TIRAR OS SIMBOLOS

#SEPARAR O CEP DO ENDEREÇO
def extract_cep(endereco):
    match = re.search(r'\b\d{5}-?\d{3}\b', str(endereco))  # Procura o CEP no formato XXXXX-XXX
    return match.group(0) if match else None  # Retorna o CEP se encontrado, senão retorna None

# Aplicando a função para extrair o CEP e criando uma nova coluna 'CEP'
df['CEP'] = df['Endereco'].apply(extract_cep)

# Removendo o CEP do endereço original
df['Endereco'] = df['Endereco'].str.replace(r'\b\d{5}-\d{3}\b', '', regex=True).str.strip()

def formatar_documento(doc):
    """Formata CPF e CNPJ corretamente"""
    doc = re.sub(r'\D', '', str(doc))  # Remove caracteres não numéricos

    if len(doc) == 11:  # CPF: XXX.XXX.XXX-XX
        return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}"
    elif len(doc) == 14:  # CNPJ: XX.XXX.XXX/XXXX-XX
        return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}"
    
    return doc  # Retorna o próprio valor se não for CPF nem CNPJ

df['Documento'] = df['Documento'].apply(formatar_documento)

print(df.loc[5:15])