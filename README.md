# projeto-lista-devops

## Comandos para executar o projeto no Docker
- docker build -t lista-tarefas .
- docker run -it lista-tarefas

## Comando para executar os testes
- docker run lista-tarefas python -m unittest discover app/tests
