
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

#https://www.portaldoagronegocio.com.br/agricultura/cafe/noticias/preco-do-cafe-dispara-66-em-12-meses-e-ruptura-de-produtos-aumenta-nos-supermercados
categorias = ['Ovo', 'Café', 'Açúcar', 'Azeite']
percentual = [ 19.7, 11.1, 10, 7.6]


#Gráfico de Barra
'''plt.figure(figsize=(10, 6))
plt.bar(categorias, percentual, )

plt.title("Aumento Percentual de Preço")
plt.xlabel("Alimentos")
plt.ylabel("Percentual de Preço")

# Exibindo o gráfico
plt.show()'''


#Gráfico de Curva
plt.plot(categorias, percentual, label="Aumento Percentual")

plt.title("Aumento Percentual de Preço")
plt.xlabel("Alimentos")
plt.ylabel("Preços")
plt.legend()
plt.show()