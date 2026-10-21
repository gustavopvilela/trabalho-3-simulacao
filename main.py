import matplotlib.pyplot as plt
from distribuicoes import set_seed
from cenarios import cenario_1, cenario_2, cenario_3
from simulacao import rodar_monte_carlo


def plotar_resultados(cenario, resultados):
    """Gera histogramas de Custo e Duração para o cenário."""
    custos = resultados['custos']
    duracoes = resultados['duracoes']
    preco_fixo = cenario['contrato']['preco_fixo']
    prazo = cenario['contrato']['prazo']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f"Resultados da Simulação: {cenario['nome']}", fontsize=14)

    # Gráfico de Custos
    ax1.hist(custos, bins=50, color='skyblue', edgecolor='black')
    ax1.axvline(preco_fixo, color='red', linestyle='dashed', linewidth=2,
                label=f'Preço Contrato (R$ {preco_fixo:,.2f})')
    ax1.set_title('Distribuição do Custo Total')
    ax1.set_xlabel('Custo (R$)')
    ax1.set_ylabel('Frequência')
    ax1.legend()

    # Gráfico de Duração
    ax2.hist(duracoes, bins=50, color='lightgreen', edgecolor='black')
    ax2.axvline(prazo, color='red', linestyle='dashed', linewidth=2, label=f'Prazo Contrato ({prazo} dias)')
    ax2.set_title('Distribuição da Duração Total')
    ax2.set_xlabel('Dias')
    ax2.set_ylabel('Frequência')
    ax2.legend()

    plt.tight_layout()
    plt.show()



def plotar_dispersao_bivariada(cenario, resultados):
    """
    Gera um gráfico de dispersão correlacionando Custo vs Duração,
    dividindo os resultados em quadrantes de risco.
    """
    custos = resultados['custos']
    duracoes = resultados['duracoes']
    preco_fixo = cenario['contrato']['preco_fixo']
    prazo = cenario['contrato']['prazo']

    # Classificação de cores por quadrante
    cores = []
    for d, c in zip(duracoes, custos):
        if d <= prazo and c <= preco_fixo:
            cores.append('#2ca02c')  # Verde: No prazo e no orçamento
        elif d > prazo and c > preco_fixo:
            cores.append('#d62728')  # Vermelho: Atrasado e com prejuízo
        else:
            cores.append('#ff7f0e')  # Laranja: Estourou apenas um dos critérios

    plt.figure(figsize=(10, 6))

    # Plotagem dos pontos com transparência (alpha) para evidenciar a densidade
    plt.scatter(duracoes, custos, c=cores, alpha=0.4, edgecolors='none', s=15)

    # Linhas demarcatórias do contrato
    plt.axvline(x=prazo, color='black', linestyle='--', linewidth=1.5, label=f'Prazo Limite ({prazo} dias)')
    plt.axhline(y=preco_fixo, color='black', linestyle='-.', linewidth=1.5,
                label=f'Teto Orçamentário (R$ {preco_fixo:,.2f})')

    # Configurações visuais
    plt.title(f"Análise de Risco Bivariada: {cenario['nome']}", fontsize=14, pad=15)
    plt.xlabel('Duração Total (Dias)', fontsize=11)
    plt.ylabel('Custo Total (R$)', fontsize=11)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def plotar_boxplots_comparativos(cenarios, todos_resultados):
    """
    Gera diagramas de caixa normalizados (% em relação ao limite do contrato).
    """
    nomes = [c['nome'].split(':')[0] for c in cenarios]

    dados_custo_norm = []
    dados_duracao_norm = []

    # Normaliza os dados: (Valor / Limite do Contrato) * 100
    for cenario, res in zip(cenarios, todos_resultados):
        preco_fixo = cenario['contrato']['preco_fixo']
        prazo = cenario['contrato']['prazo']

        dados_custo_norm.append([(c / preco_fixo) * 100 for c in res['custos']])
        dados_duracao_norm.append([(d / prazo) * 100 for d in res['duracoes']])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 9))
    fig.suptitle('Análise Comparativa de Variância (Normalizada pelo Contrato)', fontsize=16)

    cores = ['#87CEEB', '#90EE90', '#FA8072']

    # Boxplot de Custos
    bplot1 = ax1.boxplot(dados_custo_norm, patch_artist=True, tick_labels=nomes)
    ax1.set_title('Desvio do Orçamento', pad=10)
    ax1.set_ylabel('Percentagem do Preço Fixo (%)')
    ax1.axhline(y=100, color='red', linestyle='--', linewidth=2, label='Teto Contratual (100%)')
    ax1.grid(True, axis='y', alpha=0.4, linestyle='--')
    ax1.legend()

    # Boxplot de Duração
    bplot2 = ax2.boxplot(dados_duracao_norm, patch_artist=True, tick_labels=nomes)
    ax2.set_title('Desvio do Cronograma', pad=10)
    ax2.set_ylabel('Percentagem do Prazo (%)')
    ax2.axhline(y=100, color='red', linestyle='--', linewidth=2, label='Prazo Máximo (100%)')
    ax2.grid(True, axis='y', alpha=0.4, linestyle='--')
    ax2.legend()

    # Aplicação de cores
    for bplot in (bplot1, bplot2):
        for patch, cor in zip(bplot['boxes'], cores):
            patch.set_facecolor(cor)
            patch.set_alpha(0.8)

    plt.tight_layout()
    plt.show()

def avaliar_decisao(cenario, resultados):
    """Gera a recomendação final de viabilidade."""
    prob = resultados['prob_prejuizo']
    multa = resultados['multa_media']
    crit = cenario['criterios']

    viavel = True
    motivos = []

    if prob > crit['max_prob_prejuizo']:
        viavel = False
        motivos.append(
            f"Risco de Prejuízo ({prob * 100:.2f}%) excede o limite de {crit['max_prob_prejuizo'] * 100:.0f}%")

    if multa > crit['max_multa_media']:
        viavel = False
        motivos.append(f"Multa média (R$ {multa:,.2f}) excede o limite estipulado (R$ {crit['max_multa_media']:,.2f})")

    print(f"\n{'=' * 50}")
    print(f"ANÁLISE DE DECISÃO: {cenario['nome'].upper()}")
    print(f"Probabilidade de Prejuízo: {prob * 100:.2f}%")
    print(f"Multa Média por Atraso: R$ {multa:,.2f}")
    print("-" * 50)

    if viavel:
        print(">>> DECISÃO RECOMENDADA: ACEITAR CONTRATO (VIÁVEL)")
    else:
        print(">>> DECISÃO RECOMENDADA: RECUSAR CONTRATO (INVIÁVEL)")
        for m in motivos:
            print(f"    - {m}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    # Garante a reproducibilidade estipulando a seed customizada que você criou
    set_seed(42)
    N_ITERACOES = 1000000

    cenarios = [cenario_1, cenario_2, cenario_3]

    todos_resultados = []

    for cenario in cenarios:
        print(f"Executando {N_ITERACOES} simulações para {cenario['nome']}...")
        resultados = rodar_monte_carlo(cenario, N_ITERACOES)
        avaliar_decisao(cenario, resultados)
        plotar_resultados(cenario, resultados)
        plotar_dispersao_bivariada(cenario, resultados)
        todos_resultados.append(resultados)

    plotar_boxplots_comparativos(cenarios, todos_resultados)