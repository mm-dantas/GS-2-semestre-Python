import json
from datetime import datetime


# Função para carregar dados do arquivo dados.json
def carregarCasas():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'dados.json' não encontrado.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. O arquivo pode estar corrompido.")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return {}


# Função para salvar dados no arquivo dados.json
def salvarCasas(casas):
    try:
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(casas, arquivo, indent=4, ensure_ascii=False)
        print("Dados atualizados com sucesso.")
    except Exception as e:
        print("Erro ao salvar dados:", e)


#Função para visualizar todas as casas cadastradas no sistema
def visualizarTodasCasas():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

    casas_dados = ''
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


# Função para visualizar as casas que estão sem enregia
def visualizarCasasSemEnergia():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

    casas_sem_energia = [casa for casa in casas["casas"] if casa["energia"] == "sem energia"]

    casas_sem_energia_dados = ''
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



# Função para visualizar as casas que estão com enregia
def visualizarCasasComEnergia():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

    casas_com_energia = [casa for casa in casas["casas"] if casa["energia"] == "com energia"]

    casas_com_energia_dados = ''
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


#função para buscar casa pela intalação digitada pelo usuário
def buscarCasaPorInstalacao():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

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


#função para excluir uma casa do sistema (arquivo json)
def excluirCasa():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

    instalacao = input("Digite o número de instalação da casa a ser excluída: ")
    for casa in casas["casas"]:
        if casa["instalacao"] == instalacao:
            casas["casas"].remove(casa)
            print(f"A casa com instalação {instalacao} foi excluída.")
            salvarCasas(casas)
            return
    print("Instalação não encontrada.")


#função para editar qualquer dado de uma casa no arquivo JSON
def editarDadosCasa():
    # Carregar os dados do arquivo JSON
    casas = carregarCasas()

    # Verificar se o arquivo foi carregado corretamente
    if not casas:
        return "Nenhuma casa encontrada."

   # Solicitar ao usuário o número da instalação
    instalacao = input("Digite o número de instalação da casa que deseja editar algum dado: ")
    casa_encontrada = None

    # Procurar a casa pela instalação
    for casa in casas["casas"]:
        if casa["instalacao"] == instalacao:
            casa_encontrada = casa
            break

    if not casa_encontrada:
        print("Instalação não encontrada.")
        return

    # Mostrar os campos que podem ser editados
    print("Campos disponíveis para edição:")
    for i, chave in enumerate(casa_encontrada.keys(), start=1):
        print(f"{i} - {chave}: {casa_encontrada[chave]}")

    try:
        # Solicitar ao usuário o campo a ser editado
        campo_index = int(input("Digite o número do campo que deseja editar: "))
        campo_chave = list(casa_encontrada.keys())[campo_index - 1]
    except (ValueError, IndexError):
        print("Opção inválida. Tente novamente.")
        return

    # Solicitar o novo valor
    novo_valor = input(f"Digite o novo valor para {campo_chave}: ")

    # Atualizar o valor
    casa_encontrada[campo_chave] = novo_valor

    # Salvar os dados atualizados no arquivo JSON
    salvarCasas(casas)
    print(f"O campo '{campo_chave}' foi atualizado com sucesso.")


#função para gerar um arquivo txt que nele mostra as casas que estão com ou sem energia, ou até todas elas
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
    linha = f"Usuário requerente: {requerente}".ljust(largura_linha - len(f" {data_atual}")) + f" {data_atual}"

    # Calcula o número de espaços à esquerda para centralizar o texto
    espacos_necessarios = (largura_linha - len(titulo)) // 2

    # Cria a linha com os espaços à esquerda para centralização
    linha_centralizada = " " * espacos_necessarios + titulo

    arquivo.write(f"{linha}\n")
    arquivo.write("\n"+linha_centralizada+"\n")
    arquivo.write(f"{texto}\n")
    arquivo.close()



