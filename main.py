class Task:
    def __init__(self, task):
        self.task = task
        self.done = False
    
    def __str__(self):
        string = self.task
        if self.done == False:
            string="o "+string
        else:
            string="* "+string
        return string


rep = 1
list = []
while (rep !=0):
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("*~TO DO LIST~*")
    for i in list:
        print(i)
    rep = input("\n\t~menu~\nto create a new task, hit 1\nto finish a task, hit 2\nto delete a task, hit 3\nto quit menu, hit 0\nnumber : ")
    match rep:
        case "1":
            name = input("what's the task ?\nname : ")
            for i in list:
                if i.task==name:
                    print("task already exists, try again\n")
                    break
            list.append(Task(name))
        case "2":
            name = input("what's the task ?\nname : ")
            for i in list:
                if i.task==name:
                    i.done=True
                    print("task marked as done ! \n")

        case "3": 
            name = input("what's the task ?\nname : ")
            for i in list:
                if i.task==name:
                    list.remove(i)
                    print("task removed\n")
                    break

            print("task not found, try again\n")          
        case "0":
         break
        case _:
            print("incorrect number, try again\n")
            






