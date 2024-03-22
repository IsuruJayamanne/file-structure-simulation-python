from services.gui import display_folder_structure
from services.data import get_folder_structure

def main():
    # -----------------------------------
    # input JSON file name
    filename='sample_file_structure.json'
    # -----------------------------------

    # load the data from file
    folder_structure = get_folder_structure(filename)

    # main code
    display_folder_structure(folder_structure)

if __name__ == "__main__":
    main()
