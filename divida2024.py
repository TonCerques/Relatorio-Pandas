import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('C:/Users/WellingtondosSantosC/Downloads/divida/despesasPorProgramaAcao.csv', delimiter= ';')
pd.set_option('display.max_columns', None) 
pd.set_option('display.expand_frame_repr', False)


def limpar_valores(coluna):
    return (
        coluna.astype(str) 
              .str.replace("- ", "-", regex=False)  
              .str.replace(".", "", regex=False)  
              .str.replace(",", ".", regex=False)  
              .astype(float) 
    )


colunas_numericas = ["Valor Empenhado", "Valor Pago"]
for coluna in colunas_numericas:
    df[coluna] = limpar_valores(df[coluna])

# Garantir que a coluna "Mês Ano" seja string
df["Mês Ano"] = df["Mês Ano"].astype(str)

# Criar o gráfico
plt.figure(figsize=(12, 6))

plt.plot(df["Mês Ano"], df["Valor Empenhado"], marker='o', linestyle='-', label='Valor Empenhado', color='b')
plt.plot(df["Mês Ano"], df["Valor Pago"], marker='d', linestyle='-', label='Valor Pago', color='r')

plt.xlabel("Mês Ano")
plt.ylabel("Valores (Bilhões R$)")
plt.title("Evolução das Dívidas Públicas")
plt.legend()
plt.xticks(rotation=45)


def format_billions(value, _):
    return f'R$ {value / 1e9:.1f}B'

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_billions))

plt.grid(axis='y', linestyle='--', alpha=0.7)

pico_empenhado = df["Valor Empenhado"].idxmax()
pico_pago = df["Valor Pago"].idxmax()

crises = {
    pico_empenhado: "Alta na taxa de juros\nAumento da dívida",
    pico_pago: "Crise econômica\nAumento de gastos"
}

# Adicionar anotações nos picos
for indice, texto in crises.items():
    x = df["Mês Ano"].iloc[indice]
    y = max(df["Valor Empenhado"].iloc[indice], df["Valor Pago"].iloc[indice])

    plt.annotate(
        texto,
        xy=(x, y),
        xytext=(x, y + 30e9),  # Ajuste na posição vertical
        arrowprops=dict(facecolor='black', arrowstyle="->"),
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white")
    )

# Exibir o gráfico
plt.show()
