from functions import *

#Listas
produtos = []
vendas = []
relTransfere = []
relDivergencias = []
relCanais = []

#Arquivos txt
produtos_txt = "c2_produtos.txt"
vendas_txt = "c2_vendas.txt"

#Function para gerar array do arq txt
buscarArq(produtos, produtos_txt)
buscarArq(vendas, vendas_txt)

#Function para geral rel transfere
criarRelTransfere(vendas, produtos, relTransfere)

#Function para geral rel divergencias
criarRelDivergencias(produtos, vendas, relDivergencias)

#Variáveis e Function para geral rel TotCanais
#Canais de atendimento
total_canal_repre = '1'
total_canal_web = '2'
total_canal_appA = '3'
total_canal_appI = '4'
criarRelTotCanais(vendas, relCanais, total_canal_repre)
criarRelTotCanais(vendas, relCanais, total_canal_web)
criarRelTotCanais(vendas, relCanais, total_canal_appA)
criarRelTotCanais(vendas, relCanais, total_canal_appI)

