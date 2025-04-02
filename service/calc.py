from math import factorial

def pl_wo_rep(k, n):
    if k > n:
        raise ValueError('Некорректные данные. Требуется: k <= n')
    return (factorial(n) / (factorial(n - k)))


def pl_w_rep(k, n):
    return n ** k


def pr_w_rep(n, *args):
    if len(args) != n:
        raise ValueError('Количество аргументов не равно n')
    elif n < 0:
        raise ValueError('Некорректные данные. Требуется: n >= 0')
    denominator = 1
    for arg in args:
        denominator *= factorial(arg)
    return (factorial(n) / denominator)


def pr_wo_rep(n):
    if n < 0:
        raise ValueError('Некорректные данные. Требуется: n >= 0')
    return (factorial(n))


def cm_wo_rep(k, n):
    if k > n:
        raise ValueError('Некорректные данные. Требуется: k <= n')
    return (factorial(n) / (factorial(k) * factorial(n - k)))


def cm_w_rep(k, n):
    if k > n:
        raise ValueError('Некорректные данные. Требуется: k <= n')
    return cm_wo_rep(k, n + k - 1)


def all_marked(k, m, n):
    if k >= m or m > n:
        raise ValueError('Некорректные данные. Требуется: k < m <= n')
    return cm_wo_rep(k, m) / cm_wo_rep(k, n)


def r_marked(r, k, m, n):
    if k >= m or k - r > n - m or m > n:
        raise ValueError('Некорректные данные. Требуется: k < m; k - r <= n - m; m <= n')
    return (cm_wo_rep(r, m) * cm_wo_rep(k - r, n - m) / cm_wo_rep(k, n))




               