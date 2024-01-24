
class Task:
    def __init__(self, task):
        self.task = task
        self.done = False

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "*" if self.done else "o"
        return f"{status} {self.task}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        for task in self.tasks:
            if task.task == task_name:
                print("Task already exists, try again\n")
                return
        self.tasks.append(Task(task_name))

    def mark_task_as_done(self, task_name):
        for task in self.tasks:
            if task.task == task_name:
                task.mark_as_done()
                print("Task marked as done!\n")
                return
        print("Task not found, try again\n")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.task == task_name:
                self.tasks.remove(task)
                print("Task removed\n")
                return
        print("Task not found, try again\n")

    def display_tasks(self):
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("*~ TO DO LIST ~*")
        for task in self.tasks:
            print(task)


def main():
    todo_list = ToDoList()

    while True:
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        todo_list.display_tasks()

        user_choice = input(
            "\n\t~ MENU ~\n"
            "To create a new task, hit 1\n"
            "To finish a task, hit 2\n"
            "To delete a task, hit 3\n"
            "To quit the menu, hit 0\n"
            "Number: "
        )

        if user_choice == "1":
            task_name = input("What's the task?\nName: ")
            todo_list.add_task(task_name)
        elif user_choice == "2":
            task_name = input("What's the task?\nName: ")
            todo_list.mark_task_as_done(task_name)
        elif user_choice == "3":
            task_name = input("What's the task?\nName: ")
            todo_list.remove_task(task_name)
        elif user_choice == "0":
            break
        else:
            print("Incorrect number, try again\n")


if __name__ == "__main__":
    main()


