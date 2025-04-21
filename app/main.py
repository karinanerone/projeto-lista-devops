#Projeto: lista_tarefas Aluna: Karina Nerone
tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    if tarefa.strip():
        tarefas.append(tarefa)
        print("Tarefa adicionada.")
    else:
        print("Tarefas vazias não são permitidas.")

def remover_tarefa():
    ver_tarefas()
    try:
        index = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= index < len(tarefas):
            tarefa_removida = tarefas.pop(index)
            print(f"Tarefa '{tarefa_removida}' removida.")
        else:
            print("Número da tarefa inválido.")
    except ValueError:
        print("Digite um número válido.")

def ver_tarefas():
    if tarefas:
        print("Suas tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa para exibir.")

def main():
    while True:
        print("\nLista de Tarefas")
        print("-----------------")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            ver_tarefas()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "4":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()