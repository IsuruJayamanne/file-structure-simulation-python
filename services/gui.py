import tkinter as tk
from tkinter import ttk

def build_tree(parent, tree_data, parent_tree=''):
    # build the tree view from the JSON
    for item, children in tree_data.items():
        item_id = parent.insert(parent_tree, 'end', text=item)
        if isinstance(children, dict):
            build_tree(parent, children, item_id)

def display_folder_structure(folder_structure):
    # init the GUI window
    root = tk.Tk()
    root.title("Folder Structure Viewer")

    tree_view = ttk.Treeview(root)
    tree_view.pack(expand=True, fill='both')

    # build tree
    build_tree(tree_view, folder_structure)

    root.mainloop()
