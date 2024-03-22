import json

def get_folder_structure(filename='sample_file_structure.json'):
    # load the folder structure from a JSON file
    with open(filename, 'r') as file:
        folder_structure = json.load(file)
    return folder_structure
