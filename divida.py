import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('C:/pandas/despesasPorProgramaAcao.csv', delimiter= ';')
pd.set_option('display.max_columns', None) #RECONHECER TODAS AS COLUNAS
pd.set_option('display.expand_frame_repr', False)


df["Valor Empenhado"] = df["Valor Empenhado"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float)
df["Valor Pago"] = df["Valor Pago"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float)
# Garantir que a coluna "Mês Ano" seja string

df["Mês Ano"] = df["Mês Ano"].astype(str)

plt.plot(df["Mês Ano"], df["Valor Empenhado"], marker='o', linestyle='-', label='Valor Empenhado', color='b')
plt.plot(df["Mês Ano"], df["Valor Pago"], marker='d', linestyle='-', label='Valor Pago', color='r')


plt.xlabel("Mês Ano")
plt.ylabel("Valor Empenhado")
plt.title("Evolução das Dívidas Públicas")
plt.legend()
plt.xticks(rotation=45) 


def format_billions(value, _):
    return f'R$ {value / 1e9:.1f}B'
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_billions))

plt.show()