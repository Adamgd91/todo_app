list_todos = []

while True:
    user_action = input("Type add, show, or exit Todos: ").lower()
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a Todo: ")
            list_todos.append(todo)
        case "show":
            for i in list_todos:
                print(i)
        case "exit":
            for i in list_todos:
                print(i)
            break

print(list_todos)


def my_todos_func(list_todos):
    return ", ".join(list_todos)


print(f"Thank you for making your todo list! {my_todos_func(list_todos)}!")
