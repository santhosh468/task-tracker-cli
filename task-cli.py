import sys
import os
import json
import datetime

tasks_file = "tasks.json"

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    try:
        with open(tasks_file, 'r') as file:
            tasks = json.load(file)
            max_id = 0
            valid_tasks = []
            for task in tasks:
                # Ensure required fields exist
                if 'description' not in task:
                    task['description'] = "No description"  # Add default description
                if 'id' not in task or not isinstance(task['id'], int):
                    max_id += 1
                    task['id'] = max_id
                # Handle dates
                if "createdAt" not in task or not isinstance(task["createdAt"], str):
                    task["createdAt"] = datetime.datetime.now().isoformat()
                if "status" not in task:
                    task["status"] = "todo"
                valid_tasks.append(task)
            return valid_tasks
    except json.JSONDecodeError:
        print(f"Error: The {tasks_file} is corrupted")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    try:
        with open(tasks_file, 'w') as file:
            json.dump(tasks, file, indent=2)
            return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    now = datetime.datetime.now().isoformat()
    new_task = {
        'id': get_next_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }

    tasks.append(new_task)

    if save_tasks(tasks):
        print(f"Task successfully added (ID: {new_task['id']})")
    else:
        print("Task not added")

def update_task(task_id, description):
    tasks = load_tasks()
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be a number")
        return
        
    task_found = False

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.datetime.now().isoformat()
            task_found = True
            break
    
    if task_found:
        if save_tasks(tasks):
            print(f"The task is updated at ID: {task_id}")
        else:
            print("The task is not saved.")
    else:
        print(f"The task at ID: {task_id} is not found.")

def delete_task(task_id):
    tasks = load_tasks()
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be a number")
        return
        
    initial_count = len(tasks)

    updated_tasks = [task for task in tasks if task['id'] != task_id]

    if initial_count > len(updated_tasks):
        if save_tasks(updated_tasks):
            print(f"The task at ID: {task_id} was deleted successfully.")
        else:
            print("Task was not deleted")
    else:
        print(f"No task found at ID: {task_id}")

def set_task_status(task_id, status):
    status = status.lower()
    valid_statuses = ['todo', 'in-progress', 'done']
    if status not in valid_statuses:
        print(f"Error: Invalid status. Use {', '.join(valid_statuses)}.")
        return
    
    tasks = load_tasks()

    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be a number")
        return
        
    task_found = False

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.datetime.now().isoformat()
            task_found = True
            break

    if task_found:
        if save_tasks(tasks):
            print(f"The task {task_id} is marked as {status}")
        else:
            print("Failed to update task status")
    else:
        print(f"No task found at ID: {task_id}")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        status = status.lower()
        filtered = []
        for task in tasks:
            if task["status"].lower() == status:
                filtered.append(task)
        tasks = filtered

    if not tasks:
        if status:
            print(f"No tasks found with status: {status}")
        else: 
            print("No tasks found")
        return
    
    print("\nID  | Status       | Created at         | Description")
    print("-" * 65)

    for task in tasks:
        try:
            created_at_dt = datetime.datetime.fromisoformat(task["createdAt"])
            createdAt = created_at_dt.strftime("%d.%m.%Y, %H:%M")
        except ValueError:
            createdAt = "Invalid Date"
        
        status_display = task["status"].ljust(12)
        print(f"{task['id']:<3} | {status_display} | {createdAt:<18} | {task['description']}")

    print("-" * 65)
    print()

def print_usage():
    print("Usage:")
    print(" task-cli add \"Task Description\"")
    print(" task-cli update <id> \"New Task Description\"")
    print(" task-cli delete <id>")
    print(" task-cli mark-in-progress <id>")
    print(" task-cli mark-done <id>")
    print(" task-cli list")
    print(" task-cli list [todo|in-progress|done]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description")
            print_usage()
            return
        add_task(sys.argv[2])
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing task ID or description")
            print_usage()
            return
        update_task(sys.argv[2], sys.argv[3])
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            print_usage()
            return
        delete_task(sys.argv[2])
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            print_usage()
            return
        set_task_status(sys.argv[2], "in-progress")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            print_usage()
            return
        set_task_status(sys.argv[2], "done")
    elif command == "list":
        if len(sys.argv) >= 3:
            status = sys.argv[2]
            if status.lower() not in ['todo', 'in-progress', 'done']:
                print(f"Invalid status: {status}. Use 'todo', 'in-progress', or 'done'.")
                return
            list_tasks(status)
        else:
            list_tasks()
    else:
        print_usage()

if __name__ == "__main__":
    main()