import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

class TestRemoverTarefa(unittest.TestCase):
    
    def setUp(self):
        main.tarefas.clear()
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='1')
    def test_remover_tarefa_com_sucesso(self, mock_input, mock_stdout):
        # Preparar uma tarefa para remoção
        main.tarefas.append("Comprar leite")
        main.tarefas.append("Pagar contas")
        
        # Executar função de remoção
        main.remover_tarefa()
        
        # Verificar se a tarefa foi removida
        self.assertEqual(len(main.tarefas), 1)
        self.assertEqual(main.tarefas[0], "Pagar contas")
        self.assertIn("Tarefa 'Comprar leite' removida.", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='3')
    def test_remover_tarefa_indice_invalido(self, mock_input, mock_stdout):
        # Preparar lista com apenas uma tarefa
        main.tarefas.append("Comprar leite")
        
        # Tentativa de remover com índice inválido
        main.remover_tarefa()
        
        # Verificar que a lista permanece inalterada e mensagem correta é exibida
        self.assertEqual(len(main.tarefas), 1)
        self.assertIn("Número da tarefa inválido.", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='abc')
    def test_remover_tarefa_entrada_nao_numerica(self, mock_input, mock_stdout):
        # Preparar lista com uma tarefa
        main.tarefas.append("Comprar leite")
        
        # Tentativa de remover com entrada não numérica
        main.remover_tarefa()
        
        # Verificar que a lista permanece inalterada e mensagem correta é exibida
        self.assertEqual(len(main.tarefas), 1)
        self.assertIn("Digite um número válido.", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='1')
    def test_remover_tarefa_lista_vazia(self, mock_input, mock_stdout):
        # Garantir que a lista está vazia
        main.tarefas.clear()
        
        # Tentativa de remover de lista vazia
        main.remover_tarefa()
        
        # Verificar que a mensagem correta é exibida
        self.assertIn("Nenhuma tarefa para exibir", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()