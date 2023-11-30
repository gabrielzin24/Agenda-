import os
from time import sleep

#Criando uma classe de tabela Hash 
class TabelaHash:
    #Construtor recebendo tamanho maximo 
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    #Calcular Hash 
    def hash_function(self, nome):
        return sum(ord(char) for char in nome) % self.tamanho
    
    #Adicionar contato com: nome, endereço e telefone 
    def adicionar_contato(self, nome, endereco, telefone):
        indice = self.hash_function(nome)
        if self.tabela[indice] is None:
            self.tabela[indice] = []
        self.tabela[indice].append({'nome': nome, 'endereco': endereco, 'telefone': telefone})

    #Aqui foi utilizado para remoção do contato 
    def remover_contato(self, nome):
        indice = self.hash_function(nome)
        if self.tabela[indice] is not None:
            for contato in self.tabela[indice]:
                if contato['nome'] == nome:
                    self.tabela[indice].remove(contato)

                    return True
        return False
    #Aqui foi utilizado para buscar o nome 
    def buscar_contato(self, nome):
        indice = self.hash_function(nome)
        if self.tabela[indice] is not None:
            for contato in self.tabela[indice]:
                if contato['nome'] == nome:
                    return contato
        return None

#Função que cria um menu, com interface para o usuario gerenciar seus contatos 
def menu():
    os.system("clear")
    tabela = TabelaHash(10)

    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Sair")

        opcao:str = input("Escolha uma opção: ")
        
        if opcao.isdigit() and 1 <= int(opcao) <= 4:
            opcao = int(opcao)

            if opcao == 1:
                nome = input("Digite o nome: ")
                endereco = input("Digite o endereço: ")
                telefone = input("Digite o telefone: ")
                tabela.adicionar_contato(nome, endereco, telefone)

            elif opcao == 2:
                nome = input("Digite o nome do contato a ser removido: ")
                removed = tabela.remover_contato(nome)

                if removed:
                    print("Contato removido!")

                else:
                    print("Contato não encontrado!")

            elif opcao == 3:
                nome = input("Digite o nome do contato a ser buscado: ")
                resultado = tabela.buscar_contato(nome)

                if resultado:
                    print(f"\nNome: {resultado['nome']}\n"
                          f"Endereço: {resultado['endereco']}\n"
                          f"Numero: {resultado['telefone']}"
                        )
                else:
                    print("Contato não encontrado.")

            elif opcao == 4:
                break
        else:
            print("Opção inválida. Tente novamente.")
        
        sleep(5)
        os.system("clear")        

        

menu()