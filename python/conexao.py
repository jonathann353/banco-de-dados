import mysql.connector

#abre a conexao com o banco
def abrirConexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

#fecha a conexao com o banco
def fecharConexao(conn):
    return conn.close()

#inserir usuario no banco de dados
def inserirUsuario(conn):
    cursor = conn.cursor()
    n = input("digite seu nome: ")
    r = input("digite seu rfid: ")
    sql = "insert into usuario(nome, rfid) values ('"+str(n)+"', '"+str(r)+"')"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
        
#deletar informações do banco de dados 
def deletarUsuario(conn):
    cursor = conn.cursor()
    n = input("digite o nome do usuario que deseja deletar: ")
    sql = "delete from usuario where nome='"+str(n)+"'"
    cursor.execute(sql)
    cursor.close()
    conn.commit()

#realiza emprestimo de livro
def emprestimoLivro(conn):
    cursor = conn.cursor()
    livro_emp = input("digite o nome ou o código do livro que deseja pegar emprestado: ")
    aluno_emp = input("digite sua matricula: ")
    sql = "insert into emprestimo_livro(livro_emp, aluno_emp) values ('"+str(livro_emp)+"', '"+str(aluno_emp)+"')"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
#consulta no banco     
def consultar(conn):
    cursor = conn.cursor()
    
    sql = "select usuario.nome, livros.Cód_Título from emplivro inner join usuario on emplivro.fk_id_usuario = usuario.id_usuario inner join livros on emplivro.fk_id_livro = livros.id_livro"
        
    cursor.execute(sql)
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

