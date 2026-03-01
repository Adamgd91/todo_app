list_todos = []

while True:
    user_action = input("Type add or show Todos: ")

    match user_action:
        case "add":
            todo = input("Enter a Todo: ")
            list_todos.append(todo)
        case "show":
            print(list_todos)
