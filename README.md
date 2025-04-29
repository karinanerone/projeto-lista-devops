# projeto-lista-devops

## Comandos para executar o projeto no Docker
- docker build -t lista-tarefas .
- docker run -it lista-tarefas

## Comando para executar os testes e gerar o relatório de cobertura
- docker run lista-tarefas pytest app/tests --cov=app --cov-report=html
