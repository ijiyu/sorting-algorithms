import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Sorting Algorithms")
root.geometry("500x300")

n = tk.StringVar()
sorting_types = ["Bubble", "Insertion"]
sorting_type = ttk.Combobox(root, width=27, textvariable=n, values=sorting_types)
sorting_type.pack()

build = tk.Button(root, text="Build", width=10)
build.pack()

root.mainloop()