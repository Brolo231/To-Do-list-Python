def todo():
    print("*******************")
    print("\tTo Do List:")
    print("'a' to add\n'c' to complete\n'r' to remove\n'e' to empty list")

    run = True
    while run:

        with open("ToDoList.txt", 'r') as tasks:
            lines = tasks.readlines()
            global list_len
            list_len = len(lines) + 1
        tasks.close()

        list()
        answer = input("Action: ")
        if answer.lower().strip() == "a":
            add()
        elif answer.lower().strip() == "c":
            complete()
        elif answer.lower().strip() == "r":
            remove()
        elif answer.lower().strip() == "e":
            empty()

def list():
    with open("ToDoList.txt") as list:
        print("*******************")
        print("\tTasks:")
        for line in list:
            print(line, end='')
        print("\n*******************")


def add():
    with open("ToDoList.txt", 'a') as tasks:
        question = input("Enter a task to add: ")
        if question:
            tasks.write(question.lower().strip() + ":incomplete" '\n')
            tasks.close()



def complete():
    with open("ToDoList.txt", "r") as tasks_file:
        lines = tasks_file.readlines()

    if not lines:
        print("No tasks to complete")
        return

    question = input("Enter a task to mark as completed: ")

    with open("ToDoList.txt", "w") as tasks_file:
        task_found = False
        for line in lines:
            if line.strip("\n") != question + ":incomplete" and line.strip("\n") != question + ":complete":
                tasks_file.write(line)
            else:
                task_found = True

        if task_found:
            print("Task marked as complete successfully")
            tasks_file.write(question + ":complete")
        else:
            print("Please enter a valid task to mark as complete")

    todo()

def remove():
    with open("ToDoList.txt", "r") as tasks_file:
        lines = tasks_file.readlines()

    if not lines:
        print("No tasks to remove")
        return

    question = input("Enter a task to remove: ")

    with open("ToDoList.txt", "w") as tasks_file:
        task_found = False
        for line in lines:
            if line.strip("\n") != question + ":incomplete" and line.strip("\n") != question + ":complete":
                tasks_file.write(line)
            else:
                task_found = True

        if task_found:
            print("Task removed successfully")
        else:
            print("Please enter a valid task to remove")

    todo()

def empty():

    with open("ToDoList.txt", "w") as tasks:
        tasks.write("")


todo()
