# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def delete_task(index):
    try:
        del tasks[index - 1]
        print("Task deleted!")
    except IndexError:
        print("Task index out of range!")

# Sample usage
add_task("Complete homework")
add_task("Prepare for presentation")
view_tasks()
delete_task(1)
view_tasks()
