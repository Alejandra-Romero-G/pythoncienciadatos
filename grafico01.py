import matplotlib.pyplot as plt
x= ["Atletico de Madrid","Real Madrid", "Barcelona", "Betis"]
#valor el mercado
y = [ 30, 400, 66, 20]
# Para crear el grafico debemos darles los graficos mediante plt
#librería mediante plt.bar
plt.bar(x, y)
#perzonalizamos el grafico
plt.title("Grafico de baras")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")

plt.savefig('images/barras.png')
plt.show()