# Definir a classe Funcionarios
class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "salario": self.salario,
            "departamento": self.departamento,
        }
