# Cadastro de Empresas TUI

Este é um aplicativo de terminal (TUI) para gerenciar um cadastro simples de empresas, construído com Python e a biblioteca Textual.

## Funcionalidades (MVP)

- Visualizar uma lista de empresas em um painel lateral.
- Ver os detalhes (código, nome e URL) de uma empresa selecionada.
- Alternar a visibilidade da lista de empresas com a tecla `F3`.

## Pré-requisitos

- Docker instalado em sua máquina.

## Como Executar

1.  **Crie os arquivos:**
    Salve os arquivos `app.py`, `app.css`, e `Dockerfile` no mesmo diretório.

2.  **Construa a imagem Docker:**
    Navegue até o diretório do projeto no seu terminal e execute o seguinte comando para construir a imagem:

    ```bash
    docker build -t cadastro-tui .
    ```

3.  **Execute o container Docker:**
    Após a imagem ser construída, execute o aplicativo com o comando:

    ```bash
    docker run -it --rm cadastro-tui
    ```
    - `-it` aloca um pseudo-TTY e mantém o STDIN aberto, o que é necessário para interagir com a aplicação TUI.
    - `--rm` remove o container automaticamente quando a aplicação é fechada.

## Uso

- Use as **teclas de seta** para navegar na lista de empresas quando ela estiver visível.
- Pressione **F3** para mostrar ou esconder a lista de empresas.
- Pressione **Q** para sair do aplicativo.

## Próximos Passos (Evolução)

Este é um MVP. As próximas funcionalidades a serem implementadas são:
- Adicionar, editar e remover empresas, permitindo a livre edição dos campos.
- Persistir os dados em um arquivo ou banco de dados para que não se percam ao sair.