tarefas = ["Revisar código", "Testar login", "Escrever documentação"]

print("Gerenciador de tarefas")

while True:
    print("\nMenu: ")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

    elif opcao =="2":
        nova = input("Nova tarefa: ")
        tarefas.append(nova)
        print(f" '{nova}' adicionada!")

    elif opcao == "3":
        if not tarefas: #se a lista tarefas esta vazia
            print("Nenhuma tarefa para remover!")
            continue #interrompe apenas a execução atual do laço

        num = input("Numero da tarefa a remover: ")
        if num.isdigit() and 0 < int(num) <= len(tarefas):
            removida = tarefas.pop(int(num)-1)
            print(f"'{removida}' removida!")
        else:
            print("Numero invalido!")
    
    elif opcao == "4":
        print("Até logo!")
        break

    else: print("Opção invalida!")