import pandas as pd
import json
from sqlalchemy import create_engine

'''dados = {
    "nome": ["Ana", "Carlos", "Bruna"],
    "idade": [25, 30, 22],
    "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

# Lendo o JSON para um DataFrame
df = pd.read_json("dados.json")
print(df)'''


engine = create_engine("mysql+pymysql://root:root@localhost:3306/academia")

query_Alu = "SELECT * FROM Aluno"
query_Tre = "SELECT * FROM Treino"
query_Exe = "SELECT * FROM Exercicio"
query_ATrei = "SELECT * FROM Aluno_Treino"

Aluno_df = pd.read_sql(query_Alu, con=engine) 
Treino_df = pd.read_sql(query_Tre, con=engine) 
Exercicio_df = pd.read_sql(query_Exe, con=engine) 
AluTreino_df = pd.read_sql(query_ATrei, con=engine) 


Aluno_df.to_json("Aluno.json", orient="records", indent=4)
Treino_df.to_json("Treino.json", orient="records", indent=4)
Exercicio_df.to_json("Exercicio.json", orient="records", indent=4)
AluTreino_df.to_json("Aluno_Treino.json", orient="records", indent=4)

# Exibir os JSONs salvos
print("Aluno.json:", json.dumps(json.load(open("Aluno.json")), indent=4))
print("Treino.json:", json.dumps(json.load(open("Treino.json")), indent=4))
print("Exercicio.json:", json.dumps(json.load(open("Exercicio.json")), indent=4))
print("Aluno_Treino.json:", json.dumps(json.load(open("Aluno_Treino.json")), indent=4))

