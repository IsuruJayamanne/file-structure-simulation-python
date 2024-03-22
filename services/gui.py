import tkinter as tk
from tkinter import ttk

# clicked file list
clicked_files = []

def build_tree(parent, tree_data, parent_tree=''):
    # build the tree view from the JSON
    for item, children in tree_data.items():
        item_id = parent.insert(parent_tree, 'end', text=item, tags=("unclicked",))
        if isinstance(children, dict):
            build_tree(parent, children, item_id)

def get_item_full_path(item_id):
    # generate the full path of an item from its ID
    parent_id = tree_view.parent(item_id)
    if parent_id == '':
        return tree_view.item(item_id, 'text')
    else:
        return get_item_full_path(parent_id) + "/" + tree_view.item(item_id, 'text')

def on_item_click(event):
    # handle item clicks
    item_id = tree_view.identify_row(event.y)
    if item_id and not tree_view.tag_has("clicked", item_id):
        item_text = tree_view.item(item_id, 'text')
        item_path = get_item_full_path(item_id)
        # add clicked item to a list
        clicked_files.append(item_path) 
        # tag the item as clicked to handle background color change
        tree_view.item(item_id, tags=("clicked",))  

def show_clicked_files():
    # show the names of files clicked and
    text_widget.delete(1.0, tk.END)
    if clicked_files:
        text_widget.insert(tk.END, "Attached files:\n" + "\n".join(clicked_files))
    else:
        text_widget.insert(tk.END, "--empty--")

def detach_files():
    # handle file detaching
    global clicked_files
    # clear clicked files list
    clicked_files.clear()  
    for item in tree_view.get_children():
        # reset the tag to unclicked
        tree_view.item(item, tags=("unclicked",))  
        # reset background colours
        reset_background_colors(item)  
    text_widget.delete(1.0, tk.END)

def reset_background_colors(item):
    # reset background colors
    tree_view.item(item, tags=("unclicked",))
    for child in tree_view.get_children(item):
        reset_background_colors(child)

def display_folder_structure(folder_structure):
    root = tk.Tk()
    root.title("Folder Structure Viewer")

    # background colour styles
    style = ttk.Style(root)
    style.configure("Treeview", rowheight=25)
    style.map("Treeview",
              background=[("selected", "skyblue")],
              foreground=[("selected", "white")])
    style.configure("Clicked.Treeview.Item", background="skyblue")

    global tree_view, text_widget
    tree_view = ttk.Treeview(root, style="Treeview", selectmode="extended")
    tree_view.pack(expand=True, fill='both')

    tree_view.bind("<Button-1>", on_item_click)
    tree_view.tag_configure("clicked", background="skyblue")
    tree_view.tag_configure("unclicked", background="white")

    # Attach Button
    show_button = tk.Button(root, text="Attach", command=show_clicked_files)
    show_button.pack(pady=10)

    # Detach Button
    detach_button = tk.Button(root, text="Detach", command=detach_files)
    detach_button.pack(pady=10)

    # Text Area
    text_widget = tk.Text(root, height=10)
    text_widget.pack(expand=True, fill='both', padx=10, pady=10)

    build_tree(tree_view, folder_structure)

    root.mainloop()
