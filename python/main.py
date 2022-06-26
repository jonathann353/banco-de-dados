from conexao import *

def menu():
    conn = abrirConexao("127.0.0.1", "root", "look7412", "banco")

    opcao = int(input('''[1]Emprestimo de livro\n[2]Cadastrar usuario\n[3]Consultar empretimos\n[4]Devolução de livro\n[00]Sair\n>: ''')) 

    if opcao == 00:
        print("até mais!!!")

    if opcao == 1:
        emprestimoLivro(conn)
        print("Emprestimo realizado com sucesso!")
        n = input("Deseja continuar [s]sim ou [n]nao: ")
        if n == "s":
            menu()
        else:
            print("ate mais...")

    if opcao == 2:
        inserirUsuario(conn)
        print("Cadastro realizado com sucesso!")
        n = input("Deseja continuar [s]sim ou [n]nao: ")
        if n == "s":
            menu()
        else:
            print("ate mais...")
            
    if opcao == 3:
        consultar(conn)
        print("Os dados solicitados!")
        n = input("Deseja continuar [s]sim ou [n]nao: ")
        if n == "s":
            menu()
        else:
            print("ate mais...")

    if opcao == 4:
        deletarUsuario(conn)
        print("Usuario excluido com sucesso!")
        n = input("Deseja continuar [s]sim ou [n]nao: ")
        if n == "s":
            menu()
        else:
            print("ate mais...")

    fecharConexao(conn)        
#executando o programa
def main():
  
    menu()



if __name__ == "__main__":
    main()