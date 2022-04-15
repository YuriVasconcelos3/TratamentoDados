import csv
from codigospy import tabela1, inserirdados

def criartabela1():
    tabelaa = tabela1()
    return(f"create table GRUPOSERVIÇO ({tabelaa});")

