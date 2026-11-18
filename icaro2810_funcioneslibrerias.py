
################# APARTADO 1

import numpy as np

M_calib = np.array([
    [1.05, 0.02, -0.01],
    [0.01, 0.98, 0.03],
    [-0.02, 0.01, 1.02]
])

V_medido = np.array([15.2, -4.5, 98.1])

aceleracion = np.linalg.solve(M_calib, V_medido)

print(aceleracion)

################# APARTADO 2
import numpy as np

q_tunel = np.array([500,1000,1500,2000,2500,3000])

F_drag_tunel = np.array([
    12.1,
    25.3,
    37.8,
    51.0,
    62.5,
    76.2
])

CDA, b = np.polyfit(q_tunel,
                    F_drag_tunel,
                    1)

print("CDA =", CDA)
print("Intercepto =", b)

#representarlo graficamente segun copilot sería:
# import numpy as np
# import matplotlib.pyplot as plt

# q_tunel = np.array([500,1000,1500,2000,2500,3000])

# F_drag_tunel = np.array([
#     12.1,
#     25.3,
#     37.8,
#     51.0,
#     62.5,
#     76.2
# ])

# CDA, b = np.polyfit(
#     q_tunel,
#     F_drag_tunel,
#     1
# )

# q_modelo = np.linspace(500,3000,100)

# F_modelo = CDA*q_modelo + b

# plt.scatter(
#     q_tunel,
#     F_drag_tunel,
#     color="red",
#     label="Datos túnel"
# )

# plt.plot(
#     q_modelo,
#     F_modelo,
#     color="blue",
#     label="Regresión lineal"
# )

# plt.xlabel("Presión dinámica (Pa)")
# plt.ylabel("Fuerza drag (N)")
# plt.legend()
# plt.grid()

# plt.show()


############ APARTADO 3:
import numpy as np

altitudes_isa = np.array([
    0,
    500,
    1000,
    1500,
    2000,
    2500
])

densidades_isa = np.array([
    1.225,
    1.167,
    1.112,
    1.058,
    1.007,
    0.957
])

valor = np.interp(
    405,
    altitudes_isa,
    densidades_isa
)

print(valor)

################### APARTADO 4
import numpy as np

t_tel = np.linspace(0,8,17)

x_tel = np.array([
0,48,93,137,178,
218,256,292,326,
359,390,419,448,
474,500,524,547
])

y_tel = np.array([
0,85,160,225,280,
325,360,385,400,
405,400,385,360,
325,280,225,160
])

vx = np.zeros(len(t_tel))
vy = np.zeros(len(t_tel))

dt = t_tel[1] - t_tel[0]

vx[0] = (x_tel[1]-x_tel[0])/dt
vx[-1] = (x_tel[-1]-x_tel[-2])/dt

vy[0] = (y_tel[1]-y_tel[0])/dt
vy[-1] = (y_tel[-1]-y_tel[-2])/dt

for i in range(1, len(t_tel)-1):

    vx[i] = (
        x_tel[i+1]-x_tel[i-1]
    )/(2*dt)

    vy[i] = (
        y_tel[i+1]-y_tel[i-1]
    )/(2*dt)

v = np.sqrt(vx**2 + vy**2)

# esta última parte no entiendo muy bien por qué deberíamos usar f-strings, he preguntado a la ia pero no consigo entenderlo del todo:

for i in range(len(t_tel)):

    print(
        f"t = {t_tel[i]:.1f} s  "
        f"vx = {vx[i]:.2f} m/s  "
        f"vy = {vy[i]:.2f} m/s  "
        f"v = {v[i]:.2f} m/s"
    )
