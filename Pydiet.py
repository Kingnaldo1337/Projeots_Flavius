import os  # Importa o módulo 'os' para manipulação de arquivos e diretórios
from reportlab.pdfgen import canvas  # Importa a classe 'canvas' do módulo 'reportlab.pdfgen'


class Paciente:
    def __init__(self, cpf, nome, peso, altura, hora_consulta, data_consulta):
        # Inicializa os atributos do objeto Paciente com os valores fornecidos
        self.cpf = cpf
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.hora_consulta = hora_consulta
        self.data_consulta = data_consulta

    def calcular_imc(self):
        # Calcula o IMC do paciente com base no peso e altura
        altura_in_metros = self.altura / 100
        return self.peso / (altura_in_metros ** 2)


class Pydiet:
    def __init__(self):
        self.pacientes = {}
        self.carregar_pacientes()

    def adicionar_paciente(self, paciente):
        # Adiciona um paciente ao dicionário de pacientes, usando o CPF como chave
        self.pacientes[paciente.cpf] = paciente

    def calcular_imc_paciente(self, cpf):
        # Calcula o IMC de um paciente com base no CPF fornecido
        paciente = self.pacientes.get(cpf)
        if paciente:
            imc = paciente.calcular_imc()
            print(f"O IMC do paciente {paciente.nome} é: {imc:.2f}")
        else:
            print("Paciente não encontrado.")

    def salvar_pacientes(self):
        # Salva os dados dos pacientes em um arquivo de texto
        diretorio = r"C:\Users\tomad\Desktop\pydiet"  # Substitua pelo caminho correto
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        arquivo = os.path.join(diretorio, "pacientes.txt")
        with open(arquivo, "w") as f:
            for cpf, paciente in self.pacientes.items():
                f.write("CPF: " + cpf + "\n")
                f.write("Nome: " + paciente.nome + "\n")
                f.write("Peso: " + str(paciente.peso) + "\n")
                f.write("Altura: " + str(paciente.altura) + "\n")
                f.write("Hora da consulta: " + paciente.hora_consulta + "\n")
                f.write("Data da consulta: " + paciente.data_consulta + "\n")
                f.write("\n")
        print("Dados dos pacientes salvos com sucesso!")

    def carregar_pacientes(self):
        # Carrega os dados dos pacientes a partir de um arquivo de texto
        arquivo = os.path.join(r"C:\Users\tomad\Desktop\pydiet", "pacientes.txt")  # Substitua pelo caminho correto
        if not os.path.exists(arquivo):
            print("Nenhum paciente cadastrado.")
            return
        with open(arquivo, "r") as f:
            cpf = ""
            nome = ""
            peso = 0.0
            altura = 0.0
            hora_consulta = ""
            data_consulta = ""
            for linha in f:
                if linha.startswith("CPF:"):
                    cpf = linha.replace("CPF: ", "").strip()
                elif linha.startswith("Nome:"):
                    nome = linha.replace("Nome: ", "").strip()
                elif linha.startswith("Peso:"):
                    peso = float(linha.replace("Peso: ", "").strip())
                elif linha.startswith("Altura:"):
                    altura = float(linha.replace("Altura: ", "").strip())
                elif linha.startswith("Hora da consulta:"):
                    hora_consulta = linha.replace("Hora da consulta: ", "").strip()
                elif linha.startswith("Data da consulta:"):
                    data_consulta = linha.replace("Data da consulta: ", "").strip()
                elif linha.strip() == "":
                    if cpf != "":
                        paciente = Paciente(cpf, nome, peso, altura, hora_consulta, data_consulta)
                        self.adicionar_paciente(paciente)
                        cpf = ""
                        nome = ""
                        peso = 0.0
                        altura = 0.0
                        hora_consulta = ""
                        data_consulta = ""
        print("Dados dos pacientes carregados com sucesso!")

    def cpf_valido(self, cpf):
        # Verifica se um CPF é válido
        if len(cpf) != 11:
            return False
        if not cpf.isdigit():
            return False
        if cpf in self.pacientes:
            return False
        return True

    def cadastrar_paciente(self):
        # Cadastra um novo paciente
        cpf = input("Digite o CPF do paciente: ")
        nome = input("Digite o nome do paciente: ")
        peso = float(input("Digite o peso do paciente em kg: "))
        altura = float(input("Digite a altura do paciente em centímetros: "))
        hora_consulta =input("Digite a hora da consulta com o nutricionista: ")
        data_consulta = input("Digite a data da consulta com o nutricionista: ")

        paciente = Paciente(cpf, nome, peso, altura, hora_consulta, data_consulta)
        self.adicionar_paciente(paciente)
        print("Paciente cadastrado com sucesso!")

    def editar_paciente(self, cpf):
        # Edita as informações de um paciente com base no CPF fornecido
        paciente = self.pacientes.get(cpf)
        if paciente:
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
        else:
            print("Paciente não foi encontrado.")

    def excluir_paciente(self, cpf):
        # Exclui um paciente com base no CPF fornecido
        paciente = self.pacientes.pop(cpf, None)
        if paciente:
            print("Paciente excluído com sucesso.")
        else:
            print("Paciente não foi encontrado.")

    def listar_pacientes(self):
        # Lista todos os pacientes cadastrados
        for cpf, paciente in self.pacientes.items():
            print("CPF:", cpf)
            print("Nome:", paciente.nome)
            print("Peso:", paciente.peso)
            print("Altura:", paciente.altura)
            print("Hora da consulta:", paciente.hora_consulta)
            print("Data da consulta:", paciente.data_consulta)
            print()

    def criar_plano_dieta(self, paciente):
        # Cria um plano de dieta para o paciente
        return """Plano de Dieta:
    - Café da manhã: 2 ovos, 1 fatia de pão integral, 1 xícara de café preto.
    - Lanche da manhã: 1 maçã.
    - Almoço: 150g de frango grelhado, 1 porção de arroz integral, salada de folhas verdes.
    - Lanche da tarde: 1 iogurte natural, 1 colher de sopa de aveia.
    - Jantar: 200g de peixe assado, 1 porção de legumes cozidos.
    - Ceia: 1 copo de leite desnatado.
    """

    def gerar_plano_dieta_pdf(self, paciente):
        # Gera um plano de dieta em formato PDF para o paciente
        imc = paciente.calcular_imc()
        plano_dieta = self.criar_plano_dieta(paciente)

        nome_arquivo = f"plano_dieta_{paciente.nome.replace(' ', '_')}.pdf"
        diretorio = r"C:\Users\tomad\Desktop\pydiet"  # Substitua pelo caminho correto
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        arquivo = os.path.join(diretorio, nome_arquivo)

        c = canvas.Canvas(arquivo)
        c.setFont("Helvetica", 12)
        c.drawString(50, 800, f"Nome do Paciente: {paciente.nome}")
        c.drawString(50, 780, f"IMC: {imc:.2f}")
        c.drawString(50, 760, "Plano de Dieta:")
        c.setFont("Helvetica", 10)
        text_lines = plano_dieta.splitlines()
        y = 740
        for line in text_lines:
            c.drawString(50, y, line)
            y -= 15
        c.save()
        print(f"Plano de dieta para {paciente.nome} gerado com sucesso: {nome_arquivo}")

    def gerar_plano_dieta_pdf_por_cpf(self, cpf):
        # Gera um plano de dieta em formato PDF para um paciente com base no CPF fornecido
        paciente = self.pacientes.get(cpf)
        if paciente:
            self.gerar_plano_dieta_pdf(paciente)
        else:
            print("Paciente não foi encontrado.")

    def run(self):
        while True:
            self.limpar_tela()
            print("\n====== Pydiet ======")
            print("1. Cadastrar paciente")
            print("2. Calcular IMC de um paciente")
            print("3. Listar pacientes")
            print("4. Editar paciente")
            print("5. Excluir paciente")
            print("6. Gerar plano de dieta em PDF por CPF")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.cadastrar_paciente()
                self.salvar_pacientes()
                input("Pressione ENTER para continuar...")

            elif escolha == "2":
                cpf = input("Digite o CPF do paciente para calcular o IMC: ")
                self.calcular_imc_paciente(cpf)
                input("Pressione ENTER para continuar...")

            elif escolha == "3":
                self.listar_pacientes()
                input("Pressione ENTER para continuar...")

            elif escolha == "4":
                cpf = input("Digite o CPF do paciente para editar: ")
                self.editar_paciente(cpf)
                self.salvar_pacientes()
                input("Pressione ENTER para continuar...")

            elif escolha == "5":
                cpf = input("Digite o CPF do paciente para excluir: ")
                self.excluir_paciente(cpf)
                self.salvar_pacientes()
                input("Pressione ENTER para continuar...")

            elif escolha == "6":
                cpf = input("Digite o CPF do paciente para gerar o plano de dieta em PDF: ")
                self.gerar_plano_dieta_pdf_por_cpf(cpf)
                input("Pressione ENTER para continuar...")

            elif escolha == "0":
                print("Encerrando o Pydiet...")
                break

            else:
                print("Opção inválida. Digite um número válido.")
                input("Pressione ENTER para continuar...")

    @staticmethod
    def limpar_tela():
        # Limpa a tela do console
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


if __name__ == "__main__":
    pydiet = Pydiet()
    pydiet.run()
