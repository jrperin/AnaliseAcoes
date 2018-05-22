#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 03:12:40 2018

@author: jrperin
"""
import requests, zipfile, io, time, glob, os

#  Series Diarias
#  bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_D02042018.zip

#  Series Mensais
#  bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_M012018.zip


# Series Anuais
urlAno = 'http://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A'
#    bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2017.ZIP
#    1986 -> 2018

# Series Mensais
urlMes = 'http://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_M'

# Series Diarias
urlDia = 'http://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_D'

'''
anos =  [
            1986, 1987, 1988, 1989,
            1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
            2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
            2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017
        ]
'''


anos  = [    ]
meses = [ "042018"  ]
dias  = [ "02052018", "03052018"  ]

# Baixa anos ------------------------------------------------
print("\nBaixando os anos\n")
for ano in anos:
    url = '{0}{1}.ZIP'.format(urlAno, ano)
    print('Pegando:  {0}'.format(url))
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./Bovespa/ano')
    print('Ano {0} processado'.format(ano))
    time.sleep(5)

# Baixa meses ------------------------------------------------

print("\nBaixando os meses\n")
for mes in meses:
    url = '{0}{1}.ZIP'.format(urlMes, mes)
    print('Pegando:  {0}'.format(url))
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./Bovespa/mes')
    print('Mes {0} processado'.format(mes))
    time.sleep(5)


# Baixa Dias ------------------------------------------------

print("\nBaixando os dias\n")
for dia in dias:
    url = '{0}{1}.ZIP'.format(urlDia, dia)
    print('Pegando:  {0}'.format(url))
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./Bovespa/dia')
    print('Dia {0} processado'.format(dia))
    time.sleep(5)


print('Acertando nomes dos arquivos de ano...')

files = glob.glob("./Bovespa/ano/COTAHIST.A*")
files.sort()

for file in files:
    newName = '{0}.TXT'.format(file.replace(".A", "_A"))
    print("Renomeando de '{0}' para '{1}'".format(file, newName))

    os.rename(file, newName)


print('FIM ...')
