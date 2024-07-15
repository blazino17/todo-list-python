# To-Do List Python Project

This is a simple command-line To-Do List application written in Python.
It allows users to manage their tasks by adding, viewing, marking as completed, and deleting tasks. Additionally, tasks can be saved to and loaded from a file.

## Features

- Add tasks to the list
- View all tasks with their status (completed or not)
- Mark tasks as completed
- Delete tasks
- Save tasks to a file
- Load tasks from a file

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/blazino17/todo-list-python.git
    cd todo-list-python
    ```

2. Run the application:

    ```bash
    python todo.py
    ```

### Usage

When you run `todo.py`, you will be presented with a menu to interact with the To-Do List application. Here are the options:

1. **Add Task**: Enter the task description to add a new task.
2. **View Tasks**: View all tasks along with their status (completed or not).
3. **Mark Task as Completed**: Enter the task index to mark it as completed.
4. **Delete Task**: Enter the task index to delete it.
5. **Save Tasks to File**: Save all tasks to `tasks.txt`.
6. **Load Tasks from File**: Load tasks from `tasks.txt`.
7. **Exit**: Save tasks and exit the application.

### Example

```plaintext
=== To-Do List ===
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Save Tasks to File
6. Load Tasks from File
7. Exit

Enter your choice: 1
Enter task: Complete homework
Task added!

=== To-Do List ===
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Save Tasks to File
6. Load Tasks from File
7. Exit

Enter your choice: 2
Your tasks:
1. [ ] Complete homework
