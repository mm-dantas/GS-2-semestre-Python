# Monitoramento Residencial de Energia

## Autores
- **Matheus Dantas Carvalho** - RM: 558804  
- **Marco Antonio Gonçalves** - RM: 556818  
- **Silas Alves Santos** - RM: 555020  

---

## Problema a Ser Resolvido
A transição para um futuro sustentável no Brasil enfrenta o desafio das perdas no sistema elétrico, que chegam a **8% da energia gerada** — equivalente ao consumo anual de 18 milhões de residências.  
Essas perdas, causadas por falhas técnicas e furtos, impactam a economia, aumentam as emissões de carbono e desperdiçam recursos naturais.  

---

## Descrição do Projeto
Este projeto consiste em um software de **monitoramento de energia elétrica para residências**.  
O sistema, desenvolvido em **Python**, permite que funcionários da companhia de energia realizem as seguintes operações:  

- **Visualizar todas as casas cadastradas.**  
- **Identificar casas com e sem energia**, verificando a consistência da energia.  
- **Monitorar a tensão elétrica** chegando nas residências.  
- **Buscar casas pelo número de instalação.**  
- **Gerar relatórios em formato `.txt`.**  
- **Editar ou excluir registros de residências.**  

Esse software contribui para uma **melhor gestão e manutenção da rede elétrica**, tornando o serviço mais eficiente, reduzindo desperdícios e agilizando a resolução de problemas.  

---

## Instruções de Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/mm-dantas/GS-2-semestre-Python.git
2.	Certifique-se de que o arquivo “dados.json” está na mesma pasta do projeto. Este arquivo deve conter os dados iniciais das residências em formato JSON.
3.	Execute o script principal: main.py
4.	Faça login utilizando as credenciais de algum contribuinte, exemplo:
    -	Usuário: MatheusDantas
    -	Senha: matheus123
5.	Siga as opções do menu para navegar entre as funcionalidades.

## Exemplos de Uso
**Visualizar Casas com Energia**
1.	Escolha a opção 3 no menu principal.
2.	O sistema exibirá os detalhes de todas as residências com energia elétrica.

**Gerar Relatório**
1.	Escolha a opção 7.
2.	Selecione o tipo de relatório desejado:
    - Casas com energia,
    - Casas sem energia,
    - Todas as casas.
3.	O relatório será salvo.

## Requisitos
- Python 3.8+
- Biblioteca padrão (json, datetime)

## Dependências
O projeto não possui dependências externas. Todas as funcionalidades utilizam módulos integrados do Python.

## Estrutura do Projeto
- main.py: Arquivo principal para execução do programa.
- monitoramento.py: Contém funções específicas para manipulação de dados e operações do sistema.
- dados.json: Banco de dados em JSON com os registros das casas. (caso o projeto seja utilizado profissionalmente, o JSON será armazenado remotamente e acessado via requisições HTTP).
