class Task:
    def __init__(self, task):
        self.task = task
        self.done = False

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "\033[32m*\033[0m" if self.done else "\033[33mo\033[0m"
        return f"{status} {self.task}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task_name = task_name.strip()  # Remove leading/trailing spaces
        if not task_name:
            print("\033[33mTask name cannot be empty, try again\033[0m\n")
            return

        for task in self.tasks:
            if task.task.lower() == task_name.lower():
                print("\033[33mTask already exists, try again\033[0m\n")
                return
        self.tasks.append(Task(task_name))
        print("\033[1;32mTask added!\033[0m\n")

    def mark_task_as_done(self, task_name):
        task_name = task_name.strip()  # Remove leading/trailing spaces
        if not task_name:
            print("\033[33mTask name cannot be empty, try again\033[0m\n")
            return

        for task in self.tasks:
            if task.task.lower() == task_name.lower():
                task.mark_as_done()
                print("\033[1;32mTask marked as done!\033[0m\n")
                return
        print("\033[33mTask not found, try again\033[0m\n")

    def remove_task(self, task_name):
        task_name = task_name.strip()  # Remove leading/trailing spaces
        if not task_name:
            print("\033[33mTask name cannot be empty, try again\033[0m\n")
            return

        for task in self.tasks:
            if task.task.lower() == task_name.lower():
                self.tasks.remove(task)
                print("\033[1;32mTask removed!\033[0m\n")
                return
        print("\033[33mTask not found, try again\033[0m\n")

    def display_tasks(self):
        print("\033[94m~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\033[0m")
        print("\033[94m*~ TO DO LIST ~*\033[0m")
        for task in self.tasks:
            print(task)


def main():
    todo_list = ToDoList()

    while True:
        todo_list.display_tasks()

        user_choice = input(
            "\n\t\033[94m~ MENU ~\033[0m\n"
            "\033[96mTo create a new task, hit 1\n"
            "To finish a task, hit 2\n"
            "To delete a task, hit 3\n"
            "To quit the menu, hit 0\n"
            "Number: \033[0m"
        )

        if not user_choice.isdigit():
            print("\033[33mIncorrect number, try again\033[0m\n")
            continue

        if user_choice == "1":
            task_name = input("\033[96mWhat's the task?\nName: \033[0m")
            todo_list.add_task(task_name)
        elif user_choice == "2":
            task_name = input("\033[96mWhat's the task?\nName: \033[0m")
            todo_list.mark_task_as_done(task_name)
        elif user_choice == "3":
            task_name = input("\033[96mWhat's the task?\nName: \033[0m")
            todo_list.remove_task(task_name)
        elif user_choice == "0":
            break
        else:
            print("\033[33mIncorrect number, try again\033[0m\n")


if __name__ == "__main__":
    main()
