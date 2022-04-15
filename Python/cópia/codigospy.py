import csv


def tabela1():
  lista = []
  lista1 = []
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    arquivo = csv.reader(csvfile, delimiter = ',')
    for linha in arquivo:
      lista.append(linha)
    for c in range(0,5):
      lista1.append(lista[0][c])
      if c == 0:
        lista1.append('INT NOT NULL,')
      if c == 1:
        lista1.append('INT NOT NULL,')
      if c == 2:
        lista1.append('VARCHAR(60) NOT NULL,')
      if c == 3:
        lista1.append('INT NOT NULL,')
      if c == 4:
        lista1.append('VARCHAR(45) NOT NULL,')
    
    lista1.append('ENDEREÇO_ID INT, SITUAÇAO_ID INT, PRIMARY KEY (_ID), FOREIGN KEY (ENDEREÇO_ID) REFERENCES ENDEREÇO(_ID), FOREIGN KEY (SITUAÇAO_ID) REFERENCES SITUACAO(_ID)')
    resposta = (' '.join(lista1))
  return (resposta)

def tabela2():
  lista = []
  lista1 = []
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    arquivo = csv.reader(csvfile, delimiter = ',')
    for linha in arquivo:
      lista.append(linha)
    lista1.append('_ID INT NOT NULL,')
    for c in range(5,8):
      lista1.append(lista[0][c])
      if c == 5:
        lista1.append('VARCHAR(45) NOT NULL,')
      if c == 6:
        lista1.append('VARCHAR(5),')
      if c == 7:
        lista1.append('VARCHAR(45) NOT NULL,')
    
    lista1.append('PRIMARY KEY (_ID)')

    resposta = (' '.join(lista1))
  return (resposta)

def tabela3():
  lista = []
  lista1 = []
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    arquivo = csv.reader(csvfile, delimiter = ',')
    for linha in arquivo:
      lista.append(linha)
    lista1.append('_ID INT NOT NULL,')
    for c in range(8,12):
      lista1.append(lista[0][c] )
      if c == 8:
        lista1.append('INT NOT NULL,')
      if c == 9:
        lista1.append('DATETIME NOT NULL,')
      if c == 10:
        lista1.append('VARCHAR(45) NOT NULL,')
      if c == 11:
        lista1.append('DATETIME NOT NULL,')
    
    lista1.append('PRIMARY KEY (_ID)')

    resposta = (' '.join(lista1))
  return (resposta)

def inserirdados():
  lista = listaa = lista1 = list = []
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=',')
    for linha in arquivo:
      lista.append(linha)
      for c in linha:
        listaa = [x for x in linha]
      list.append(listaa) 
    for cc in range(0,5):
      lista1.append(lista[0][cc])
    resposta = (', '.join(lista1))
    for cont in range(1,165):
      valor = ("', '".join(list[cont]))
      lista2 = [(f"Insert Into GRUPOSERVIÇO ({resposta}) values ('{valor}');" )]
      resp = ', '.join(map(str, lista2))
      print(resp)

print(inserirdados())
