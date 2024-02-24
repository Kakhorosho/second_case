# Part of case-study
# Developer: Rusakova Margarita
#            Kosheleva Ann
#            Markelov Egor
#            Sokolova Sofia
import ru_local as ru

print(ru.TASK)
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


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


def mc_previous(q):
    return 2 * q - 172


def qe():
    q = sy.Symbol("q")
    mr_1 = mr(q)
    mc_1 = mc_previous(q)
    qe = sy.solve(mc_1 - mr_1, q)
    return qe[0]


def pe():
    q_equal = qe()
    pe = p(150, 100, 50, 60, q_equal)
    return pe


q = sy.Symbol("q")
mc = sy.integrate(mc_previous(q), q)


def tc(qx, fc):
    mc_1 = mc.subs({q: qx})
    tc = mc_1 + fc
    return tc


def profit():
    q_equal = qe()
    tr_1 = tr(q_equal)
    tc_1 = tc(q_equal, 80)
    profit = tr_1 - tc_1
    profit = int(profit)
    return profit


def profit_print():
    q_equal = qe()
    tr_1 = tr(q_equal)
    tc_1 = tc(q_equal, 80)
    profit = tr_1 - tc_1
    profit = int(profit)
    print(f'{ru.MAXIMUM_PROFIT} {profit} {ru.CURRENCY}')
    return profit


def p_print(q1, q2, p1, p2, q):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    print(f'{ru.REVERSE_DEMAND_FUNCTION} p = (q - {int(a)})/{int(b)}')
    return (q - a) / b


def mr_print(q):
    mr = sy.diff(tr(q), q)
    print(f'{ru.MARGINAL_REVENUE} {mr}')
    return mr


def qe_print():
    q = sy.Symbol("q")
    mr_1 = mr(q)
    mc_1 = mc_previous(q)
    qe = sy.solve(mc_1 - mr_1, q)
    qe = int(qe[0])
    print(f'{ru.MARKET_EQUILIBRIUM_QUANTITY} {qe} {ru.QOODS}')
    return qe


def pe_print():
    q_equal = qe()
    pe = p(150, 100, 50, 60, q_equal)
    pe = int(pe)
    print(f'{ru.MARKET_EQUILIBRIUM_PRICE} {pe} {ru.CURRENCY}')
    return pe


def tc_print(qx, fc):
    mc_1 = mc.subs({q: qx})
    tc = mc_1 + fc
    print(f'{ru.TOTAL_COSTS} {tc}')
    return tc


def days(qe, a_1, a_n):
    n = int((2 * qe) / (a_1 + a_n))
    print(f'{ru.AMOUNT_DAYS} {n} {ru.NAME_DAYS}')
    return n


def qd_new(q1, q2, p1, p2, new_volume):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1 + new_volume
    pd = sy.Symbol("pd")
    print(f'{ru.NEW_DEMAND_FUNCTION} qd = {int(a)}{int(b)}pd')
    return a + b * pd


def p_new(q1, q2, p1, p2, q, new_volume):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1 + new_volume
    return (q - a) / b


def p_new_print(q1, q2, p1, p2, q, new_volume):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1 + new_volume
    print(f'{ru.NEW_REVERSE_DEMAND_FUNCTION} p = (q - {int(a)})/{int(b)}')
    return (q - a) / b


def tr_new(qx_new):
    px_new = p_new(150, 100, 50, 60, qx_new, 300)
    tr_new = px_new * qx_new
    return tr_new


def mr_new(q):
    mr_new = sy.diff(tr_new(q), q)
    return mr_new


def mr_new_print(q):
    mr_new = sy.diff(tr_new(q), q)
    print(f'{ru.NEW_MARGINAL_REVENUE} {mr_new}')
    return mr_new


def qe_new():
    q = sy.Symbol("q")
    mr_new_1 = mr_new(q)
    mc_1 = mc_previous(q)
    qe_new = sy.solve(mc_1 - mr_new_1, q)
    return qe_new[0]


def qe_new_print():
    q = sy.Symbol("q")
    mr_new_1 = mr_new(q)
    mc_1 = mc_previous(q)
    qe_new = sy.solve(mc_1 - mr_new_1, q)
    qe_new = int(qe_new[0])
    print(f'{ru.NEW_MARKET_EQUILIBRIUM_QUANTITY} {qe_new} {ru.QOODS}')
    return qe_new


def pe_new():
    q_equal_new = qe_new()
    pe_new = p_new(150, 100, 50, 60, q_equal_new, 300)
    return pe_new


def pe_new_print():
    q_equal_new = qe_new()
    pe_new = p_new(150, 100, 50, 60, q_equal_new, 300)
    print(f'{ru.NEW_MARKET_EQUILIBRIUM_PRICE} {int(pe_new)} {ru.CURRENCY}')
    return pe_new


def new_profit():
    q_equal_new = qe_new()
    tr_1_new = tr_new(q_equal_new)
    tc_1 = tc(q_equal_new, 80)
    new_profit = tr_1_new - tc_1
    new_profit = int(new_profit)
    return new_profit


def new_profit_print():
    q_equal_new = qe_new()
    tr_1_new = tr_new(q_equal_new)
    tc_1 = tc(q_equal_new, 80)
    new_profit = tr_1_new - tc_1
    new_profit = int(new_profit)
    print(f'{ru.NEW_MAXIMUM_PROFIT} {new_profit} {ru.CURRENCY}')
    return new_profit


print(ru.POINT_A)
qd(150, 100, 50, 60)
p_print(150, 100, 50, 60, q)
mr_print(q)
qe_print()
pe_print()
tc_print(q, 80)
profit_print()
print(ru.POINT_B)
days(105, 1, 14)
print(ru.POINT_C)
qd_new(150, 100, 50, 60, 300)
p_new_print(150, 100, 50, 60, q, 300)
mr_new_print(q)
qe_new_print()
pe_new_print()
new_profit_print()
print(f'{ru.CHANGE_PROFIT} {new_profit() - profit()} {ru.CURRENCY}')

plt.figure()
plt.xlabel('Q')
plt.ylabel('P')

q_value = np.linspace(0, 200, 400)

profit_value = [tr(q) - tc(q, 80) for q in q_value]
plt.plot(q_value, profit_value)
plt.text(-8, 3000, 'Profit')

mc_value = [mc_previous(q) for q in q_value]
plt.plot(q_value, mc_value)
plt.text(200, 500, 'MC')

q1 = 150
q2 = 100
p1 = 50
p2 = 60
b = (q2 - q1) / (p2 - p1)
a = q1 - b * p1
p1 = []
q1 = []

for i in range(0, 200):
    p1.append(i)
    q1.append(a + b * i)
plt.plot(p1, q1)
plt.text(200, -1000, 'Qd')

tr_value = [tr(q) for q in q_value]
plt.plot(q_value, tr_value)
plt.text(200, 8500, 'TR')

mr_value = np.gradient(tr(q_value), q_value)
plt.plot(q_value, mr_value)
plt.text(200, -300, 'MR')

q_new_value = np.linspace(165, 210, 400)
tc_value = [tc(q, 80) for q in q_new_value]
plt.plot(q_new_value, tc_value)
plt.text(205, 6000, 'TC')

# Task C
q1 = 150
q2 = 100
p1 = 50
p2 = 60
b = (q2 - q1) / (p2 - p1)
a = q1 - b * p1 + 300
p1 = []
q1 = []

for i in range(0, 200):
    p1.append(i)
    q1.append(a + b * i)
plt.plot(p1, q1)
plt.text(25, 1000, "Qd'")

q_new_value_1 = np.linspace(0, 200, 400)
tr_value_new = [tr_new(q) for q in q_new_value_1]
plt.plot(q_new_value_1, tr_value_new)
plt.text(105, 13500, "TR'")

profit_value_new = [tr_new(q) - tc(q, 80) for q in q_value]
plt.plot(q_value, profit_value_new)
plt.text(90, 20000, "Profit'")

plt.show()
