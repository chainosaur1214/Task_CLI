# Task Tracker CLI

Task Tracker CLI is a simple command-line application that allows you to add, update, mark, and delete tasks in a JSON file. The application also lets you view a list of tasks based on their status.

## Features

- **Add Task**: Add a new task with a description and a default status of "todo".
- **List Tasks**: View a list of tasks based on their status (todo, in progress, done, or all).
- **Update Task Description**: Update the description of an existing task based on its ID.
- **Mark Task Status**: Change the status of a task to "in progress" or "done" based on its ID.
- **Delete Task**: Remove an existing task based on its ID.

## Usage

```
usage: task_cli.py [-h] [-a DESCRIPTION] [-u TASK_ID DESCRIPTION] [-m STATUS TASK_ID] [-d TASK_ID] [-l [STATUS]]

used to track and manage tasks

optional arguments:
  -h, --help            show this help message and exit
  -a DESCRIPTION, --add DESCRIPTION
                        Add a new task with a description and a default status of "todo"
  -u TASK_ID DESCRIPTION, --update TASK_ID DESCRIPTION
                        Update the task by specifying the task ID (an integer) and the new description
  -m STATUS TASK_ID, --mark STATUS TASK_ID
                        Change the status of a task to "in progress" or "done" based on its ID
  -d TASK_ID, --delete TASK_ID
                        Delete the task by specifying the task ID
  -l [STATUS], --list [STATUS]
                        View a list of tasks based on their status (todo, in progress, done, or all)
```


### Add Task

To add a new task, use the `-a` or `--add` argument. Default status is "todo":

```bash
python3 task-cli.py -a "New Task Description"
```

### List Tasks

To list tasks based on their status, use the `-l` or `--list` argument. You can specify "todo", "in-progress", "done", "all".
You can also use "ALL", "*" or even empty args to view all of the records:

```bash
python3 task-cli.py -l "todo"
```

```bash
python3 task-cli.py -l
```

### Update Task Description

To update the description of a task, `-u` or `--update` argument. Specify additional requirements task_id and modified task description:

```bash
python3 task-cli.py -u 2 "Updated Task Description"
```

### Mark Task Status

To mark a task as "in-progress" or "done", use `-m` or `--mark` argument to provide the task_id and new status:

```bash
python3 task-cli.py -m "in progress" 2
```

### Delete Task

To delete a task, use `-d` or `--delete` argument and specify the task_id you want to delete:

```bash
python3 task-cli.py -d 2
```

## Notes

- Ensure that the `test_tasks.json` file exists in the same directory as the script for it to function correctly.
- The application will create the `test_tasks.json` file if it does not already exist when adding a new task.

## Project Link

For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).
