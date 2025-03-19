import matplotlib.pyplot as plt

X = ["Jan", "Fev", "Mars", "Avr", "Mai", "Juin", "Jui", "Aout", "Sep", "Oct", "Nov", "Dec"]

pluvio = [23.7, 70.9, 52.5, 38.6, 84.1, 57.8, 20.3, 61.4, 51.6, 90.6, 21.2, 33.9]
T_min = [3.8, 5.8, 7.2, 8.2, 11.4, 15.6, 18.1, 18.6, 13.3, 12.6, 7.7, 4]
T_max = [11.2, 13, 16.5, 18.4, 20.7, 25.6, 29.9, 29.8, 22.2, 20.6, 16.6, 10.6]

fig, ax1 = plt.subplots()

color = "tab:blue"
ax1.set_xlabel("Mois")
ax1.set_ylabel("Pluie (mm)")
ax1.bar(X, pluvio, color=color)
ax1.tick_params(axis="y", color=color)

ax2 = ax1.twinx()
ax2.set_ylabel("Température (°C)")
ax2.plot(X, T_min, color="green", label="Temp. min")
ax2.plot(X, T_max, color="red", label="Temp. max")
ax2.legend()

fig.tight_layout()
plt.show()
