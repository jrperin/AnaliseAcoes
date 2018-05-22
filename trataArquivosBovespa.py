# -*- coding: utf-8 -*-

import sys
import csv
import glob

dirlist = glob.glob("./Bovespa/*.TXT")
dirlist.sort(reverse=True)

fileOut = './BovespaConsolidado/bovespa.csv'


from pathlib import Path


if Path(fileOut).is_file():
    
    # Remove cabecalho
    print("Removendo cabecalho antigo ... ")
    with open(fileOut, 'r') as f:
        lines = f.readlines()
    f.close()
    
    cont = 0
    with open(fileOut, 'w+') as f:
        for line in lines:
            cont += 1
            if line[:11]!="data,codbdi":
                f.write(line)
            else:
                print(line)
                print(cont)
    f.close()
    print("Fim remocao do cabecalho antigo")




with open(fileOut, 'a+', newline='', encoding='utf-8') as csvOut:
    print("Carregando arquivos TXT da Bovespa")
    #print("Processando ...", end="", flush=True)
    
    writer = csv.writer(csvOut, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #Grava cabecalho do CSV:
            
    lbData            = 'data'
    lbCd_bdi          = 'codbdi'
    lbCodneg          = 'codneg'
    lbTp_merc         = 'tpmerc'
    lbNome_emiss      = 'nomres'
    lbEspecifi_papel  = 'epeci'
    lbPrazo_termo     = 'prazot'
    lbMoeda_ref       = 'modref'
    lbP_abertura      = 'preabe'
    lbP_maximo        = 'premax'
    lbP_minimo        = 'premin'
    lbP_medio         = 'premed'
    lbP_ultimo        = 'preult'
    lbP_melhor_of_c   = 'preofc'
    lbP_melhor_of_v   = 'preofv'
    lbTot_neg         = 'totneg'
    lbTot_tit         = 'quatot'
    lbVol_tot         = 'voltot'
    lbPre_merc_op     = 'preexe'
    lbInd_corr_prec   = 'indopc'
    lbDt_venc_opc     = 'datven'
    lbFator_cot       = 'fatcot'
    lbPreco_pts_exerc = 'ptoexe'
    lbCod_isin        = 'codisi'
    lbNum_distr       = 'dismes'
    
    
    ''' Obs.: os papeis como PETR4, PETR3 sao do Tipo de Mercado = 10
    
        010 - A vista
        012 - Exercicio de opcoes de compra
        013 - Exercicio de opcoes de venda
        017 - Leilao
        020 - Fracionario
        030 - Termo
        050 - Futuro com retencao de ganho
        060 - Futuro com movimentacao continua
        070 - Opcoes de compra
        080 - Opcoes de venda
    
    '''
    
    '''
    # Deixar para gravar o cabecalho no final depois de ordenar o arquivo...
    
    writer.writerow([lbData, lbCd_bdi, lbCodneg, lbTp_merc, lbNome_emiss,
                     lbEspecifi_papel, lbPrazo_termo, lbMoeda_ref, lbP_abertura,
                     lbP_maximo, lbP_minimo, lbP_medio, lbP_ultimo, lbP_melhor_of_c, 
                     lbP_melhor_of_v, lbTot_neg, lbTot_tit, lbVol_tot, lbPre_merc_op, 
                     lbInd_corr_prec, lbDt_venc_opc, lbFator_cot, lbPreco_pts_exerc, 
                     lbCod_isin, lbNum_distr])
    '''
    
    registros = 0
    for file in dirlist:
        #print("...", end="", flush=True)
        with open(file, 'r', newline='', encoding='latin-1', errors='replace') as fileIn:
            print("Processando arquivo {0}".format(file))
            lines = fileIn.readlines()
           
            for line in lines:
                tipo_registro  = line[0:2].strip()                           #01 - N(02)      - TIPO DE REGISTRO
                
                if (tipo_registro == '01'):                
                    
                    data           = '{0}-{1}-{2}'.format(line[2:6],line[6:8],line[8:10]).strip() #02 - N(08)      - DATA DO PREGÃO
                    cd_bdi         = line[10:12].strip()                      #03 - X(02)      - CÓDIGO BDI
                    codneg         = line[12:24].strip()                      #04 - X(12)      - CÓDIGO DE NEGOCIAÇÃO DO PAPEL
                    tp_merc        = int(line[24:27].strip())                 #05 - N(03)      - TIPO DE MERCADO
                    nome_emiss     = line[27:39].strip()                      #06 - X(12)      - NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL
                    especifi_papel = line[39:49].strip()                      #07 - X(10)      - ESPECIFICAÇÃO DO PAPEL
                    prazo_termo    = line[49:52].strip()                      #08 - X(03)      - PRAZO EM DIAS DO MERCADO A TERMO
                    moeda_ref      = line[52:56].strip()                      #09 - X(04)      - MOEDA DE REFERÊNCIA
                    p_abertura     = float(line[56:69].strip()) / 100         #10 - N(11)V99   - PREÇO DE ABERTURA DO PAPEL - MERCADO NO PREGÃO
                    p_maximo       = float(line[69:82].strip()) / 100         #11 - N(11)V99   - PREÇO MÁXIMO DO PAPEL - MERCADO NO PREGÃO
                    p_minimo       = float(line[82:95].strip()) / 100         #12 - N(11)V99   - PREÇO MÍNIMO DO PAPEL - MERCADO NO PREGÃO
                    p_medio        = float(line[95:108].strip()) / 100        #13 - N(11)V99   - PREÇO MÉDIO DO PAPEL - MERCADO NO PREGÃO
                    p_ultimo       = float(line[108:121].strip()) / 100       #14 - N(11)V99   - PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL-MERCADO NO PREGÃO
                    p_melhor_of_c  = float(line[121:134].strip()) / 100       #15 - N(11)V99   - PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL - MERCADO
                    p_melhor_of_v  = float(line[134:147].strip()) / 100       #16 - N(11)V99   - PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL - MERCADO
                    tot_neg        = int(line[147:152].strip())               #17 - N(05)      - NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL - MERCADO NO PREGÃO
                    tot_tit        = int(line[152:170].strip())               #18 - N(18)      - QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
                    vol_tot        = float(line[170:188].strip()) / 100       #19 - N(16)V99   - VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
                    pre_merc_op    = float(line[188:201].strip()) / 100       #20 - N(11)V99   - PREÇO DE EXERCÍCIO PARA O MERCADO DE OPÇÕES OU VALOR DO CONTRATO PARA O MERCADO DE TERMO SECUNDÁRIO
                    ind_corr_prec  = int(line[201:202].strip())               #21 - N(01)      - INDICADOR DE CORREÇÃO DE PREÇOS DE EXERCÍCIOS OU VALORES DE CONTRATO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
                    dt_venc_opc    = int(line[202:210].strip())               #22 - N(08)      - DATA DO VENCIMENTO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
                    fator_cot      = int(line[210:217].strip())               #23 - N(07)      - FATOR DE COTAÇÃO DO PAPEL
                    preco_pts_exerc= float(line[217:230].strip()) / 1000000   #24 - N(11)V06   - PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO SECUNDÁRIO
                    cod_isin       = line[230:242].strip()                    #25 - X(12)      - CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL
                    num_distr      = int(line[242:245].strip())               #26 - N(03)      - NÚMERO DE DISTRIBUIÇÃO DO PAPEL
                    
                    
                    #print(line)
                    #print ("{0} - {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}".format(
                    #                tipo_registro, 
                    #                data, cd_bdi, codneg, tp_merc, nome_emiss,
                    #                especifi_papel, prazo_termo, moeda_ref, p_abertura,
                    #                p_maximo, p_minimo, p_medio, p_ultimo, p_melhor_of_c, p_melhor_of_v,
                    #                tot_neg, tot_tit, vol_tot, pre_merc_op, ind_corr_prec,
                    #                dt_venc_opc, fator_cot, preco_pts_exerc, cod_isin, num_distr
                    #       ))
                
                    
                    if (tp_merc == 10):
                        registros += 1
                        writer.writerow([data, cd_bdi, codneg, tp_merc, nome_emiss,
                                         especifi_papel, prazo_termo, moeda_ref, p_abertura,
                                         p_maximo, p_minimo, p_medio, p_ultimo, p_melhor_of_c, p_melhor_of_v,
                                         tot_neg, tot_tit, vol_tot, pre_merc_op, ind_corr_prec,
                                         dt_venc_opc, fator_cot, preco_pts_exerc, cod_isin, num_distr])
        
        fileIn.close()
        
csvOut.close()

print("{0} registros novos processados".format(registros))
print(" - - - Fim da carga - - - ")


print(" - - - Ordenando arquivo por data - - - ")
with open(fileOut, 'r') as f:
    sorted_file = sorted(f, reverse = True)
    print("Arquivo final contem {0} linhas (sem header)".format(len(sorted_file)))
f.close()


#save to a file
header = "data,codbdi,codneg,tpmerc,nomres,epeci,prazot,modref,preabe,premax,premin,premed,preult,preofc,preofv,totneg,quatot,voltot,preexe,indopc,datven,fatcot,ptoexe,codisi,dismes\n"

with open(fileOut, 'w+') as f:
    f.write(header)
    f.writelines(sorted_file)
f.close()

print(" - - - Fim Processamento ! - - - ")