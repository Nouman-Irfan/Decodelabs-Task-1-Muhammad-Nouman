# =========================================
# DECODE LABS - PROJECT 1
# PYTHON PROGRAM: TO-DO LIST APPLICATION
# =========================================


# List to store tasks temporarily in RAM
tasks = []


# =========================================
# FUNCTION: Load tasks from file
# =========================================
def load_tasks():

    try:

        file = open("tasks.txt", "r")

        for line in file:

            # Remove extra newline character
            task = line.strip()

            # Add task into list
            tasks.append(task)

        file.close()

    except FileNotFoundError:

        # Create file if it does not exist
        file = open("tasks.txt", "w")
        file.close()


# =========================================
# FUNCTION: Save a new task into file
# =========================================
def save_task(task):

    file = open("tasks.txt", "a")

    file.write(task + "\n")

    file.close()


# =========================================
# FUNCTION: Add new task
# =========================================
def add_task():

    print("\n========== ADD TASK ==========")

    task = input("Enter your task: ")

    # Add task into list
    tasks.append(task)

    # Save task into file
    save_task(task)

    print("Task added successfully!")


# =========================================
# FUNCTION: View all tasks
# =========================================
def view_tasks():

    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:

        print("No tasks available.")

    else:

        i = 0

        for task in tasks:

            print(str(i + 1) + ". " + task)

            i = i + 1


# =========================================
# FUNCTION: Main menu
# =========================================
def menu():

    while True:

        print("\n================================")
        print("         TO-DO LIST")
        print("================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # ==============================
        # ADD TASK
        # ==============================
        if choice == "1":

            add_task()

        # ==============================
        # VIEW TASKS
        # ==============================
        elif choice == "2":

            view_tasks()

        # ==============================
        # EXIT PROGRAM
        # ==============================
        elif choice == "3":

            print("\nExiting program...")
            print("Your tasks are saved in file.")

            break

        # ==============================
        # INVALID INPUT
        # ==============================
        else:

            print("Invalid choice! Please try again.")


# =========================================
# PROGRAM START
# =========================================

# Load previous tasks from file
load_tasks()

# Start menu
menu()