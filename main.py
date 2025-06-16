menu = """
========= Menu =========
1. Task qo'sish
2. Tasklarni ko'rish
3. Taskni o'chirish
4. Taskni yangilash
5. Chiqish
"""
todos: list[str] = []


def print_menu() -> None:
    "print menu"
    print(menu)

def add_task() -> None:
    "add task"
    name = input("yangi task nomini kiriting: ").capitalize()
    if name in todos:
        print("bunday todo mavjud.")
    else:
        todos.append(name)
        print("todo qoshildi.")

def print_todos() -> None:
    "print todos"
    print("Todo List:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index} - {todo}")


def main() -> None:
    "main funciton"

    while True:
        print_menu()

        choice = input("Menu tanlang: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            print_todos()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        else:
            print("xato menu")

main()  


