class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the list.")
    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for index, task in enumerate(self.tasks, start=1): 
                print(f"{index}. {task}")
def main():
    todo_list = TodoList()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the application. Goodbye!\nPlease, visit me again")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    main()
