import csv
from codigospy import tabela1, tabela2, tabela3

def criartabela1():
    tabelaa = tabela1()
    return(f"create table GRUPOSERVIÇO ({tabelaa});")

def criartabela2():
    tabelaa = tabela2()
    return(f"create table ENDEREÇO ({tabelaa});")

def criartabela3():
    tabelaa = tabela3()
    return(f"create table SITUACAO ({tabelaa});")
