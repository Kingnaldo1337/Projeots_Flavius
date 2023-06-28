import os


class Paciente:
    def __init__(self, nome, peso, altura, hora_consulta, data_consulta):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.hora_consulta = hora_consulta
        self.data_consulta = data_consulta

    def calcular_imc(self):
        altura_in_metros = self.altura / 100
        return self.peso / (altura_in_metros ** 2)


class PyeDiet:
    def __init__(self):
        self.pacientes = []
        self.carregar_pacientes()

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def salvar_pacientes(self):
        diretorio = r"C:\Users\tomad\Desktop\pydiet"
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        arquivo = os.path.join(diretorio, "pacientes.txt")
        with open(arquivo, "w") as f:
            for paciente in self.pacientes:
                f.write(
                    f"{paciente.nome},{paciente.peso},{paciente.altura},{paciente.hora_consulta},{paciente.data_consulta}\n"
                )
        print("Dados dos pacientes salvos com sucesso!")

    def carregar_pacientes(self):
        arquivo = os.path.join(r"C:\Users\tomad\Desktop\pydiet", "pacientes.txt")
        if not os.path.exists(arquivo):
            print("Nenhum paciente cadastrado.")
            return
        with open(arquivo, "r") as f:
            for linha in f:
                dados = linha.strip().split(",")
                nome = dados[0]
                peso = float(dados[1])
                altura = float(dados[2])
                hora_consulta = dados[3]
                data_consulta = dados[4]
                paciente = Paciente(nome, peso, altura, hora_consulta, data_consulta)
                self.adicionar_paciente(paciente)
        print("Dados dos pacientes carregados com sucesso!")

    def editar_paciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                print("Paciente encontrado. Agora edite as informações:")
                peso = float(input("Digite o novo peso do paciente em kg: "))
                altura = float(input("Digite a nova altura do paciente em centímetros: "))
                hora_consulta = input("Digite a nova hora da consulta com o nutricionista: ")
                data_consulta = input("Digite a nova data da consulta com o nutricionista: ")
                paciente.peso = peso
                paciente.altura = altura
                paciente.hora_consulta = hora_consulta
                paciente.data_consulta = data_consulta
                print("Paciente foi atualizado.")
                return
        print("Paciente não foi encontrado.")

    def excluir_paciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                self.pacientes.remove(paciente)
                print("Paciente excluído com sucesso!.")
                return
        print("Paciente não foi encontrado na lista de dados.")

    def criar_plano_dieta(self, paciente):
        imc = paciente.calcular_imc()
        if imc < 18.5:
            return "Plano de dieta para aumentar de peso, coma mais carboidratos, muito carboidrato!"
        elif imc > 26.5:
            return "Plano de dieta para diminuir peso, precisa fazer muitos exercícios físicos e comer menos."
        else:
            return "O IMC do paciente está dentro da faixa saudável. Continue mantendo essa constância para ter uma vida saudável."

    def listar_pacientes(self):
        print("\nLista de Pacientes Cadastrados:")
        if not self.pacientes:
            print("Nenhum paciente foi cadastrado até o momento.")
        else:
            for paciente in self.pacientes:
                print(f"Nome: {paciente.nome}")
                print(f"Data da consulta: {paciente.data_consulta}")
                print(f"Hora da consulta: {paciente.hora_consulta}")

    def run(self):
        while True:
            print("\n====== PyeDiet ======")
            print("1. Cadastrar paciente")
            print("2. Calcular IMC de um paciente")
            print("3. Listar pacientes")
            print("4. Editar paciente")
            print("5. Excluir paciente")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Digite o nome do paciente: ")
                peso = float(input("Digite o peso do paciente em kg: "))
                altura = float(input("Digite a altura do paciente em cm: "))
                hora_consulta = input("Digite a hora da consulta com o nutricionista: ")
                data_consulta = input("Digite a data da consulta com o nutricionista: ")
                paciente = Paciente(nome, peso, altura, hora_consulta, data_consulta)
                self.adicionar_paciente(paciente)
                print("Paciente cadastrado com sucesso!")

            elif escolha == "2":
                nome = input("Digite o nome do paciente: ")
                paciente_encontrado = None
                for paciente in self.pacientes:
                    if paciente.nome == nome:
                        paciente_encontrado = paciente
                        break

                if paciente_encontrado:
                    imc = paciente_encontrado.calcular_imc()
                    print(f"O IMC de {paciente_encontrado.nome} é {imc:.2f}")
                    plano_dieta = self.criar_plano_dieta(paciente_encontrado)
                    print(plano_dieta)
                else:
                    print("Paciente não foi encontrado.")

            elif escolha == "3":
                self.listar_pacientes()

            elif escolha == "4":
                nome = input("Digite o nome do paciente que deseja editar: ")
                self.editar_paciente(nome)

            elif escolha == "5":
                nome = input("Digite o nome do paciente que deseja excluir: ")
                self.excluir_paciente(nome)

            elif escolha == "0":
                self.salvar_pacientes()
                print("Saindo...")
                break

            else:
                print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    pye_diet = PyeDiet()
    pye_diet.run()
