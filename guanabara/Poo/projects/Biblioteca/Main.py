from biblioteca import Biblioteca
from livro import Livro


def menu():

    print("       SISTEMA DE BIBLIOTECA")
    print("1 - Adicionar livro")
    print("2 - Remover livro")
    print("3 - Buscar livro")
    print("4 - Listar todos os livros")
    print("5 - Listar livros disponíveis")
    print("6 - Emprestar livro")
    print("7 - Devolver livro")
    print("0 - Sair")


def adicionar_livro(biblioteca: Biblioteca):
    print("\n--- Adicionar livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    try:
        ano = int(input("Ano: "))
        paginas = int(input("Páginas: "))
    except ValueError:
        print("Ano e páginas devem ser números inteiros.")
        return

    livro = Livro(titulo, autor, ano, paginas)
    biblioteca.adicionar(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")


def remover_livro(biblioteca: Biblioteca):
    print("\n--- Remover livro ---")
    titulo = input("Título do livro a remover: ").strip()
    livro = biblioteca.busca(titulo)

    if livro is None:
        print("Livro não encontrado.")
        return

    biblioteca.remover(livro)
    print(f"Livro '{titulo}' removido com sucesso!")


def buscar_livro(biblioteca: Biblioteca):
    print("\n--- Buscar livro ---")
    titulo = input("Título: ").strip()
    livro = biblioteca.busca(titulo)

    if livro is None:
        print("Livro não encontrado.")
        return

    print("\n" + str(livro))


def emprestar_livro(biblioteca: Biblioteca):
    print("\n--- Emprestar livro ---")
    titulo = input("Título do livro: ").strip()
    livro = biblioteca.busca(titulo)

    if livro is None:
        print("Livro não encontrado.")
        return

    print(livro.emprestar())


def devolver_livro(biblioteca: Biblioteca):
    print("\n--- Devolver livro ---")
    titulo = input("Título do livro: ").strip()
    livro = biblioteca.busca(titulo)

    if livro is None:
        print("Livro não encontrado.")
        return

    print(livro.devolver())


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_livro(biblioteca)
        elif opcao == "2":
            remover_livro(biblioteca)
        elif opcao == "3":
            buscar_livro(biblioteca)
        elif opcao == "4":
            print("\n--- Todos os livros ---")
            biblioteca.listar_todos()
        elif opcao == "5":
            print("\n--- Livros disponíveis ---")
            biblioteca.listar_disponíveis()
        elif opcao == "6":
            emprestar_livro(biblioteca)
        elif opcao == "7":
            devolver_livro(biblioteca)
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
