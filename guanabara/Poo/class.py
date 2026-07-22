class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")


pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("Maria", 25)

pessoa1.falar()
pessoa2.falar()