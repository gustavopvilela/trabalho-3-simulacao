from distribuicoes import *
from models_distribuicoes import *

def preparacao_terreno (duracao: PERT, material: LogNormal, mao_obra: Normal):
    t1 = pert(duracao.o, duracao.m, duracao.p)
    cm1 = lognormal(material.media_ln, material.desvio_ln)
    cmo1 = normal(mao_obra.media, mao_obra.desvio)

    t_terreno = t1
    c_terreno = cm1 + cmo1

    return t_terreno, c_terreno

def fundacao (
    empresa: Bernoulli, # Chance de ser a empresa A
    evento_geologico: Bernoulli,
    duracao_a: PERT, duracao_b: PERT,
    material_a: LogNormal, material_b: LogNormal,
    mao_obra_a: Normal, mao_obra_b: Normal,
    t_geo: float, c_geo: float
):
    e_f = bernoulli(empresa.p)

    if e_f == 1:
        t2 = pert(duracao_a.o, duracao_a.m, duracao_a.p)
        cm2 = lognormal(material_a.media_ln, material_a.desvio_ln)
        cmo2 = normal(mao_obra_a.media, mao_obra_a.desvio)
    else:
        t2 = pert(duracao_b.o, duracao_b.m, duracao_b.p)
        cm2 = lognormal(material_b.media_ln, material_b.desvio_ln)
        cmo2 = normal(mao_obra_b.media, mao_obra_b.desvio)

    g = bernoulli(evento_geologico.p)

    if g == 1:
        t_fund = t2 + t_geo
        c_fund = cm2 + cmo2 + c_geo
    else:
        t_fund = t2
        c_fund = cm2 + cmo2

    return t_fund, c_fund

def laje (duracao: PERT, material: LogNormal, mao_obra: Normal):
    t3 = pert(duracao.o, duracao.m, duracao.p)
    cm3 = lognormal(material.media_ln, material.desvio_ln)
    cmo3 = normal(mao_obra.media, mao_obra.desvio)

    t_laje = t3
    c_laje = cm3 + cmo3

    return t_laje, c_laje

def alvenaria (
    risco_inspecao: Bernoulli,
    duracao: PERT, material: LogNormal,
    mao_obra: Normal,
    t_retrabalho: float, c_retrabalho: float
):
    t4 = pert(duracao.o, duracao.m, duracao.p)
    cm4 = lognormal(material.media_ln, material.desvio_ln)
    cmo4 = normal(mao_obra.media, mao_obra.desvio)
    r = bernoulli(risco_inspecao.p)

    if r == 1:
        t_alvenaria = t4 + t_retrabalho
        c_alvenaria = cm4 + cmo4 + c_retrabalho
    else:
        t_alvenaria = t4
        c_alvenaria = cm4 + cmo4

    return t_alvenaria, c_alvenaria

def acabamento_interno (duracao: PERT, material: LogNormal, mao_obra: Normal):
    t5 = pert(duracao.o, duracao.m, duracao.p)
    cm5 = lognormal(material.media_ln, material.desvio_ln)
    cmo5 = normal(mao_obra.media, mao_obra.desvio)

    t_acabamento = t5
    c_acabamento = cm5 + cmo5

    return t_acabamento, c_acabamento

def pintura_externa(
    escolha_terceirizada: Bernoulli,
    condicao_climatica: Bernoulli,
    duracao_a_bom: PERT,
    duracao_a_chuva: PERT,
    duracao_b_bom: PERT,
    duracao_b_chuva: PERT,
    material_a: LogNormal,
    material_b: LogNormal,
    mao_obra_a: Normal,
    mao_obra_b: Normal,
):
    e_p = bernoulli(escolha_terceirizada.p)
    w = bernoulli(condicao_climatica.p)

    if e_p == 1:
        material, mao_obra = material_a, mao_obra_a
        duracao = duracao_a_chuva if w == 1 else duracao_a_bom
    else:
        material, mao_obra = material_b, mao_obra_b
        duracao = duracao_b_chuva if w == 1 else duracao_b_bom

    cm6 = lognormal(material.media_ln, material.desvio_ln)
    cmo6 = normal(mao_obra.media, mao_obra.desvio)
    t6 = pert(duracao.o, duracao.m, duracao.p)

    t_pintura = t6
    c_pintura = cm6 + cmo6

    return t_pintura, c_pintura