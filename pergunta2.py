def print_valor(x: int) -> int:
    """
    Retorna o valor da posição x na sequência 11,18,25,...

    Exemplos:
    print_valor(1) -> 11
    print_valor(2) -> 18
    print_valor(200) -> 1404
    print_valor(254) -> 1782
    print_valor(3542158) -> 24795110
    """
    if x < 1:
        raise ValueError("x deve ser >= 1 (a sequência começa em 1).")
    return 7 * x + 4
