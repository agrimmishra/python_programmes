def menuPrinter():
    """
    Print the menu options for the to-do list application.
    """
    menu = """PRESS : 
    1: to add task
    2: to show the task
    3: to delete task
    0: to exit the program"""
    
    print(menu)
    

# Initialize an empty to-do list
toDoList = []

def add_task(task):
    """
    Add a new task to the to-do list.

    Parameters:
    task (str): The task to be added to the list.
    """
    toDoList.append(task)

def show_list():
    """
    Display all tasks in the to-do list.
    """
    if toDoList:
        for i, task in enumerate(toDoList, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.") 

def delete_task():
    """
    Delete a task from the to-do list by its index.
    """
    if toDoList:
        try:
            index = int(input("Enter the task number to be deleted: "))
            if 1 <= index <= len(toDoList):
                del_task = toDoList.pop(index - 1)
                print(f"'{del_task}' has been deleted from the to-do list.")
            else:
                print("Invalid index entered.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your to-do list is empty.")

# Main driver function
while True:
    menuPrinter()  # Display the menu options
    try:
        ch = int(input("Enter your choice: "))
        match ch:
            case 1:
                task = input("Enter task: ")
                add_task(task)  # Add a new task to the list
            case 2:
                show_list()  # Display all tasks
            case 3:
                delete_task()  # Delete a task by its index
            case 0:
                break  # Exit the program
            case _:
                print("Invalid choice. Please enter a number between 0 and 3.")
    except ValueError:
        print("Please enter a valid number.")
