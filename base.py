import sympy as sy


def Qd(q1, q2, p1, p2):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    Pd = sy.Symbol("Pd")
    print(f'Demand function = Qd = {a} + {b}Pd')
    return a + b*Pd


def P(q1, q2, p1, p2, Q):
    b = (q2 - q1) / (p2 - p1)
    a = q1 - b * p1
    print(f'Reverse demand function = P = (Q - {a})/{b}')
    return (Q - a) / b

def TR(Qx):
    Px = P(150, 100, 50, 60, Qx)
    TR = Px * Qx
    return TR

def MR(Q):
    MR = sy.diff(TR(Q), Q)
    print(f'Marginal revenue = {MR}')
    return MR


def MC_previous(Q):
    return 2*Q - 172


def Qe():
    Q = sy.Symbol("Q")
    MR_1 = MR(Q)
    MC_1 = MC_previous(Q)
    Qe = sy.solve(MC_1 - MR_1, Q)
    print(f'Market equilibrium quantity = {Qe}')
    return Qe[0]


def Pe():
    Q_equal = Qe()
    Pe = P(150, 100, 50, 60, Q_equal)
    print(f'Market equilibrium price = {Pe}')
    return Pe


Q = sy.Symbol("Q")
MC = sy.integrate(MC_previous(Q), Q)


def TC(Qx, FC):
    MC_1 = MC.subs({Q: Qx})
    TC = MC_1 + FC
    print(f'Total costs  = {TC}')
    return TC


def Profit():
    Q_equal = Qe()
    TR_1 = TR(Q_equal)
    TC_1 = TC(Q_equal, 80)
    Profit = TR_1 - TC_1
    print(f'Maximum profit = {Profit}')
    return Profit


