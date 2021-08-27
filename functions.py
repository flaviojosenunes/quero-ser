def buscarArq(arrLeitura, arqTxt):
    with open(arqTxt, "r") as arqRegistro:
        for registro in arqRegistro.readlines():
            arrLeitura.append(registro.split(";"))

def criarRelTransfere(vendas, produtos, relTransfere):

    for valorProd in range(0, len(produtos)):
        varCodProd = produtos[valorProd][0]
        numAuxiliar = 0
        for valor in range(0, len(vendas)):
            if vendas[valor][0] == varCodProd and (vendas[valor][2] == '100' or vendas[valor][2] == '102'):
                total = int(vendas[valor][1]) + numAuxiliar
                numAuxiliar = total
        relTransfere.insert(valorProd, [produtos[valorProd][0],
                        produtos[valorProd][1],
                        produtos[valorProd][2],
                        str(total)])
    print(produtos)
    print(vendas)

    # Cálculo de estoque após venda
    with open("transfere.txt", "w") as arq_tranfere:
        arq_tranfere.write("Produto  QtCO  QtMin  QtVendas  Estq.aposVendas  Necess.  Transf.deArmp/CO\n")
        for valor in range(0, len(relTransfere)):
            estoque = int(relTransfere[valor][1]) - int(relTransfere[valor][3])
            relTransfere[valor].insert(4, str(estoque))

        # Cálculo de Necessidade
            necess = int(relTransfere[valor][2]) - estoque
            if necess < 0:
                necess = 0
            relTransfere[valor].insert(5, str(necess))

            # Transf. de arm p/ CO
            if necess > 1 and necess < 10:
                relTransfere[valor].insert(6, '10')
            else:
                relTransfere[valor].insert(6, str(necess))

            arq_tranfere.write(relTransfere[valor][0] + "    " + relTransfere[valor][1] + "   " + relTransfere[valor][2].rstrip() + "    " + str(relTransfere[valor][3]) + "       " + str(relTransfere[valor][4]) + "              " + relTransfere[valor][5] + "        " + relTransfere[valor][6] + "\n")

    print(relTransfere)

def criarRelDivergencias(produtos, vendas, relDivergencias):
    for valor in range(0, len(vendas)):
        #Encontrar divergências
        if vendas[valor][2] == '100' or vendas[valor][2] == '102':
            var = 0
        elif vendas[valor][2] == '190':
            number_190 = valor + 1
            relDivergencias.insert(valor, "Linha " + str(number_190) + " - Venda nao finalizada")
        elif vendas[valor][2] == '135':
            number_135 = valor + 1
            relDivergencias.insert(valor, "Linha " + str(number_135) + " - Venda cancelada")
        elif vendas[valor][2] == '999':
            number_999 = valor + 1
            relDivergencias.insert(valor, "Linha " + str(number_999) + " - Erro desconhecido. Acionar equipe de TI")
        else:
            number_desc_cod = valor + 1
            relDivergencias.insert(valor, "Linha " + str(number_desc_cod) + " - Status "+str(vendas[valor][2])+" nao encontrado" + str(vendas[valor][0]))

        arrayteste = []
        for valor2 in range(0, len(produtos)):
            arrayteste.append(produtos[valor2][0])

        if vendas[valor][0] in arrayteste:
            print('Okay')
        else:
            number_desc = valor + 1
            relDivergencias.insert(valor, "Linha " + str(number_desc) + " - Codigo de Produto nao encontrado " + str(
                vendas[valor][0]))

        with open("divergencias.txt", "w") as arq_divergencias:
            for valor_div in range(0, len(relDivergencias)):
                arq_divergencias.write(relDivergencias[valor_div] + "\n")

    print(relDivergencias)

def criarRelTotCanais(vendas,totcanais, num_canal):
    num_auxiliar_canal = 0
    for valor in range(0, len(vendas)):
        if vendas[valor][3].rstrip() == num_canal and (vendas[valor][2] == '100' or vendas[valor][2] == '102'):
            total_canal = int(vendas[valor][1]) + num_auxiliar_canal
            num_auxiliar_canal = total_canal

    if num_canal == '1':
        totcanais.insert(valor, "1 - Representante             "+str(total_canal))
    elif num_canal == '2':
            totcanais.insert(valor, "2 - Website                   "+str(total_canal))
    elif num_canal == '3':
            totcanais.insert(valor, "3 - App movel Android         "+str(total_canal))
    elif num_canal == '4':
            totcanais.insert(valor, "4 - App movel Iphone           "+str(total_canal))

    with open("totcanais.txt", "w") as arq_totcanais:
        arq_totcanais.write("Quantidades de Vendas por cana\n\n")
        arq_totcanais.write("Canal                    QtVendas\n")
        for valor_tot in range(0, len(totcanais)):
            arq_totcanais.write(totcanais[valor_tot] + "\n")
    print(totcanais)

