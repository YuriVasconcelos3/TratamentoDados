import csv


def tabela1():
  lista = []
  lista1 = []
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    arquivo = csv.reader(csvfile, delimiter = ',')
    for linha in arquivo:
      lista.append(linha)
    for c in range(0,12):
      lista1.append(lista[0][c])
      if c == 0:
        lista1.append('INT NOT NULL,')
      elif c == 1:
        lista1.append('INT NOT NULL,')
      elif c == 2:
        lista1.append('VARCHAR(60) NOT NULL,')
      elif c == 3:
        lista1.append('INT NOT NULL,')
      elif c == 4:
        lista1.append('VARCHAR(45) NOT NULL,')
      elif c == 5:
        lista1.append('VARCHAR(45) NOT NULL,')
      elif c == 6:
        lista1.append('VARCHAR(5),')
      elif c == 7:
        lista1.append('VARCHAR(45) NOT NULL,')
      elif c == 8:
        lista1.append('INT NOT NULL,')
      elif c == 9:
        lista1.append('DATETIME NOT NULL,')
      elif c == 10:
        lista1.append('VARCHAR(45) NOT NULL,')
      elif c == 11:
        lista1.append('DATETIME NOT NULL,')       
    
    lista1.append('PRIMARY KEY (_ID)')
    resposta = (' '.join(lista1))
  return (resposta)

def inserirdados():
  with open('atendimento.csv', "r", encoding='UTF-8-sig') as csvfile:
    lista = []
    lista1 = []
    list = []
    lista2 = []
    arquivo = csv.reader(csvfile, delimiter=',')
    for linha in arquivo:
      lista.append(linha)
      for c in linha:
        listaa = [x for x in linha]
      list.append(listaa)
    for cc in range(0,12):
      lista1.append(lista[0][cc])
    resposta = (', '.join(lista1))
    for cont in range(1,165):
      valor = ("', '".join(list[cont]))
      lista2 = [(f"Insert Into GRUPOSERVIÇO ({resposta}) values ('{valor}');" )]
    resp = ', '.join(map(str, lista2))
    return(resp)
print(inserirdados())