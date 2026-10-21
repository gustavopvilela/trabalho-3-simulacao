from models_distribuicoes import PERT, Normal, LogNormal, Bernoulli

cenario_1 = {
    'nome': 'Cenário 1: Edifício Residencial',
    'contrato': {'preco_fixo': 19000000, 'prazo': 360, 'multa_diaria': 3000},
    'criterios': {'max_prob_prejuizo': 0.30, 'max_multa_media': 200000},
    'fase1': {
        'duracao': PERT(10, 14, 20), 'material': LogNormal(120000, 30000), 'mao_obra': Normal(150000, 35000)
    },
    'fase2': {
        'empresa': Bernoulli(0.6), 'evento_geologico': Bernoulli(0.1),
        'duracao_a': PERT(30, 40, 55), 'duracao_b': PERT(25, 34, 48),
        'material_a': LogNormal(2700000, 300000), 'material_b': LogNormal(3000000, 350000),
        'mao_obra_a': Normal(2300000, 250000), 'mao_obra_b': Normal(2100000, 260000),
        't_geo': 25, 'c_geo': 700000
    },
    'fase3': {
        'duracao': PERT(80, 100, 130), 'material': LogNormal(2400000, 300000), 'mao_obra': Normal(1800000, 200000)
    },
    'fase4': {
        'risco_inspecao': Bernoulli(0.12), 'duracao': PERT(60, 75, 95),
        'material': LogNormal(900000, 120000), 'mao_obra': Normal(1600000, 200000),
        't_retrabalho': 12, 'c_retrabalho': 300000
    },
    'fase5': {
        'duracao': PERT(80, 110, 150), 'material': LogNormal(2500000, 350000), 'mao_obra': Normal(2500000, 400000)
    },
    'fase6': {
        'escolha_terceirizada': Bernoulli(0.6), 'condicao_climatica': Bernoulli(0.2),
        'duracao_a_bom': PERT(12, 16, 22), 'duracao_a_chuva': PERT(16, 20, 28),
        'duracao_b_bom': PERT(10, 14, 18), 'duracao_b_chuva': PERT(14, 18, 24),
        'material_a': LogNormal(300000, 50000), 'material_b': LogNormal(320000, 60000),
        'mao_obra_a': Normal(280000, 40000), 'mao_obra_b': Normal(260000, 45000)
    }
}

cenario_2 = {
    'nome': 'Cenário 2: Galpão Logístico',
    'contrato': {'preco_fixo': 4300000, 'prazo': 150, 'multa_diaria': 5000},
    'criterios': {'max_prob_prejuizo': 0.25, 'max_multa_media': float('inf')}, # Sem limite explícito de multa no PDF
    'fase1': {
        'duracao': PERT(5, 7, 12), 'material': LogNormal(50000, 12000), 'mao_obra': Normal(80000, 18000)
    },
    'fase2': {
        'empresa': Bernoulli(0.7), 'evento_geologico': Bernoulli(0.08),
        'duracao_a': PERT(18, 22, 30), 'duracao_b': PERT(15, 19, 25),
        'material_a': LogNormal(1200000, 180000), 'material_b': LogNormal(1300000, 200000),
        'mao_obra_a': Normal(700000, 120000), 'mao_obra_b': Normal(650000, 110000),
        't_geo': 10, 'c_geo': 200000
    },
    'fase3': {
        'duracao': PERT(18, 24, 32), 'material': LogNormal(1000000, 150000), 'mao_obra': Normal(600000, 100000)
    },
    'fase4': {
        'risco_inspecao': Bernoulli(0.05), 'duracao': PERT(8, 10, 14),
        'material': LogNormal(125000, 25000), 'mao_obra': Normal(160000, 30000),
        't_retrabalho': 4, 'c_retrabalho': 60000
    },
    'fase5': {
        'duracao': PERT(14, 18, 26), 'material': LogNormal(200000, 35000), 'mao_obra': Normal(300000, 50000)
    },
    'fase6': {
        'escolha_terceirizada': Bernoulli(0.5), 'condicao_climatica': Bernoulli(0.3),
        'duracao_a_bom': PERT(6, 7, 9), 'duracao_a_chuva': PERT(8, 9, 12),
        'duracao_b_bom': PERT(5, 7, 8), 'duracao_b_chuva': PERT(7, 8, 11),
        'material_a': LogNormal(40000, 7000), 'material_b': LogNormal(45000, 8000),
        'mao_obra_a': Normal(50000, 8000), 'mao_obra_b': Normal(45000, 7000)
    }
}

cenario_3 = {
    'nome': 'Cenário 3: Centro de Saúde',
    'contrato': {'preco_fixo': 12500000, 'prazo': 300, 'multa_diaria': 4000},
    'criterios': {'max_prob_prejuizo': 0.15, 'max_multa_media': 50000},
    'fase1': {
        'duracao': PERT(8, 12, 18), 'material': LogNormal(90000, 20000), 'mao_obra': Normal(120000, 25000)
    },
    'fase2': {
        'empresa': Bernoulli(0.5), 'evento_geologico': Bernoulli(0.2),
        'duracao_a': PERT(28, 36, 48), 'duracao_b': PERT(25, 32, 44),
        'material_a': LogNormal(1800000, 220000), 'material_b': LogNormal(1900000, 260000),
        'mao_obra_a': Normal(1400000, 180000), 'mao_obra_b': Normal(1350000, 170000),
        't_geo': 30, 'c_geo': 800000
    },
    'fase3': {
        'duracao': PERT(30, 40, 55), 'material': LogNormal(1200000, 170000), 'mao_obra': Normal(900000, 120000)
    },
    'fase4': {
        'risco_inspecao': Bernoulli(0.15), 'duracao': PERT(50, 65, 85),
        'material': LogNormal(600000, 90000), 'mao_obra': Normal(1300000, 160000),
        't_retrabalho': 15, 'c_retrabalho': 400000
    },
    'fase5': {
        'duracao': PERT(70, 95, 130), 'material': LogNormal(2000000, 300000), 'mao_obra': Normal(2200000, 300000)
    },
    'fase6': {
        'escolha_terceirizada': Bernoulli(0.4), 'condicao_climatica': Bernoulli(0.25),
        'duracao_a_bom': PERT(10, 13, 16), 'duracao_a_chuva': PERT(14, 18, 22),
        'duracao_b_bom': PERT(9, 12, 15), 'duracao_b_chuva': PERT(12, 16, 20),
        'material_a': LogNormal(120000, 20000), 'material_b': LogNormal(130000, 22000),
        'mao_obra_a': Normal(100000, 18000), 'mao_obra_b': Normal(95000, 16000)
    }
}