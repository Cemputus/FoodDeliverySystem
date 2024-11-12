# # src/utils.py
# import json
# import os

# def load_json(file_path):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             return json.load(file)
#     return {}

# def save_json(data, file_path):
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)



# src/utils.py
import json

def save_to_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)

def load_from_json(file):
    with open(file, 'r') as f:
        return json.load(f)
