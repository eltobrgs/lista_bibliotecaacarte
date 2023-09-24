class Livro:
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn

class Biblioteca:
    def __init__(self):
        self.inventario = []

    def adicionar_livro(self, livro):
        self.inventario.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao inventário.')

    def consultar_livro(self, titulo):
        for livro in self.inventario:
            if livro.titulo == titulo:
                print(f'Informações sobre o livro "{livro.titulo}":')
                print(f'Autor: {livro.autor}')
                print(f'Ano de Publicação: {livro.ano_publicacao}')
                print(f'ISBN: {livro.isbn}')
                return
        print(f'O livro "{titulo}" não foi encontrado no inventário.')

    def remover_livro(self, titulo):
        for livro in self.inventario:
            if livro.titulo == titulo:
                self.inventario.remove(livro)
                print(f'O livro "{titulo}" foi removido do inventário.')
                return
        print(f'O livro "{titulo}" não foi encontrado no inventário.')

# Função principal
if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")
            isbn = input("Digite o ISBN do livro: ")
            livro = Livro(titulo, autor, ano_publicacao, isbn)
            biblioteca.adicionar_livro(livro)

        elif opcao == "2":
            titulo = input("Digite o título do livro que deseja consultar: ")
            biblioteca.consultar_livro(titulo)

        elif opcao == "3":
            titulo = input("Digite o título do livro que deseja remover: ")
            biblioteca.remover_livro(titulo)

        elif opcao == "4":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
