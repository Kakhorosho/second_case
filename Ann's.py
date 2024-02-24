import sympy as sy


def qd(q1, q2, p1, p2):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    pd = sy.Symbol("pd")
    print(f'Demand function = qd = {a} + {b}pd')
    return a + b*pd


def p(q1, q2, p1, p2, q):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    print(f'Reverse demand function = p = (q - {a})/{b}')
    return (q - a) / b

def tr(qx):
    px = p(150, 100, 50, 60, qx)
    tr = px * qx
    return tr

def mr(q):
    mr = sy.diff(tr(q), q)
    print(f'Marginal revenue = {mr}')
    return mr


def mc_previous(q):
    return 2*q - 172


def qe():
    q = sy.Symbol("q")
    mr_1 = mr(q)
    mc_1 = mc_previous(q)
    qe = sy.solve(mc_1 - mc_1, q)
    print(f'Market equilibrium quantity = {qe}')
    return qe[0]


def pe():
    q_equal = qe()
    pe = p(150, 100, 50, 60, q_equal)
    print(f'Market equilibrium price = {pe}')
    return pe


q = sy.Symbol("q")
mc = sy.integrate(mc_previous(q), q)


def tc(qx, fc):
    mc_1 = mc.subs({q: qx})
    tc = mc_1 + fc
    print(f'Total costs  = {tc}')
    return tc


def profit():
    q_equal = qe()
    tr_1 = tr(q_equal)
    tc_1 = tc(q_equal, 80)
    profit = tr_1 - tc_1
    print(f'Maximum profit = {profit}')
    return profit


qd(150, 100, 50, 60)
p(150, 100, 50, 60, q)
mr(q)
qe()
pe()
tc(q, 80)
profit()