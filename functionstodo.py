def get_todos(filepath="todos.txt"):
    """ Read the text file and
    return a list of todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write new todo items list  to a text file """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
