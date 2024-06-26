# Tree View file selection simulation from JSON input in Python

Reads a JSON file of a file structure and shows in a UI. Simulates file selection.

- Uses Tkinter library for GUI
- Loads JSON file as input
- Simulate file select from mouse with attach and detach

## Instructions

### Prerequisites
- Python3
    - Dependancies : tkinter, json

### Configuration

#### Sample JSON file is provided and can be [run](#run_section) with it. Follow the below steps to input a custom JSON file if required.

Save the JSON file in the project root.

Update the JSON file name in ["main.py"](main.py)
- Replace the filename value (line 10)

```python
# -----------------------------------
# input JSON file name
filename='your file name here .json'
# -----------------------------------
```

Below is a sample valid JSON input
```json
{
    "root_string":{
        "folder_dict_string1":{
            "folder_dict_string1":{
                "file_string1":null,
                "file_string2":null,
                "file_string3":null
                }
            },
            "file_string1":null
        },
        "folder_dict_string2":{
    }
}
```

### To run <a name="run_section"></a>

Run from terminal

```bash
python3 main.py
```

- Opens a UI in a new window
- Close the window to exit

### Notes:

Tested on macOS.
