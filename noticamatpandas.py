import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


#Conexao com o Banco
engine = create_engine("mysql+pymysql://root:root@localhost:3306/bavi")
conn = engine.raw_connection()  # Obter conexão bruta
cursor = conn.cursor() 
query_bavi = "SELECT nomeTime, vit_jog, der_jog FROM jogo INNER JOIN equipe ON id_equi_fk = id_equi"
cursor.execute("SELECT SUM(vit_jog + der_jog) / 2 FROM jogo")
quantidade_jogos = cursor.fetchone()[0]
cursor.close()
conn.close()

df = pd.read_sql(query_bavi, engine)

plt.figure(figsize=(10, 5))
plt.plot(df['nomeTime'], df['vit_jog'], marker = 'o', linestyle = '-', label = 'Vitórias', color = 'blue')
plt.plot(df['nomeTime'], df['vit_jog'], marker = 's', linestyle = '--', label = 'Vitórias', color = 'red')

plt.title("Estatísticas do BAVI")
plt.xlabel("Jogos")
plt.legend()


plt.show()


