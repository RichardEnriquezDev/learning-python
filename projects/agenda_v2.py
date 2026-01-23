
####### PERSONAL PLANNER #######

task = []
schedule_menu = [
    "Add task",
    "See task",
    "Mark task as done",
    "Delete task",
    "Save task"
    ]
def show_menu(title, options, extra_option=None):
    print("\n" + title)
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    
    if extra_option:
        print(f"{len(options) + 1}) {extra_option}")
    
def see_task():
    if not task:
        print("There's no homework assigned.")
        return
    print("\nTask list\n")
    for i, assignment in enumerate(task, start=1):
        estado = "✔" if assignment[1] else " "
        print(f"({i}) [{estado}] {assignment[0]}")

def delete_task():
    if not task:
        print("There are no task to delete.")
        return   
    see_task()
    number = int(input("\nEnter task number to delete: "))
    index = int(number) - 1
    assignment = task[index]
    confirm = input(f"\n¿Delete '{assignment}'? (y/n): ")
        
    if confirm.lower() == "y": 
        task.pop(index)
        print("\nTask removed.")
    else:
        print("\nOperation cancelled.")

def mark_task():
    if not task:
        print("There are no tasks to mark")
        return
    see_task()
    number = int(input("\nEnter task number to mark:"))
    index = number - 1
    task[index][1] = True
    print("\nTask marked correctly")

def save_task():
    with open("practice.txt", "w") as files:
        for assignment in task:
            files.write(f"{assignment[0]}|{assignment[1]}\n")

def load_tasks():
    try:
        with open("practice.txt", "r") as files:
            for line in files:
                text, status = line.strip() .split("|")
                task.append([text, status == "True"])
        print("\nTask loaded successfully.")
    except FileNotFoundError:
        pass

load_tasks()

while True:
    show_menu("PERSONAL PLANER\n",
            schedule_menu,
            "Get out")
    option = int(input("\nSelect an option: "))
    
    if option == 1:
        assignment = input("\nEnter a new task: ")
        task.append([assignment, False])
        print("\nTask added successfully.")
    
    elif option == 2:
        see_task()
    
    elif option == 3:
        mark_task()

    elif option == 4:
        delete_task()
    
    elif option == 5:
        save_task()
        print("\nTask saved. Exiting the program...\n")
        break
    elif option == len(schedule_menu) + 1:
        print("\nExiting the program...\n")
        break
    else:
        print("Invalid option.")