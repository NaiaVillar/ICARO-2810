
import numpy as np
from scipy.integrate import trapezoid, simpson
from scipy.optimize import newton, bisect

import physics as ph
import mymath


def comparar(nombre, nuestro, ref, tol=1e-6):
    """Imprime el resultado de mymath y el de numpy/scipy, y si coinciden."""
    ok = np.allclose(nuestro, ref, rtol=tol, atol=tol)
    print(f"{nombre}\n  mymath : {nuestro}\n  numpy  : {ref}\n  -> {'OK' if ok else 'ERROR'}\n")


################# APARTADO 1: sistema lineal
ref = np.linalg.solve(ph.M_calib, ph.V_medido)
nuestro = mymath.resolver_sistema(ph.M_calib.tolist(), ph.V_medido.tolist())
comparar("APARTADO 1: aceleracion", nuestro, ref)

################# APARTADO 2: regresion lineal (F = CDA * q)
q, F = ph.q_tunel, ph.F_drag_tunel
ref = np.sum(q * F) / np.sum(q ** 2)
nuestro = mymath.ajuste_origen(q.tolist(), F.tolist())
comparar("APARTADO 2: CDA", nuestro, ref)

################# APARTADO 3: interpolacion
ref = np.interp(405, ph.altitudes_isa, ph.densidades_isa)
nuestro = mymath.interpolar(405, ph.altitudes_isa.tolist(), ph.densidades_isa.tolist())
comparar("APARTADO 3: rho(405 m)", nuestro, ref)

################# APARTADO 4: derivacion numerica
vx_ref = np.gradient(ph.x_tel, ph.t_tel)
vy_ref = np.gradient(ph.y_tel, ph.t_tel)
vx = mymath.derivar(ph.t_tel.tolist(), ph.x_tel.tolist())
vy = mymath.derivar(ph.t_tel.tolist(), ph.y_tel.tolist())
comparar("APARTADO 4: vx", vx, vx_ref)
comparar("APARTADO 4: vy", vy, vy_ref)

################# APARTADO 5: integracion numerica (energia disipada)
CDA = np.sum(q * F) / np.sum(q ** 2)
rho = np.interp(405, ph.altitudes_isa, ph.densidades_isa)
v = np.sqrt(vx_ref ** 2 + vy_ref ** 2)
P = CDA * 0.5 * rho * v ** 3

comparar("APARTADO 5: trapecios", mymath.trapecios(ph.t_tel.tolist(), P.tolist()),
         trapezoid(P, ph.t_tel))
comparar("APARTADO 5: Simpson", mymath.simpson(ph.t_tel.tolist(), P.tolist()),
         simpson(P, x=ph.t_tel))

################# APARTADO 6: busqueda de raices
def y(t):
    return 400 - 35 * (t - 5) - 150 * np.exp(-0.2 * (t - 5))


def dy(t):
    return -35 + 30 * np.exp(-0.2 * (t - 5))


comparar("APARTADO 6: Newton", mymath.newton(y, dy, 15.0), newton(y, 15.0, fprime=dy))
comparar("APARTADO 6: biseccion", mymath.biseccion(y, 5.0, 25.0), bisect(y, 5.0, 25.0))