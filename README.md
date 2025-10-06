# Atividade Técnica — Funções em Python

Conjunto de funções para resolver as quatro perguntas propostas.

## Sumário
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Estrutura](#estrutura)
- [Uso Rápido](#uso-rápido)
  - [Pergunta 1](#pergunta-1)
  - [Pergunta 2](#pergunta-2)
  - [Pergunta 3](#pergunta-3)
  - [Pergunta 4](#pergunta-4)
- [Exemplos de Execução](#exemplos-de-execução)
- [Testes Rápidos](#testes-rápidos)
- [Licença](#licença)

---

## Requisitos
- Python 3.10+ (recomendado 3.11+)

## Instalação
Clone o repositório e, se desejar, crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows (PowerShell)
```

Não há dependências externas.

## Estrutura
- `funcoes.py` (sugestão de nome) contendo:
  - Pergunta 1: `comeca_b_termina_a`
  - Pergunta 2: `print_valor`
  - Pergunta 3: `min_turnos`, `prob_caminho_otimo`, `caminhos_sem_loop`, `analisa_tabuleiro`
  - Pergunta 4: `calcular_beneficios_rescisao` (e helpers internos)

---

## Uso Rápido

### Pergunta 1
**Determinar se uma string começa com 'B' e termina com 'A'.**
```python
def comeca_b_termina_a(s: str, case_insensitive: bool = False) -> bool:
    if case_insensitive:
        s = s.upper()
    return s.startswith('B') and s.endswith('A')
```

### Pergunta 2
**PA 11, 18, 25, …** — a₁ = 11, r = 7 → aₙ = 7n + 4
```python
def print_valor(x: int) -> int:
    if x < 1:
        raise ValueError("x deve ser >= 1 (a sequência começa em 1).")
    return 7 * x + 4
```

### Pergunta 3
**Tabuleiro unidirecional com roleta {1,2,3} equiprovável, N ≥ 3.**  
Partida na casa 1, meta na casa N. Se ultrapassar N, “dá a volta” e continua a partir da casa 1 com o excedente. Equivalentemente, precisamos somar **S = N − 1**.

Funções separadas + agregadora:
```python
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
    return count / (3 ** T)

def caminhos_sem_loop(N: int) -> int:
    if N < 3:
        raise ValueError("N mínimo é 3.")
    S = N - 1
    if S == 0: return 1
    if S == 1: return 1
    if S == 2: return 2
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
```

### Pergunta 4
**Cálculo de Férias proporcionais (com 1/3) e 13º proporcional.**  
Simplificações:
- Férias “zeram” a cada **aniversário** do emprego.
- 13º “zera” em **1º de janeiro**.
- Opção de contar mês por **≥15 dias** (padrão) ou apenas **meses completos**.

```python
from datetime import date

def _dias_no_mes(ano: int, mes: int) -> int:
    if mes == 12:
        return (date(ano+1,1,1) - date(ano,12,1)).days
    return (date(ano,mes+1,1) - date(ano,mes,1)).days

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

def calcular_beneficios_rescisao(salario: float, admissao: date, desligamento: date, regra_15_dias: bool = True) -> dict:
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
    ferias_com_terco = ferias_base * (4/3)
    decimo_terceiro = salario * (meses_13 / 12)
    return {
        "meses_ferias": meses_ferias,
        "meses_13": meses_13,
        "ferias_proporcionais_com_terco": round(ferias_com_terco, 2),
        "decimo_terceiro_proporcional": round(decimo_terceiro, 2),
        "total": round(ferias_com_terco + decimo_terceiro, 2),
    }
```

---

## Exemplos de Execução

```python
# Pergunta 1
comeca_b_termina_a("BELA")           # True
comeca_b_termina_a("bela")            # False
comeca_b_termina_a("bela", True)      # True

# Pergunta 2
print_valor(1)        # 11
print_valor(2)        # 18
print_valor(200)      # 1404
print_valor(254)      # 1782
print_valor(3542158)  # 24795110

# Pergunta 3
min_turnos(5)                 # 2
prob_caminho_otimo(5)         # 0.3333333333333333
caminhos_sem_loop(5)          # 7
analisa_tabuleiro(5)
# {'min_turnos': 2, 'prob_caminho_otimo': 0.3333333333333333, 'sem_loop_combinacoes': 7}

# Pergunta 4
from datetime import date
calcular_beneficios_rescisao(
    salario=5000.0,
    admissao=date(2023,4,10),
    desligamento=date(2025,10,15),
    regra_15_dias=True
)
```

---

## Testes Rápidos

```bash
python - <<'PY'
from datetime import date

def assert_eq(a,b): 
    assert a==b, f"esperado {b}, obtido {a}"

# Importe as funções do seu módulo 'funcoes.py'
# from funcoes import (comeca_b_termina_a, print_valor, min_turnos,
#                      prob_caminho_otimo, caminhos_sem_loop,
#                      analisa_tabuleiro, calcular_beneficios_rescisao)

# Q2
assert_eq(7*1+4, 11)
assert_eq(7*2+4, 18)
assert_eq(7*200+4, 1404)
assert_eq(7*254+4, 1782)
assert_eq(7*3542158+4, 24795110)

# Q3 (sanidade)
import math
def _min_turnos(N): return math.ceil((N-1)/3)
assert_eq(_min_turnos(3), 1)

print("OK")
PY
```
