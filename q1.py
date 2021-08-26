from datetime import datetime

class Cadastro:
    def __init__(self):
        self.codigo_banco = input("Insira o código do banco: ")
        self.valor_despesa = input("Insira o valor da despesa: ")
        self.descricao_despesa = input("Insira a descrição da despesa: ")
        self.data = str(datetime.date(datetime.now()))
        self.formatarData()

    def getString(self):
        print(f"Banco: {self.codigo_banco}")
        print(f"Valor {self.valor_despesa}")
        print(f"Descrição da despesa: {self.descricao_despesa}")
        print(f"Data do registro: {self.data}")

    def formatarData(self):
        data = self.data
        separados = data.split("-")
        self.data = f"Dia {separados[2]} do mês {separados[1]} do ano {separados[0]}"

cadastro = Cadastro()
cadastro.getString()