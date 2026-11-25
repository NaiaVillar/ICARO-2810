from numpy import array

# datos de la Atmosfera Estandar (ISA)
altitudes_isa = array([0, 500, 1000, 1500, 2000, 2500])
densidades_isa = array([1.225, 1.167, 1.112, 1.058, 1.007, 0.957])


# Paso 1: buscamos un valor entre dos puntos. especificamente: 405 m. esta entre 0 m y 500 m, es decir, en el intervalo i = 0 (primer intervalo de la tabla).
def my_buscar_intervalo(x, xs):
    if x < xs[0] or x > xs[-1]:
        print("la altura esta fuera de la tabla ISA")
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            return i


# Paso 2: unir esos dos datos con una recta y evaluarla en x.
#   pendiente = (y1 - y0) / (x1 - x0)
#   y = y0 + pendiente * (x - x0)
def interpolar(x, xs, ys):
    i = my_buscar_intervalo(x, xs)
    x0 = xs[i]
    x1 = xs[i + 1]
    y0 = ys[i]
    y1 = ys[i + 1]
    pendiente = (y1 - y0) / (x1 - x0)
    return y0 + pendiente * (x - x0)


h = 405
rho = interpolar(h, altitudes_isa, densidades_isa)
print("la densidad del aire a", h, "m es", rho, "kg/m^3")