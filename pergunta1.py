def comeca_b_termina_a(s: str, case_insensitive: bool = False) -> bool:
    """
    True se a string começa com 'B' e termina com 'A'.

    case_insensitive=True faz a checagem ignorando maiúsc/minúsc.

    Exemplos:
    comeca_b_termina_a("BELA") -> True
    comeca_b_termina_a("bela") -> False
    comeca_b_termina_a("bela", case_insensitive=True) -> True
    """
    if case_insensitive:
        s = s.upper()
    return s.startswith("B") and s.endswith("A")
