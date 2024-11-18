from monitoramento import *

contribuidores = {
    "MatheusDantas": "matheus123",
    "LucasRafael": "lucas123",
    "JulioSouza": "julio123",
    "NeymarJr": "neymar123"
}



def entrar():
    nomeUsuario = input("Para começar digite seu nome de usuário:")
    senha = input("Digite sua senha: ")
    if nomeUsuario in contribuidores and senha == contribuidores[nomeUsuario]:
        print("Acesso consedido")
        return True, nomeUsuario
    else:
        print("Senha ou nome de usário incorretos. Acesso negado!")
        return False, None

def menu():
    acesso, nomeUsuario = entrar()

    if acesso != True:
        return None
    while True:
        print("Veja as opções existentes: \n"
              "1 - Visualizar todas as casas; \n"
              "2 - Visualizar casas sem energia; \n"
              "3 - Visualizar casas com energia; \n"
              "4 - Buscar casa por instalação; \n"
              "5 - Excluir casa; \n"
              "6 - Gerar relatório; \n"
              "7 - Sair"
              )
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Digite um doas números que há no menu.")
            continue

        if opcao == 1:
            titulo, dados = visualizarTodasCasas()
            print(titulo)
            print(dados)
        elif opcao == 2:
            titulo, dados = visualizarCasasSemEnergia()
            print(titulo)
            print(dados)
        elif opcao == 3:
            titulo, dados = visualizarCasasComEnergia()
            print(titulo)
            print(dados)
        elif opcao == 4:
            excluirCasa()
        elif opcao == 5:
            buscarCasaPorInstalacao()
        elif opcao == 6:
            gerarRelatorio(nomeUsuario)
        elif opcao == 7:
            print("Saindo...")
            return None
        else:
            print("Opção inválida!")


menu()


