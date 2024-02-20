# Criando a tela inicial do programa
from funcionarios import Funcionario
from sistema_gestao import SistemaGestao


def main():
    sistema = SistemaGestao()
    sistema.carregar_dados("funcionarios_dados.pkl")

    while True:
        print("*****Sistema de Gerenciamento de Funcionários*****")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Atualizar funcionário")
        print("4 - Remover funcionário")
        print("5 - Salvar dados")
        print("6 - Sair")
        print()

        opcao = int(input("Digite a opção desejada (1/2/3/4/5/6): "))
        print()

        if opcao == 1:
            # id = int(input("Digite o ID do funcionário: "))
            nome = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            departamento = input("Digite o departamento do funcionário: ")

            funcionario = Funcionario(nome, salario, departamento)
            sistema.adicionar_funcionario(funcionario)

        elif opcao == 2:
            if len(sistema.funcionarios) == 0:
                print("Não há funcionários cadastrados!")
                print()
            else:
                sistema.listar_funcionarios()

        elif opcao == 3:
            id = int(input("Digite o ID do funcionário que deseja atualizar: "))
            nome = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            departamento = input("Digite o departamento do funcionário: ")

            novo_funcionario = Funcionario(nome, salario, departamento)
            sistema.atualizar_funcionario(id, novo_funcionario)

        elif opcao == 4:
            id = int(input("Digite o ID do funcionário que deseja remover: "))
            sistema.remover_funcionario(id)

        elif opcao == 5:
            sistema.salvar_dados("funcionarios_dados.pkl")

        elif opcao == 6:
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
