import json
import os

FILE_NAME = 'data.json'

def write_json(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def read_json():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

#CRUD Operations 

def create_record(record_id, name, role):
    data = read_json()
    if record_id in data:
        print("Record already exists.")
    else:
        data[record_id] = {"name": name, "role": role}
        write_json(data)
        print(f"Created: {name}")

def get_record(record_id):
    data = read_json()
    record = data.get(record_id, "Record not found.")
    print(f"Read: {record}")

def update_record(record_id, new_role):
    data = read_json()
    if record_id in data:
        data[record_id]['role'] = new_role
        write_json(data)
        print(f"Updated {record_id} to {new_role}")
    else:
        print("Record not found.")

def delete_record(record_id):
    data = read_json()
    if record_id in data:
        del data[record_id]
        write_json(data)
        print(f"Deleted {record_id}")
    else:
        print("Record not found.")

create_record("1", "John Doe", "Developer")
get_record("1")
update_record("1", "Senior Developer")
delete_record("1")