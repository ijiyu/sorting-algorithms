import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Sorting Algorithms")

frame = tk.Frame(root)
frame.pack()

sorting_type_frame = tk.LabelFrame(frame, text="Sorting Algorithm")
sorting_type_frame.grid(row=0, column=0, padx=20, pady=10)

sorting_label = tk.Label(sorting_type_frame, text="Type")
sorting_combobox = ttk.Combobox(sorting_type_frame, values=["Bubble", "Insertion"])
sorting_label.grid(row=0, column=0, padx=5, pady=5)
sorting_combobox.grid(row=0, column=1, padx=5)



root.mainloop()