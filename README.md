# Farm Optimizer

## Descrição

Este é um projeto para ajudar um trabalhador rural a organizar seu calendário de colheita anual de forma a obter o maior lucro possível com seus produtos. O trabalhador possui uma fazenda onde planta diferentes tipos de vegetais e frutas, além de criar alguns animais. Ele precisa levar em consideração as restrições de trabalho mensal e demanda de cada produto.

## Sumário

- [Limitações do problema](#limitações-do-problema)
- [Índices](#índices)
- [Variáveis](#variáveis)
- [Variáveis Auxiliares](#variáveis-auxiliares)
- [Dados](#dados)
  - [Para plantas (i)](#para-plantas-i)
  - [Para animais (k)](#para-animais-k)
- [Função Objetivo](#função-objetivo)
- [Restrições](#restrições)
- [Instalação](#instalação)
- [Uso](#uso)

### Limitações do problema

- O trabalhador tem um limite de horas de trabalho mensal.
- Existe um limite de demanda para cada produto.
- A venda dos produtos é feita diretamente pelo trabalhador.
- O sistema de irrigação é automático, reduzindo o tempo gasto com insumos vegetais.
- O tempo gasto com os animais inclui a coleta de insumos e distribuição de ração.
- Cada produto tem seu próprio limite de demanda.
- O trabalhador reserva uma porção da produção para consumo próprio.

### Índices

- **i**: varia de X a X (plantas)
- **j**: varia de X a X (ciclo)
- **k**: varia de X a X (animais)

### Variáveis

- **QCij**: Quantidade de uma planta _i_ para colher no mês _j_ (kg/mês)
- **QPij**: Quantidade de uma planta _i_ para plantar no mês _j_ (mudas/mês)

### Variáveis Auxiliares

- **LVij**: Lucro adquirido com a planta _i_ no mês _j_ (R$)
  - Fórmula: ((QCij _ ECij) – (PCi _ ECij)) \* Vi
- **LAkj**: Lucro adquirido com o animal _k_ no mês _j_ (R$)
  - Fórmula: (((NFk _ TPk _ 30) – PCk) _ Vk) – ((NMk + NFk) _ CAk)
- **TTMPj**: Total de tempo trabalhado no mês _j_ em plantas (horas)
  - Fórmula: Σi (QCij _ TCOLHi + QPij _ TPLANT + ((QCij – PCi _ ECij) / RPi) _ TVENDi)
- **TTMj**: Total de tempo trabalhado no mês _j_ (horas)
  - Fórmula: TTMPj + TTMAj
- **TTMAj**: Total de tempo trabalhado no mês _j_ em animais (horas)
  - Fórmula: Σk ((NFk _ TCk _ 30) + (((NFk _ TPk _ 30) / RA) \* TVENDk))

### Dados

- **HT**: Horas de trabalho diárias (horas/dia)
- **HM**: Horas usadas em manutenção (horas/mês)
- **DLM**: Dias de trabalho mensais (dias/mês)
- **RA**: Remessa de transporte para produtos animais (unidades)

#### Para plantas (i)

- **PCi**: Produção de _i_ que fica para casa (kg/mês)
- **Vi**: Valor de venda do produto _i_ (R$)
- **ECi**: Estação de colheita do produto _i_ (boolean[12])
- **TFRUi**: Tempo de frutificação do produto _i_ (meses)
- **TCOLHi**: Tempo de colheita do produto _i_ (horas)
- **TPLANTi**: Tempo de plantio do produto _i_ (horas)
- **TVENDi**: Tempo de venda do produto _i_ (horas)
- **CSi**: Custo de m do produto _i_ (R$)
- **PSi**: Produção por muda do produto _i_ (kg)
- **RPi**: Remessa de transporte para produtos vegetais (kg)
- **Mi**: Limitador máximo (kg)

#### Para animais (k)

- **PCk**: Produção animal que fica para casa (unidades/mês)
- **Vk**: Valor de venda do produto do animal _k_ (R$)
- **TCk**: Tempo de cuidado com o animal _k_ (horas/dia/animal)
- **CAk**: Custo por animal _k_ (R$/mês)
- **TVENDk**: Tempo de venda do produto _k_ (horas/remessa)
- **TPk**: Tempo de produção do animal _k_ (dias)
- **NFk**: Número de fêmeas de _k_ (inteiro)
- **NMk**: Número de machos de _k_ (inteiro)

### Função Objetivo

- **Lj**: Lucro adquirido no mês _j_ (R$)
  - Fórmula: Σi (LVij) + Σk (Lakj)

**MAX** Σj (Lj)

### Restrições

- Não trabalhar mais do que o limite de horas disponíveis:
  - ∀j | TTMj <= (HT \* DLM) - HM
- Colher no mínimo a quantidade de vegetais necessária para consumo próprio:
  - ∀i ∀j | QCij >= PCi \* ECij
- Obrigação de plantar o que está sendo colhido no mesmo mês (_j_):
  - ∀i ∀j | QCij <= QPi[j – TFRUi] \* PSi
- Não exceder o limite máximo de vegetais:
  - ∀i | Σj (QCij) <= Mi

## Instalação

1. Clone o repositório: `git clone https://github.com/CharlesLB/farm-optimizer.git`
2. Instale o python na sua máquina: [guia de instalação](https://python.org.br/index.html)
3. Instale o pip na sua máquina [guia de instalação](https://pip.pypa.io/en/stable/cli/pip_install/)
4. Instale o pyomo com o comando: `pip install pyomo`
5. Instale o glpk [caso seja windows](http://www.osemosys.org/uploads/1/8/5/0/18504136/glpk_installation_guide_for_windows10_-_201702.pdf) ou caso seja linux, rode o comando `apt-get install glpk-utils`

## Uso

1. Crie o arquivo json automaticamente com: `python -u ./scripts/create_json_file.py`
2. Rode a API com o comando: `python -u index.py input.json` ou `python -u index.py <input_name>`
