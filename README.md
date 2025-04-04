# Task CLI

A simple command-line task management application built with Python.

## Overview

Task CLI is a lightweight command-line tool that allows you to manage your tasks efficiently. It stores tasks in a JSON file and provides commands to add, update, delete, and list tasks with different statuses.

## Features

- Add new tasks with descriptions
- Update existing task descriptions
- Delete tasks by ID
- Mark tasks as "todo", "in-progress", or "done"
- List all tasks or filter by status
- Persistent storage using JSON

## Installation

1. Ensure you have Python 3.6+ installed on your system.
2. Download the `task-cli.py` script to your preferred location.
3. Make the script executable (Linux/Mac):
   ```bash
   chmod +x task-cli.py
   ```
4. Optionally, create a symbolic link to run it from anywhere:
   ```bash
   ln -s /path/to/task-cli.py /usr/local/bin/task-cli
   ```

## Usage

```
task-cli add "Task Description"
task-cli update <id> "New Task Description"
task-cli delete <id>
task-cli mark-in-progress <id>
task-cli mark-done <id>
task-cli list
task-cli list [todo|in-progress|done]
```

### Examples

Add a new task:
```bash
task-cli add "Complete the project documentation"
```

Update an existing task:
```bash
task-cli update 1 "Complete the updated project documentation"
```

Mark a task as in-progress:
```bash
task-cli mark-in-progress 1
```

Mark a task as done:
```bash
task-cli mark-done 1
```

Delete a task:
```bash
task-cli delete 1
```

List all tasks:
```bash
task-cli list
```

List only tasks with a specific status:
```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```

## Data Storage

Tasks are stored in a file named `tasks.json` in the same directory as the script. Each task contains the following information:

- `id`: Unique identifier for the task
- `description`: Text description of the task
- `status`: Current status of the task ("todo", "in-progress", or "done")
- `createdAt`: ISO format timestamp of when the task was created
- `updatedAt`: ISO format timestamp of when the task was last updated

## Error Handling

The application includes error handling for:
- Corrupted JSON files
- Invalid task IDs
- Invalid status values
- Missing command arguments

## Project from [roadmap.sh](https://roadmap.sh/projects/task-tracker)

## License

[MIT License](LICENSE)

For questions, [connect with me](santhoshpakkiri550@gmail.com) 
