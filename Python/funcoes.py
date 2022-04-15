import MySQLdb
from sqlite3 import Cursor
from criartabela import criartabela1
import csv
#crud: criar, ler, atualizar e remover

#Ação de conectar
def conectar():
    print('Conectar ao  servidor...')
    try:
        conn = MySQLdb.connect(db='python', host='localhost', user='root', password='Kkdheartshapedbox!1')
        return conn

    except MySQLdb.Error as e:
        print('Erro:{}'.format(e))

#Ação de desconectar
def desconectar(conn):
    if conn:
        conn.close()

def createtable():
    conn = conectar()
    cursor = conn.cursor() 
    
    cursor.execute(f'{criartabela1()}')
    cursor.execute('show tables')
    okay = cursor.fetchall()

    if len(okay) > 0:
        print('Tabelas criadas')
    else:
        print('Ops, algo deu errado :/.')
    desconectar(conn)

def inserirdefault():
    conn = conectar()
    cursor = conn.cursor() 
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
            cursor.execute(f'{resp}')
            conn.commit()

    desconectar(conn)

#funcao de inserir registros
def inserir():
    conn = conectar()
    cursor = conn.cursor()
    descricao = input('Inserir valores separadas por vírgula e aspas:')
    cursor.execute("""INSERT INTO GRUPOSERVIÇO (_id, GRUPOSERVICO_CODIGO, GRUPOSERVICO_DESCRICAO, SERVICO_CODIGO,
     SERVICO_DESCRICAO, LOGRADOURO, NUMERO, BAIRRO, RPA, DATA_DEMANDA, SITUACAO, DATA_ULT_SITUACAO)
     VALUES ({})""".format(descricao))
    conn.commit()

    if cursor.rowcount == 1:
        print('o tipo de produto {} foi inserido!'.format(descricao))
    else:
        print('Não foi inserido nenhum TIPO DE PRODUTO!')

    desconectar(conn)

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM GRUPOSERVIÇO')
    produtos = cursor.fetchall()
    cont = 0
    if len(produtos) > 0:
        print('Listar o tipo do serviço')
        for produto in produtos:
            print('id:{}'.format(produto[0]))
            print('descricao:{}'.format(produto[2]))            
    else:
        print('não tipo produto cadastrado!!!!')
    
    desconectar(conn)

def atualizar():
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Isira o ID do registro a ser atualizado:'))
    nova_descricao = input('Insira o novo valor da para DESCRIÇÃO:')
    cursor.execute("UPDATE gruposerviço SET _id = '{}' WHERE _id ={}".format(nova_descricao, codigo))
    conn.commit()

    desconectar(conn)

def deletar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Insirir o código do registro a ser REMOVIDO:'))
    cursor.execute("DELETE FROM gruposerviço WHERE _id={}".format(codigo))
    conn.commit()

    desconectar(conn)



def menu():
    print('=====Gerenciador de registros=====')
    print('Selecione uma opção abaixo:')
    print('0- Criar Tabelas')
    print('1- Listar os registros')
    print('2- Inserir os registros')
    print('3- Atualizar registros')
    print('4- Remover registros')
    print('5- Inserir a base de dados primária')
    opcao = int(input('Defina a OPÇÃO:'))
    if opcao in [0, 1, 2, 3, 4,5]:
        if opcao == 0:
            createtable()
        elif opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar() 
        elif opcao == 5:
            inserirdefault()
    else:
        print('Opcao invalida')
