## Todolist Project:
class Todolist():
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append({"task":task,"done":False})
        print(f"Task '{task}' added succefully.")

    def remove_task(self,task):
        for t in self.tasks:
            if t["task"]==task:
                self.tasks.remove(t)
                print(f"Task Removed successfully")
            else:
                print("Task is Not found.")

    def Display_task(self):
        if self.tasks:
            print(f"Your To-Do list:")
            for index,task in enumerate(self.tasks,start=1):
                status="Done" if task["done"] else "Not done"
                print(f"{index}.{task["task"]} - {status}")
        else:
            print(f"print Your To-do list is empty.")
 
    def Mark_completed(self):
        task_index = int(input("Enter the task number to mark as done:")) - 1  # Convert to 0-based index
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print("Task marked as done")
        else:
            print("Invalid Task Number")

        
def main():
    todolist=Todolist()
    while True:
        print("\n Enter Your option:")
        print("1.Add Task:")
        print("2.Remove Task:")
        print("3.Display Tasks:")
        print("4.Mark Task As Completed:")
        print("5.Exit")

        choice=input("Enter your choice:")
        if choice=='1':
            task=input("Enter the Task to add:")
            todolist.add_task(task)

        elif choice=='2':
            task=input("Enter the task to Remove:")
            todolist.remove_task(task)
        
        elif choice=='3':
            todolist.Display_task()
        
        elif choice=='4':
            #task=input("Enter the task to mark as completed:")
            todolist.Mark_completed()
        
        elif choice=='5':
            print("Existing the program.")
            break
        else:
            print("Invalid choice.please Enter the valid")

if __name__=="__main__":
    main()
        

    

    
