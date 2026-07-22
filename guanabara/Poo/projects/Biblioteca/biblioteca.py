class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def remover(self, livro):
        self.livros.remove(livro)

    def busca(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def listar_todos(self):
        if not self.livros:
            print("Não há livros na biblioteca.")
            return
        for livro in self.livros:
            print(livro)

    def listar_disponíveis(self):
        if not self.livros:
            print("Não há livros na biblioteca.")
            return
        for livro in self.livros:
            if livro.disponivel:
                print(livro)
