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