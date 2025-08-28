import pandas as pd
import matplotlib.pyplot as plt


dados = {
    "id": range(1, 11),
    "tempoAtend": [1, 8, 4, 20, 31, 14, 5, 6, 7, 2],  
    "modoAtend": ['Chat', 'Telefone', 'Chat', 'Telefone', 'Telefone', 'Chat', 'Chat', 'Chat', 'Telefone', 'Chat']  
}

df = pd.DataFrame(dados)


media_tempo = df.groupby("modoAtend")["tempoAtend"].mean() #Ta calculando a media de tempo de atendimento, dentro do groupby


plt.figure(figsize=(15, 5))
plt.barh(media_tempo.index, media_tempo.values, color=['blue', 'green'])

plt.xlabel("Tempo Médio (min)")
plt.ylabel("Tipo de Atendimento")
plt.title("Tempo Médio de Atendimento por Tipo")
plt.legend()

plt.show()



