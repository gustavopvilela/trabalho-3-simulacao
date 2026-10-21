from fases_construcao import (preparacao_terreno, fundacao, laje,
                              alvenaria, acabamento_interno, pintura_externa)


def simular_projeto(cenario_config):
    """Executa UMA rodada completa da construção."""

    t1, c1 = preparacao_terreno(**cenario_config['fase1'])
    t2, c2 = fundacao(**cenario_config['fase2'])
    t3, c3 = laje(**cenario_config['fase3'])
    t4, c4 = alvenaria(**cenario_config['fase4'])
    t5, c5 = acabamento_interno(**cenario_config['fase5'])
    t6, c6 = pintura_externa(**cenario_config['fase6'])

    duracao_total = t1 + t2 + t3 + t4 + t5 + t6
    custo_base = c1 + c2 + c3 + c4 + c5 + c6

    # Cálculo da multa por atraso
    prazo = cenario_config['contrato']['prazo']
    atraso = max(0.0, duracao_total - prazo)
    multa = atraso * cenario_config['contrato']['multa_diaria']

    custo_total = custo_base + multa

    return duracao_total, custo_total, multa


def rodar_monte_carlo(cenario_config, n_iteracoes=10000):
    """Executa o projeto N vezes e consolida os resultados estatísticos."""

    resultados_duracao = []
    resultados_custo = []
    multas_com_atraso = []

    for _ in range(n_iteracoes):
        duracao, custo, multa = simular_projeto(cenario_config)
        resultados_duracao.append(duracao)
        resultados_custo.append(custo)

        # Só registramos a multa para a média SE houver atraso (multa > 0)
        if multa > 0:
            multas_com_atraso.append(multa)

    # Cálculo das métricas de viabilidade
    preco_fixo = cenario_config['contrato']['preco_fixo']
    cenarios_com_prejuizo = sum(1 for c in resultados_custo if c > preco_fixo)

    prob_prejuizo = cenarios_com_prejuizo / n_iteracoes
    multa_media = sum(multas_com_atraso) / len(multas_com_atraso) if multas_com_atraso else 0.0

    return {
        'duracoes': resultados_duracao,
        'custos': resultados_custo,
        'prob_prejuizo': prob_prejuizo,
        'multa_media': multa_media
    }