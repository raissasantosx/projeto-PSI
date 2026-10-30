# Sistema de Gerenciamento de Biblioteca Web

## Tema Escolhido
Sistema para gestão de acervo bibliográfico, controle de autores e empréstimos/leituras efetuadas por leitores.

## Integrantes do Grupo
- **[BRENDA WALSH DE MEDEIROS PEREIRA]**: Responsável pelas rotas do módulo de Autores, rotas de cadastro de usuário e Readme do projeto.
- **[EMILLY MIRELY MARIZ DE ANDRADE]**: Responsável pelas rotas do módulo de Livros, criação do modelo Usuario em models.py, implementação das rotas de login e logout, e Readme do projeto.
- **[LUCAS GABRIEL DE ARAÚJO DIAS]**: Responsável pelos Blueprints e pelo HTML e CSS das páginas de Início, Cadastro, Login e Cadastro de livro, além da função de emprestar livro.
- **[RAÍSSA DOS SANTOS MEDEIROS]**: Responsável pela implementação dos módulos Autor, Livro e Leitor, juntamente com os relacionamentos, além da criação da engine e da função criar_banco.

## Descrição do Sistema
O Sistema possui módulos de Autor, Livro, Leitor e Autenticação. Permite o cadastro e gerenciamento completo de autores, a vinculação de livros aos seus respectivos autores, o controle de leitores cadastrados e o registro de empréstimos entre leitores e livros através de uma tabela associativa. Conta também com controle de acesso através de autenticação de usuários (login, cadastro e logout). 

## Entidades do Sistema
1. **Autor**: Representa o autor responsável pelas obras.
2. **Livro**: Representa a obra cadastrada na biblioteca.
3. **Leitor**: Representa os leitores que possuem vínculo de leitura com os livros.
4. **Usuario**: Representa os acessos ao sistema para autenticação.

## Relacionamentos
- **1:N (Um para Muitos)**: Um Autor pode possuir vários Livros cadastrados, enquanto cada Livro pertence a um único Autor.
- **N:N (Muitos para Muitos)**: Um Leitor pode pegar emprestado/ler vários Livros, e um Livro pode ser lido por vários Leitores.

## Instruções para Executar o Sistema
1. Criar e ativar o ambiente virtual:
   ```bash
   python -m venv env
   # No Windows:
   env\Scripts\activate

## Principais dificuldades encontradas
Na verificação do autor para impedir que ele fizesse o cadastro novamente; 
Na logica da tabela associativa; 
No erro de pegar o id do leitor e do livro;

## Declaração de autoria
Declaro que desenvolvi este projeto compreendendo o código entregue e que sou
capaz de explicar e modificar suas partes principais.
Uso de IA:
[ ] Não utilizei IA generativa.
[X] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
Descrição do uso, se houver:
Foi utilizado como auxilio para tirar dúvidas, como por exemplo: 
Na verificação do autor para impedir que ele fizesse o cadastro novamente; 
Na logica da tabela associativa; 
No erro de pegar o id do leitor e do livro; 
