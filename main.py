list_todos = []

while True:
    user_action = input("Type add, show, or exit Todos: ")

    match user_action:
        case "add":
            todo = input("Enter a Todo: ")
            list_todos.append(todo)
        case "show":
            print(list_todos)
        case "exit":
            break

print(f"Thank you for making your todo list! \n {list_todos}")
