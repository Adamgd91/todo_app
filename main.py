list_todos = []

while True:
    user_action = input("Type add, show, or exit Todos: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a Todo: ")
            list_todos.append(todo)
        case "show":
            for i in list_todos:
                print(i)
        case "exit":
            break

print(f"Thank you for making your todo list! \n {list_todos}")
