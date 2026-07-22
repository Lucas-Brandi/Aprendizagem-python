class Livro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        ano: int,
        paginas: int,
    ):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return " livro emprestado"
        else:
            return "Este Livro já foi emprestado"

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return " livro devolvido"
        else:
            return "O livro já se encontra na biblioteca"

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Ano: {self.ano}\n"
            f"Páginas: {self.paginas}\n"
            f"Status: {status}"
        )
