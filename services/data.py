import json
import os

def validate_structure(structure, path=""):
    # recursively validate the structure consists only of nested dicts with strings or None
    if not isinstance(structure, dict):
        raise ValueError(f"Invalid structure at '{path}': not a dictionary")

    for key, value in structure.items():
        if not isinstance(key, str):
            raise ValueError(f"Invalid key at '{path}': keys must be strings")
        
        # check for valid strings or None
        if not (isinstance(value, str) or value is None or isinstance(value, dict)):
            raise ValueError(f"Invalid value at '{path}/{key}': must be a string, None, or a nested dictionary")

        # recursively validate dicts
        if isinstance(value, dict):
            validate_structure(value, path=f"{path}/{key}" if path else key)

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

            # validate the input json
            try:
                validate_structure(folder_structure)  
            except Exception as e:
                print("Invalid input JSON file")
                print("""Desired format:
                      {
                      'root_string':{
                        'folder_dict_string1':{
                            'folder_dict_string1':{
                                'file_string1':null,
                                'file_string2':null,
                                'file_string3':null
                                }
                            },
                            'file_string1':null
                            }
                        },
                        'folder_dict_string2':{
                        }
                      }
                      """)
                raise e

            return folder_structure
    except json.JSONDecodeError as e:
        raise ValueError(f"Error occurred while decoding the JSON file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred: {e}")

