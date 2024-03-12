class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)

    def remove_task(self, task):
        if task in self.todos:
            self.todos.remove(task)

    def display_tasks(self):
        print("Todo List:")
        for idx, task in enumerate(self.todos, start=1):
            print(f"{idx}. {task}")


def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
        
