import argparse
import json
import os
from datetime import datetime as d

parser = argparse.ArgumentParser(description='used to track and manage tasks')
parser.add_argument('-a', '--add', nargs=1, metavar='DESCRIPTION', help='Add a new task with a description and a default status of "todo"', required=False)
parser.add_argument('-u', '--update', nargs=2, metavar=('TASK_ID', 'DESCRIPTION'), help='Update the task by specifying the task ID (an integer) and the new description', required=False)
parser.add_argument('-m', '--mark', nargs=2, metavar=('STATUS', 'TASK_ID'), help='Change the status of a task to "in progress" or "done" based on its ID', required=False)
parser.add_argument('-d', '--delete', nargs=1, metavar='TASK_ID', help='Delete the task by specifying the task ID', required=False)
parser.add_argument('-l', '--list', nargs='?', metavar='STATUS', help='View a list of tasks based on their status (todo, in progress, done, or all)', required=False)

args = parser.parse_args()
json_file = 'task_list.json'
current_datetime = d.now().strftime("%Y-%m-%d %H:%M:%S")
print(args)

def status_check(val)-> object:
    status_def = ('TODO', 'IN-PROGRESS', 'DONE', 'ALL', '*')
    if  val is None:
        return val
    elif val.upper() in status_def:
        return val.upper()
    else:
        parser.error(f"Status should only the following: {status_def}")

def new_task(id, desc, creation_dt)->object:
    data = {
            "id": id,
            "description": desc,
            "status": "TODO",
            "createdAt": creation_dt,
            "updatedAt": None
        }
    return data

def get_max_id()->int:
    max_id = max((record['id'] for record in json_data if 'id' in record), default=0)
    return max_id

def write_file(json_data):
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

def read_json()->object:
    if os.path.isfile(json_file) and os.path.getsize(json_file) > 0:
        with open(json_file, "r") as file:
            data = json.load(file)
    else:
        data = []
        write_file(data)
    return data

def task_id_check(val)-> int:
    try:
        task_id = int(val)
        ids = [item.get('id') for item in json_data if isinstance(item, dict)]
        if task_id in ids:
            return task_id
        else:
            parser.error(f"Task ID {task_id} not found")
    except ValueError:
        parser.error("Task ID must be an integer.")

def add_task():
    desc = args.add[0]
    if not json_data:
        new_id = 1
    else:
        new_id=get_max_id()+1
    new_data = new_task(new_id, desc, current_datetime)
    json_data.append(new_data)
    write_file(json_data)
    print(f"Task added succesfully (ID {new_id})")

def update_task():
    task_id = task_id_check(args.update[0])
    desc = args.update[1]
    for record in json_data:
        if record['id'] == task_id:
            record.update({"description": desc, "updatedAt": current_datetime})
            print(f"Description of Task ID {task_id} updated successfully")
            break
    write_file(json_data)

def mark_task():
    status = status_check(args.mark[0])
    task_id = task_id_check(args.mark[1])
    for record in json_data:
        if record['id'] == task_id:
            record.update({"status": status, "updatedAt": current_datetime})
            print(f"Status of Task ID {task_id} updated successfully")
            break
    write_file(json_data)

def del_task():
    task_id = task_id_check(args.delete[0])
    json_data[:] = [task for task in json_data if task['id'] != task_id]
    print(f"Task ID {task_id} deleted successfully")
    write_file(json_data)

def list_task():
    status = status_check(args.list)
    list_tasks = []
    if args.list is None or status=='ALL' or  status=='*':
        list_tasks = json_data
    else:
        for record in json_data:
            if record['status'] == status:
                list_tasks.append(record)
    if list_tasks:
        print(json.dumps(list_tasks, indent=2))
    else:
        print(f"No record found for status {status}")

json_data = read_json()
if args.add:
    add_task()
elif args.update:
    update_task()
elif args.mark:
    mark_task()
elif args.delete:
    del_task()
else:
    list_task()

# END-OF-PROGRAM