from datetime import datetime

casas = {
  "casas": [
    {
      "instalacao": "123456789",
      "titular": "João da Silva",
      "cpf": "111.222.333-44",
      "cep": "07010-000",
      "endereco": "Rua A, 123",
      "bairro": "Centro",
      "cidade": "Guarulhos",
      "estado": "SP",
      "energia": "com energia",
      "data_ultima_medicao": "2024-11-10",
      "tensao_ultima_medicao": 220,
      "status_energia": "estável"
    },
    {
      "instalacao": "987654321",
      "titular": "Maria Oliveira",
      "cpf": "555.666.777-88",
      "cep": "07020-111",
      "endereco": "Av. B, 456",
      "bairro": "Jardim São Paulo",
      "cidade": "Guarulhos",
      "estado": "SP",
      "energia": "sem energia",
      "data_ultima_medicao": "2024-11-05",
      "tensao_ultima_medicao": 0,
      "status_energia": "sem fornecimento"
    },
    {
      "instalacao": "135791357",
      "titular": "Carlos Souza",
      "cpf": "999.888.777-66",
      "cep": "07030-222",
      "endereco": "Rua C, 789",
      "bairro": "Vila Augusta",
      "cidade": "Guarulhos",
      "estado": "SP",
      "energia": "com energia",
      "data_ultima_medicao": "2024-11-12",
      "tensao_ultima_medicao": 127,
      "status_energia": "oscilando"
    },
    {
      "instalacao": "246824682",
      "titular": "Ana Costa",
      "cpf": "222.333.444-55",
      "cep": "07040-333",
      "endereco": "Av. D, 321",
      "bairro": "Gopoúva",
      "cidade": "Guarulhos",
      "estado": "SP",
      "energia": "sem energia",
      "data_ultima_medicao": "2024-11-08",
      "tensao_ultima_medicao": 0,
      "status_energia": "frequentes quedas"
    },
    {
      "instalacao": "112233445",
      "titular": "Pedro Fernandes",
      "cpf": "123.456.789-00",
      "cep": "07050-444",
      "endereco": "Rua E, 654",
      "bairro": "Jardim Tranquilidade",
      "cidade": "Guarulhos",
      "estado": "SP",
      "energia": "com energia",
      "data_ultima_medicao": "2024-11-14",
      "tensao_ultima_medicao": 220,
      "status_energia": "estável"
    }
  ]
}



def visualizarTodasCasas():
    casas_dados = ''
    print('\nAqui estão todas as casas que estão com e sem energia:')
    tituloCasasComESemEnergia = "Casas Que Estão Com e Sem Energia Elétrica Na Cidade de Guarulhos No Momento"
    for casa in casas["casas"]:
        casas_dados += (
            f"\nInstalação: {casa['instalacao']}\n"
            f"Titular: {casa['titular']}\n"
            f"CPF: {casa['cpf']}\n"
            f"CEP: {casa['cep']}\n"
            f"Endereço: {casa['endereco']}\n"
            f"Bairro: {casa['bairro']}\n"
            f"Cidade: {casa['cidade']}\n"
            f"Estado: {casa['estado']}\n"
            f"Residência: {casa['energia']}\n"
            f"Data da Última Medição: {casa['data_ultima_medicao']}\n"
            f"Tensão na Última Medição: {casa['tensao_ultima_medicao']}V\n"
            f"Status da Energia: {casa['status_energia']}\n"
            + "-" * 40
        )
    return tituloCasasComESemEnergia, casas_dados



def visualizarCasasSemEnergia():
    casas_sem_energia = [casa for casa in casas["casas"] if casa["energia"] == "sem energia"]

    casas_sem_energia_dados = ''
    print('Aqui estão todas as casas que estão sem energia:')
    tituloCasasSemEnergia = "Casas Que Estão Sem Energia Elétrica Na Cidade de Guarulhos No Momento"
    for casa in casas_sem_energia:
        casas_sem_energia_dados += (
            f"\nInstalação: {casa['instalacao']}\n"
            f"Titular: {casa['titular']}\n"
            f"CPF: {casa['cpf']}\n"
            f"CEP: {casa['cep']}\n"
            f"Endereço: {casa['endereco']}\n"
            f"Bairro: {casa['bairro']}\n"
            f"Cidade: {casa['cidade']}\n"
            f"Estado: {casa['estado']}\n"
            f"Residência: {casa['energia']}\n"
            f"Data da Última Medição: {casa['data_ultima_medicao']}\n"
            f"Tensão na Última Medição: {casa['tensao_ultima_medicao']}V\n"
            f"Status da Energia: {casa['status_energia']}\n"
            + "-" * 40)
    return tituloCasasSemEnergia, casas_sem_energia_dados




def visualizarCasasComEnergia():
    casas_com_energia = [casa for casa in casas["casas"] if casa["energia"] == "com energia"]

    casas_com_energia_dados = ''
    print('Aqui estão todas as casas que estão com energia:')
    tituloCasasComEnergia = "Casas Que Estão Com Energia Elétrica Na Cidade de Guarulhos No Momento"
    for casa in casas_com_energia:
        casas_com_energia_dados += (
                f"\nInstalação: {casa['instalacao']}\n"
                f"Titular: {casa['titular']}\n"
                f"CPF: {casa['cpf']}\n"
                f"CEP: {casa['cep']}\n"
                f"Endereço: {casa['endereco']}\n"
                f"Bairro: {casa['bairro']}\n"
                f"Cidade: {casa['cidade']}\n"
                f"Estado: {casa['estado']}\n"
                f"Residência: {casa['energia']}\n"
                f"Data da Última Medição: {casa['data_ultima_medicao']}\n"
                f"Tensão na Última Medição: {casa['tensao_ultima_medicao']}V\n"
                f"Status da Energia: {casa['status_energia']}\n"
                + "-" * 40)
    return tituloCasasComEnergia, casas_com_energia_dados


def buscarCasaPorInstalacao():
    instalacao = input("Digite o número de instalação da casa a ser buscada: ")
    for casa in casas["casas"]:
        if casa["instalacao"] == instalacao:
            print(f"\nInstalação: {casa['instalacao']}\n"
                  f"Titular: {casa['titular']}\n"
                  f"CPF: {casa['cpf']}\n"
                  f"CEP: {casa['cep']}\n"
                  f"Endereço: {casa['endereco']}\n"
                  f"Bairro: {casa['bairro']}\n"
                  f"Cidade: {casa['cidade']}\n"
                  f"Estado: {casa['estado']}\n"
                  f"Status de Energia: {casa['energia']}\n"
                  f"Data da Última Medição: {casa['data_ultima_medicao']}\n"
                  f"Tensão na Última Medição: {casa['tensao_ultima_medicao']}V\n"
                  f"Status da Energia: {casa['status_energia']}\n"
                  + "-" * 40)
            return
    print("Instalação não encontrada.")


def excluirCasa():
    instalacao = input("Digite o número de instalação da casa a ser excluída: ")
    for casa in casas["casas"]:
        if casa["instalacao"] == instalacao:
            casas["casas"].remove(casa)
            print(f"A casa com instalação {instalacao} foi excluída.")
            return
    print("Instalação não encontrada.")


def gerarRelatorio(requerente):
    print("Você deseja gerar um relatório sobre:")
    opcaoRelatorio = int(input("1 - as casas sem energia;\n"
                               "2 - as casas com energia;\n"
                               "3 - as casas com e sem energia.\n"
                               "Selecione a opção desejada: "))

    if opcaoRelatorio == 1:
        titulo, texto = visualizarCasasSemEnergia()
    elif opcaoRelatorio == 2:
        titulo, texto = visualizarCasasComEnergia()
    elif opcaoRelatorio == 3:
        titulo, texto = visualizarTodasCasas()


    data_atual = "Data: " + datetime.now().strftime("%d/%m/%Y")

    # Abre o arquivo para escrita (irá sobrescrever o arquivo, se ele já existir)
    arquivo = open('relatorio.txt', 'w', encoding='utf-8')
    largura_linha = 80  # Define a largura da linha. Ajuste conforme necessário

    # Formata a linha com a nome à esquerda e o data à direita
    linha = f"{requerente}".ljust(largura_linha - len(f" {data_atual}")) + f" {data_atual}"

    # Calcula o número de espaços à esquerda para centralizar o texto
    espacos_necessarios = (largura_linha - len(titulo)) // 2

    # Cria a linha com os espaços à esquerda para centralização
    linha_centralizada = " " * espacos_necessarios + titulo

    arquivo.write(f"{linha}\n")
    arquivo.write("\n"+linha_centralizada+"\n")
    arquivo.write(f"{texto}\n")



