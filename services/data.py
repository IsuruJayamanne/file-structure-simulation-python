import json
import os

def get_folder_structure(filename='sample_file_structure.json'):
    # check filename is a string
    if not isinstance(filename, str) or not filename:
        raise ValueError("Filename must be a valid string.")
    
    # check if the file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    
    try:
        # load the folder structure from a JSON file
        with open(filename, 'r') as file:
            folder_structure = json.load(file)
            return folder_structure
    except json.JSONDecodeError as e:
        raise ValueError(f"Error occurred while decoding the JSON file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred: {e}")

