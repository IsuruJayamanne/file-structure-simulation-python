from services.gui import display_folder_structure
from services.data import get_folder_structure

def main():
    folder_structure = get_folder_structure()
    display_folder_structure(folder_structure)

if __name__ == "__main__":
    main()
