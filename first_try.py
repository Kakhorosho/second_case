import sympy as sy
import ru_local as ru
import matplotlib.pyplot as plt
import numpy as np
q = sy.Symbol("q")

def qd(q1, q2, p1, p2):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    pd = sy.Symbol("pd")
    print(f'{ru.DEMAND_FUNCTION} qd = {int(a)}{int(b)}pd')
    return a + b * pd


def p(q1, q2, p1, p2, q):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    return (q - a) / b
def tr(qx):
    px = p(150, 100, 50, 60, qx)
    tr = px * qx
    return tr
def mr(q):
    mr = sy.diff(tr(q), q)
    return mr
mr(q)