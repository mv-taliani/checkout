import math


def min_turnos(N: int) -> int:
    if N < 3:
        raise ValueError("N mínimo é 3.")
    return math.ceil((N - 1) / 3)


def prob_caminho_otimo(N: int) -> float:
    if N < 3:
        raise ValueError("N mínimo é 3.")
    S = N - 1
    q, r = divmod(S, 3)
    T = q if r == 0 else q + 1
    if r == 0:
        count = 1
    elif r == 1:
        count = (T * (T + 1)) // 2
    else:
        count = T
    return count / (3**T)


def caminhos_sem_loop(N: int) -> int:
    if N < 3:
        raise ValueError("N mínimo é 3.")
    S = N - 1
    if S == 0:
        return 1
    if S == 1:
        return 1
    if S == 2:
        return 2
    a, b, c = 1, 1, 2
    for _ in range(3, S + 1):
        a, b, c = b, c, a + b + c
    return c


def analisa_tabuleiro(N: int) -> dict:
    return {
        "min_turnos": min_turnos(N),
        "prob_caminho_otimo": prob_caminho_otimo(N),
        "sem_loop_combinacoes": caminhos_sem_loop(N),
    }
