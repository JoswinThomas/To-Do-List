import json
def save_tasks():
    with open("tasks.txt","w") as file:
        json.dump(tasks,file)
def load_tasks():
    global tasks
    try:
        with open("tasks.txt","r") as file:
            tasks = json.load(file)
    except:
        tasks=[]

tasks=[]
#initializing a list to add the tasks

def add_task():
    task=input("Enter task:")
    tasks.append(task)
    save_tasks()
    print("Task added!")
#To delete the task
def delete_task():
    view_task()
    n=int(input("Enter task number to delete: "))
    if 1<=n<=len(tasks):
        tasks.pop(n-1)
        save_tasks()
        print("Task deleted!")
    else:
        print("Invalid number!")
#viewing the task that user have inputed
def view_task():
    if len(tasks)==0:
        print("No task available.")
    else:
        
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i+1,".",tasks[i])
def main():
    load_tasks()
    while True:
        print("\n===================================================================")
        print("                            TO-DO LIST                               ")
        print("\n===================================================================")
        print("\n1.add task")
        print("\n2.view tasks")
        print("\n3.Delete Task")
        print("\n4.exit")
        print("\n===================================================================")
        choice=input("Enter choice: ")

        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            delete_task()
        elif choice=="4":
            print("Goodbye!")
            break
        else:
            print("invalid choice!")
main()
            