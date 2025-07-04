# Sistema de Gerenciamento de Eventos - Comunidade Tech

## Descrição

Este é um sistema simples de gerenciamento de eventos desenvolvido em Python para o trabalho final da disciplina de Algoritmos. O sistema permite o cadastro de eventos e participantes, a associação de participantes a eventos, consulta e alteração de dados, exclusão, além da geração de estatísticas básicas sobre os eventos e participantes.

## Funcionalidades

- Cadastro de eventos com nome, data e tema.
- Cadastro de participantes com nome, CPF, email e preferência temática.
- Consulta e alteração dos dados dos participantes.
- Associação de participantes aos eventos.
- Consulta de eventos e visualização de seus detalhes.
- Exclusão de eventos e participantes.
- Geração de estatísticas, como participantes mais ativos, temas mais frequentes, eventos com poucos participantes e taxa média de participação por tema.
- Validações importantes, como CPF único e válido, nome de evento único, data de evento futura e escolha de preferência temática com base nos temas dos eventos cadastrados.

## Estrutura do Projeto

- `main.py`: Arquivo principal que controla o fluxo do sistema.
- `menu.py`: Funções para exibição dos menus e leitura das opções.
- `eventos.py`: Funções relacionadas ao cadastro, consulta e manipulação de eventos.
- `participantes.py`: Funções relacionadas ao cadastro, consulta e alteração de participantes.
- `estatisticas.py`: Função para geração das estatísticas do sistema.
- `util.py`: Funções utilitárias, como limpeza da tela, validação de CPF e leitura de opções.

## Como usar

1. Execute o arquivo `main.py`.
2. Navegue pelos menus para cadastrar eventos e participantes.
3. Associe participantes aos eventos pelo menu de eventos.
4. Consulte dados, altere ou exclua conforme necessidade.
5. Gere estatísticas para visualizar informações consolidadas.

## Requisitos

- Python 3.x
- Sistema operacional com terminal (Windows, Linux, macOS)

## Observações

- O CPF é o identificador único para participantes.
- Datas de eventos devem estar no futuro.
- Preferência temática dos participantes é escolhida entre os temas já cadastrados em eventos.
- O sistema é baseado em terminal, com interação simples via menus numéricos.

---

Este projeto foi desenvolvido para fins educacionais e prática em programação estruturada, manipulação de listas e dicionários, validação de entradas, modularização e desenvolvimento de sistemas simples em Python.

---

**Autor:** Leonardo Franco de Almeida

