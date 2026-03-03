import matplotlib.pyplot as plt
equipos= ["Atletico de Madrid","Real Madrid", "Barcelona", "Betis"]
#valor el mercado
valores= [ 30, 400, 66, 20]
# Para crear el grafico debemos darles los graficos mediante plt
#librería mediante plt.bar
plt.pie(valores, labels = equipos)
#perzonalizamos el grafico
plt.title("Grafico de Tartas")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")

plt.savefig('images/circular.png')
plt.show()