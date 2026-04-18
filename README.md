# 📦 Inventário de Qualidade: Automação Industrial em Python

Este projeto é um sistema de **Inventário de Qualidade** e **Rastreabilidade** desenvolvido para automatizar a triagem e o armazenamento de peças em uma linha de produção industrial. O sistema garante que apenas itens em conformidade técnica sejam estocados e organizados em lotes.

## 🛠️ Funcionalidades Principais

- **Triagem Inteligente:** Validação automática baseada em parâmetros físicos:
  - **Peso:** 95g a 105g.
  - **Comprimento:** 10cm a 20cm.
  - **Cores Permitidas:** Azul e Verde.
- **Entrada Flexível:** O sistema "limpa" os dados, aceitando entradas como `95g`, `95 G`, `10cm` ou apenas o número puro.
- **Rastreabilidade Total:** - **Trava de ID:** Impede duplicidade de IDs para peças aprovadas.
  - **Localização:** Cada peça aprovada recebe automaticamente o número da caixa onde foi armazenada.
- **Anonimização de Reprovações:** Peças reprovadas são registradas como `S/ID (Reprovada)` no histórico, mantendo a auditoria estatística sem bloquear o ID para novas tentativas.
- **Gestão de Lotes (Caixas):** - Agrupamento automático de 10 peças aprovadas por caixa.
  - **Listagem de Conteúdo:** Função específica para visualizar quais IDs de peças compõem cada caixa fechada.
- **Remoção Assistida:** Tela de exclusão com exibição instantânea dos IDs e respectivas caixas das peças aprovadas no sistema.

## 🚀 Como Executar

1. **Pré-requisito:** Ter o Python 3.x instalado.
2. **Preparação:** Abra ou salve o código em um arquivo chamado `main.py`.
3. **Execução:** Abra o terminal na pasta do arquivo e digite:
   python main.py

##  Exemplos de Fluxos
### 1. Sucesso (Aprovação)
* **Input:** ID: `A01` | Peso: `100g` | Comprimento: `15` | Cor: `azul`
* **Resultado:** Peça aprovada e enviada para a caixa.

### 2. Falha (Reprovação com Log)
* **Input:** ID: `A02` | Peso: `80` | Comprimento: `5cm` | Cor: `vermelho`
* **Resultado:** Registro salvo como `S/ID (Reprovada)`. O histórico exibirá:
    > *Peso fora da faixa. Cor inválida. Comprimento fora da faixa (Digitado: 80.0g, vermelho, 5.0cm)*.

### 3. Remoção de Item
Ao selecionar a opção de remover, o sistema lista automaticamente:
* *ID: A01 (100.0g, azul)*
* *ID: A05 (102.0g, verde)*
Isso permite que o operador escolha o ID correto para exclusão com agilidade.

### 4. Histórico com Rastreabilidade (Opção 2)
O sistema exibe uma tabela detalhada:
`ID: A01 | STATUS: Aprovada | CAIXA: 1 | DADOS: 100.0g, azul, 15.0cm`

### 5. Ver Conteúdo das Caixas (Opção 4)
Permite visualizar o inventário por lote:
`CAIXA #1: A01, A02, A03, A04, A05, A06, A07, A08, A09, A10`


## Estrutura de Dados
O software utiliza **Dicionários** para objetos de peça e **Listas Aninhadas** para o controle de caixas fechadas, permitindo uma gestão de inventário robusta e escalável.

---
*Projeto desenvolvido para o Desafio de Automação Digital.*