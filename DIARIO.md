Data: 15/10/2026
O que foi feito: Criação dos arquivos, Base, engine e funções "criar_banco" e "nova_sessao"
Dificuldade encontrada: Nenhuma dificuldade encontrada, pois foram implementações básicas que já haviam sido feitas recentemente em atividades práticas
Como resolvi: Nenhuma dificuldade encontrada
Próximo passo: Criar os modelos Autor, Livro e Leitor

Data: 15/10/2026
O que foi feito: Implementação dos modelos Autor, Livro e Leitor
Dificuldade encontrada: Implementação do relacionamento N:N
Como resolvi: Busquei na documentação oficial do SQLALchemy como deveria ser implementado o relacionamento. A partir disso, criei uma tabela associativa para ser possível ligar Leitores e Livros pelo ID de cada objeto.
Próximo passo: Criar os Blueprints

Data: 16/10/2026
O que foi feito: Implementação dos blueprints autores_bp, livros_bp e leitores_bp, e das rotas que serão utilizadas (sem conteúdo)
Dificuldade encontrada: Definição das páginas/rotas que seriam utilizadas
Como resolvi: Analisei os requisitos do projeto para definir quais páginas e blueprints seriam necessários para o projeto e defini as rotas que acredito que serão necessárias
Próximo passo: Implementar as primeiras rotas

Data: 20/10/2026
O que foi feito: Implementação das rotas do CRUD do módulo de Livros (listar, cadastrar, editar e remover), criação do modelo Usuario em models.py e implementação das rotas de login e logout no controller auth.
Dificuldade encontrada: Organização do envio de dados via formulários, gerenciamento da sessão do usuário autenticado e alterações no banco.
Como resolvi: Resgatei os campos com request.form.get(), utilizei flask_session para manter o usuário logado e apliquei session.commit() para salvar os dados no SQLAlchemy.
Próximo passo: Implementação das rotas de cadastro de usuário e do módulo de Autores.

Data: 21/10/2026
O que foi feito: Implementação das rotas do CRUD do módulo de Autores (listar autores e livros dos autores) e a criação do cadastro de Usuario no controller auth.
Dificuldade encontrada: Confusão entre a session do flask e a session do SQLAlchemy e em relação ao nome do parâmetro na rota de livros do autor.
Como resolvi: Separando as sessões nas importações (database import para banco de dados e flask import para o usuário), e ajuste no parâmetro da rota.
Próximo passo:  -

Data: 24/10/2026
O que foi feito: Adição do HTML e CSS das páginas de início, cadastro, login e cadastro de livros.
Dificuldade encontrada: Dificuldade para acessar o css específico de cada blueprint.
Como resolvi: Adicionei o static_folder nos arquivos init.py dos blueprints e acessei eles por meio do blueprint.
Próximo passo: Fazer o HTML e o CSS das páginas de listagem de livros, autores e livros do autor.
