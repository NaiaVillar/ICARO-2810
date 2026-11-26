import numpy as np


# Datos de telemetria del radar: tiempo (s) y posiciones (m)

t_tel = np.linspace(0, 8, 17)
x_tel = np.array([0, 48, 93, 137, 178, 218, 256, 292, 326,
                  359, 390, 419, 448, 474, 500, 524, 547])
y_tel = np.array([0, 85, 160, 225, 280, 325, 360, 385, 400,
                  405, 400, 385, 360, 325, 280, 225, 160])



# Derivacion numerica para tiempos igualmente espaciados

def derivar(t, posicion):
    N = len(t)
    dt = t[1] - t[0]
    velocidad = np.zeros(N)

    # Diferencia progresiva en el primer punto
    velocidad[0] = (posicion[1] - posicion[0]) / dt

    # Diferencias centrales en los puntos interiores
    for i in range(1, N - 1):
        velocidad[i] = (posicion[i + 1] - posicion[i - 1]) / (2 * dt)

    # Diferencia regresiva en el ultimo punto
    velocidad[-1] = (posicion[-1] - posicion[-2]) / dt

    return velocidad




# Calculo de las componentes y del modulo de la velocidad

def calcular_velocidades(t, x, y):
    vx = derivar(t, x)
    vy = derivar(t, y)
    v = np.sqrt(vx**2 + vy**2)
    return vx, vy, v

