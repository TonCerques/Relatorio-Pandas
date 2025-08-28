import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('C:/pandas/PDA_2022-2024_1.5_Cursos.csv', encoding= 'cp1252', sep=';', header= 2)
print(df.head())

filtro = df['Turno'].value_counts()
noturno = df[df['Turno'] == 'NOTURNO']
qt = len(noturno)

filtro2 = df['Turno'].value_counts()
matutino = df[df['Turno'] == 'DIURNO']
qt2 = len(matutino)



plt.figure(figsize=(6, 4))
plt.bar(['NOTURNO'], [qt], color= 'blue')
plt.bar( ['DIURNO'], [qt2], color = 'green')

plt.title("Quantidade de turnos (NOTURNO/DIURNO)")
plt.xlabel("Turno")

plt.show()