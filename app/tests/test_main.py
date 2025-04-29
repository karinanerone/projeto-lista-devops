import pytest
from unittest.mock import patch
import io
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

@pytest.fixture
def setup_tarefas():
    main.tarefas.clear()
    return main.tarefas

def test_remover_tarefa_com_sucesso(setup_tarefas, monkeypatch, capsys):
    setup_tarefas.extend(["Comprar leite", "Pagar contas"])
    monkeypatch.setattr('builtins.input', lambda _: '1')
    main.remover_tarefa()
    captured = capsys.readouterr()
    assert len(setup_tarefas) == 1
    assert setup_tarefas[0] == "Pagar contas"
    assert "Tarefa 'Comprar leite' removida." in captured.out

def test_remover_tarefa_indice_invalido(setup_tarefas, monkeypatch, capsys):
    setup_tarefas.append("Comprar leite")
    monkeypatch.setattr('builtins.input', lambda _: '3')
    main.remover_tarefa()
    captured = capsys.readouterr()
    assert len(setup_tarefas) == 1
    assert "Número da tarefa inválido." in captured.out

def test_remover_tarefa_entrada_nao_numerica(setup_tarefas, monkeypatch, capsys):
    setup_tarefas.append("Comprar leite")
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    main.remover_tarefa()
    captured = capsys.readouterr()
    assert len(setup_tarefas) == 1
    assert "Digite um número válido." in captured.out

def test_remover_tarefa_lista_vazia(setup_tarefas, monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    main.remover_tarefa()
    captured = capsys.readouterr()
    assert "Nenhuma tarefa para exibir" in captured.out

def test_adicionar_tarefa(setup_tarefas, monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'Estudar Python')
    main.adicionar_tarefa()
    captured = capsys.readouterr()
    assert len(setup_tarefas) == 1
    assert setup_tarefas[0] == "Estudar Python"
    assert "Tarefa adicionada." in captured.out