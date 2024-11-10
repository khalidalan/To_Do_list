def add_task(todo_list):
    """
    Adds a task to the to-do list.
    
    Parameters:
    todo_list (list): The list where tasks are stored.

    The function prompts the user for a task, ensures the task is not empty,
    and adds it to the to-do list.
    """
    task = input("Enter a task: ")
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")


def view_tasks(todo_list):
    """
    Displays all tasks in the to-do list.
    
    Parameters:
    todo_list (list): The list containing tasks.

    If the list is empty, it informs the user. Otherwise, it prints each task
    with a corresponding index number for reference.
    """
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nCurrent tasks:")
        for idx, task in enumerate(todo_list, 1):  # enumerate starts index at 1
            print(f"{idx}. {task}")
        print()  # Extra line for readability


def remove_task(todo_list):
    """
    Removes a task from the to-do list by index.
    
    Parameters:
    todo_list (list): The list containing tasks.

    If the list is empty, it informs the user. Otherwise, it displays all tasks
    with index numbers and prompts the user to enter the number of the task
    they want to remove. Handles invalid input and provides feedback.
    """
    if not todo_list:
        print("No tasks to remove.")
    else:
        view_tasks(todo_list)  # Show tasks to let user choose which one to remove
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(todo_list):  # Ensure valid task number
                removed_task = todo_list.pop(task_number - 1)  # Remove by index
                print(f"Task '{removed_task}' removed.")
            else:
                print(f"Invalid task number. Please enter a number between 1 and {len(todo_list)}.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def main():
    """
    The main function that controls the to-do list application.

    It presents a command prompt to the user with options to:
    - Add a task
    - View tasks
    - Remove a task
    - Exit the program

    The loop continues until the user chooses to exit, with appropriate
    validation and error handling for user inputs.
    """
    todo_list = []  # Initialize an empty to-do list

    while True:
        # Prompt user for action, strip whitespaces and convert to lowercase for consistency
        user_action = input("\nEnter a command (add, view, remove, exit): ").strip().lower()
        
        if user_action == "add":
            add_task(todo_list)
        
        elif user_action == "view":
            view_tasks(todo_list)
        
        elif user_action == "remove":
            remove_task(todo_list)
        
        elif user_action == "exit":
            # Confirm exit with the user to avoid accidental exits
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm_exit == "yes":
                print("Exiting the program. Goodbye!")
                break  # Exit the loop to stop the program
            else:
                print("Exit canceled.")
        
        else:
            # Handle invalid commands entered by the user
            print("Invalid command. Please enter 'add', 'view', 'remove', or 'exit'.")

if __name__ == "__main__":
    main()  # Entry point to start the program
