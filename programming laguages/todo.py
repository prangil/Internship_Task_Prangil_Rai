import mysql.connector

# Database connection details
DB_CONFIG = {
    "host": "localhost",
    "user": "root",       
    "password": "",  
    "database": "todo_db",   
}


def connect_to_database():
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()


def initialize_database():
    """Ensure the tasks table exists."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content VARCHAR(255) NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


def get_all_tasks():
    """Retrieve all tasks from the database."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT id, content FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return tasks


def add_task(task_content):
    """Add a new task to the database."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (content) VALUES (%s)", (task_content,))
    connection.commit()
    cursor.close()
    connection.close()
    print("Task added successfully!")


def delete_task(task_id):
    """Delete a task from the database."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print("Task deleted successfully!")


def update_task(task_id, new_content):
    """Update a task in the database."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET content = %s WHERE id = %s", (new_content, task_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Task updated successfully!")


def display_tasks():
    """Display all tasks."""
    tasks = get_all_tasks()
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nTasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")
        print()


def main():
    """Main program loop."""
    initialize_database()

    while True:
        print("\nTodo List App (MySQL Version)")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task_content = input("Enter the new task: ").strip()
            if task_content:
                add_task(task_content)
            else:
                print("Task cannot be empty!")
        elif choice == "3":
            display_tasks()
            try:
                task_id = int(input("Enter the task ID to edit: "))
                new_content = input("Enter the new content for the task: ").strip()
                if new_content:
                    update_task(task_id, new_content)
                else:
                    print("Task content cannot be empty!")
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "4":
            display_tasks()
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "5":
            print("Exiting the Todo List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
