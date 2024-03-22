from services.gui import display_folder_structure

# sample folder structure in JSON
folder_structure = {
    "Project": {
        "src": {
            "__init__.py": None,
            "main.py": None,
            "module1.py": None,
        },
        "docs": {
            "file1.txt": None,
        },
        "tests": {
            "__init__.py": None,
            "test_module1.py": None,
        },
        "README.md": None,
    }
}

def main():
    display_folder_structure(folder_structure)

if __name__ == "__main__":
    main()
