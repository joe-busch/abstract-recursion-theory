"""
Simulates continuation passing style and wraps intermediate steps of
computations in thunks before sequentially bouncing them off a trampoline.
Decides which computation converges in the fewest number of steps even
if one of the computations does not converge. Can be viewed as a sort of
analogue to the Stage Comparison Theorem and could be used to implement
parallel or.

"""

import operator


def cps_eq0(a, f):
    return lambda: f(operator.eq(a, 0))


def cps_dec_a(a, f):
    return lambda: f(a-1)


def cps_inc_a(a, f):
    return lambda: f(a+1)


def cps_countdown1(a, f):
    return lambda: cps_eq0(a, lambda x: f(a) if x else cps_inc_a(a, lambda x: cps_countdown1(x, f)))


def cps_countdown2(a, f):
    return lambda: cps_eq0(a, lambda x: f(a) if x else cps_dec_a(a, lambda x: cps_countdown2(x, f)))


def interweave(f1, f2):
    if callable(f1):
        f1 = f1()
    if callable(f2):
        f2 = f2()

    interweave(f1, f2)


def init_countdown1(x):
    print('countdown1 won')
    exit()


def init_countdown2(x):
    print('countdown2 won')
    exit()


interweave(lambda: cps_countdown1(5, lambda x: init_countdown1(x)),
           lambda: cps_countdown2(10, lambda x: init_countdown2(x)))
