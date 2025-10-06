from datetime import date


def _dias_no_mes(ano: int, mes: int) -> int:
    if mes == 12:
        return (date(ano + 1, 1, 1) - date(ano, 12, 1)).days
    return (date(ano, mes + 1, 1) - date(ano, mes, 1)).days


def _meses_proporcionais(inicio: date, fim: date, regra_15_dias: bool) -> int:
    if fim < inicio:
        return 0
    meses = (fim.year - inicio.year) * 12 + (fim.month - inicio.month)
    if regra_15_dias:
        if fim.day >= 15:
            meses += 1
    else:
        if fim.day < inicio.day:
            meses -= 1
    return max(0, min(meses, 12))


def calcular_beneficios_rescisao(
    salario: float, admissao: date, desligamento: date, regra_15_dias: bool = True
) -> dict:
    if salario < 0:
        raise ValueError("salário inválido")
    if desligamento < admissao:
        raise ValueError("datas inválidas")
    aniv_ano = desligamento.year
    if (desligamento.month, desligamento.day) < (admissao.month, admissao.day):
        aniv_ano -= 1
    dia_ref = min(admissao.day, _dias_no_mes(aniv_ano, admissao.month))
    ultimo_aniv = date(aniv_ano, admissao.month, dia_ref)
    meses_ferias = _meses_proporcionais(ultimo_aniv, desligamento, regra_15_dias)
    inicio_ano = date(desligamento.year, 1, 1)
    meses_13 = _meses_proporcionais(inicio_ano, desligamento, regra_15_dias)
    ferias_base = salario * (meses_ferias / 12)
    ferias_com_terco = ferias_base * (4 / 3)
    decimo_terceiro = salario * (meses_13 / 12)
    return {
        "meses_ferias": meses_ferias,
        "meses_13": meses_13,
        "ferias_proporcionais_com_terco": round(ferias_com_terco, 2),
        "decimo_terceiro_proporcional": round(decimo_terceiro, 2),
        "total": round(ferias_com_terco + decimo_terceiro, 2),
    }
