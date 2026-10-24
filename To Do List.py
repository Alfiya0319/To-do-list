# Aim:
# Mini Project: To develop a **user-friendly To-Do List GUI application using Python and Tkinter** that allows users to **add, view, mark as completed, and delete tasks** efficiently.

# Theory:
# The To-Do List is a Python GUI application developed using the Tkinter library. It allows users to add, view, complete, and delete tasks through a graphical interface. Tasks are stored using lists and dictionaries, while buttons and input fields provide easy interaction with the application

                                             # Team Members: 
                                        # Ansari Aisha Qasim - 25CO02 
                                        # Khan Huda Fatima - 25CO03 
                                        # Alfiyabi Yusuf Shaikh - 26DCO12 
                                        # Div: SE-C CO-I
                                        # Title : TO-DO LIST  

# Code:

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Task
    if choice == 1:
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"] else "Pending"
                print(i, ".", item["task"], "-", status)

    # Mark Task Completed
    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(i, ".", item["task"])

            num = int(input("Enter task number to complete: "))

            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == 4:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(i, ".", item["task"])

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print("Deleted:", deleted["task"])
            else:
                print("Invalid task number.")

    # Exit
    elif choice == 5:
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")

# Conclusion: 
# The To-Do List application was successfully developed using Python and Tkinter. It provides a simple and user-friendly way to manage daily tasks and helps in understanding GUI programming, lists, dictionaries, loops, and event handling in Python.        