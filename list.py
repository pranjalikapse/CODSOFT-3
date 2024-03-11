class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found in the list.')

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')
        else:
            print("Your To-Do List is empty.")

    def update_task(self, index, new_task):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f'Task {index} updated successfully.')
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
        print(f'Tasks saved to {filename}.')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print(f'Tasks loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found.')

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Update Task")
        print("5. Save To File")
        print("6. Load From File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '5':
            filename = input("Enter filename to save: ")
            todo_list.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load: ")
            todo_list.load_from_file(filename)
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

