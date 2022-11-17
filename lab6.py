import argparse
import json
import tempfile
import os

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#-------------------------------------------------  
def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}
#-------------------------------------------------    
def add(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))
#-------------------------------------------------  
def get(key):
    data = get_data()
    return data.get(key)
#-------------------------------------------------  
parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key')
parser.add_argument('--val', help='Value')
args = parser.parse_args()

if args.key and args.val:
    add(args.key, args.val)
elif args.key:
    print(get(args.key))
else:
    print("Wrong input")