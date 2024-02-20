# sistema de gerenciamento de funcionários
import pickle


class SistemaGestao:
    def __init__(self):
        self.funcionarios = []
        self.primeiro_id = 1

    # Adicionar um funcionário ----------------------------------------------
    def adicionar_funcionario(self, funcionario):
        funcionario.id = self.primeiro_id
        self.funcionarios.append(funcionario)
        print("Funcionário adicionado com sucesso!")
        print()
        self.primeiro_id += 1

    # Listar todos os funcionários ------------------------------------------
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.to_dict())
            print("=" * 30)
        print()

    # Atualizar um funcionário já criado ------------------------------------
    def atualizar_funcionario(self, id, novo_funcionario):
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                novo_funcionario.id = id
                self.funcionarios[i] = novo_funcionario
                print("Funcionário atualizado com sucesso!")
                print()
                return
        print("Funcionário não encontrado!")
        print()

    # Remover um funcionário ------------------------------------------------
    def remover_funcionario(self, id):
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                del self.funcionarios[i]
                print("Funcionário removido com sucesso!")
                print()
                return
        print("Funcionário não encontrado!")
        print()

    # Salvar os dados em um arquivo -----------------------------------------
    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, "wb") as file:
            pickle.dump(self.funcionarios, file)
        print("Dados salvos com sucesso!")
        print()

    # Carregar os dados de um arquivo ---------------------------------------
    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, "rb") as file:
                self.funcionarios = pickle.load(file)
            print("Dados carregados com sucesso!")
            print()
        except FileNotFoundError:
            self.funcionarios = []
            print("Banco de dados criado com sucesso!")
            print()
