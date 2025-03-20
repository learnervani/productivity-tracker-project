import tkinter as tk
from tkinter import ttk, PhotoImage
import back  # Importing the backend file

selected_row = []

def select_row(event):
    global selected_row
    try:
        index = list1.curselection()[0]
        selected_row = list1.get(index)
    except IndexError:
        selected_row = []

def delete_cmd():
    global selected_row
    if selected_row:
        back.delete(selected_row[0])
        selected_row = []
        view_cmd()
        status_label.config(text="Entry Deleted Successfully!", fg="red")
    else:
        status_label.config(text="No row selected!", fg="red")

def view_cmd():
    list1.delete(0, tk.END)
    for row in back.view():
        list1.insert(tk.END, row)

def search_cmd():
    list1.delete(0, tk.END)
    for row in back.search(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get()):
        list1.insert(tk.END, row)

def add_cmd():
    back.insert(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get())
    list1.insert(tk.END, (date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get()))
    status_label.config(text="Entry Added Successfully!", fg="green")

# Create Main Window
win = tk.Tk()
win.title("Daily Routine Tracker")
win.geometry("900x600")
win.configure(bg="#FCC6FF")  # Soft pink background

# Fonts and Styles
label_style = {"bg": "#FCC6FF", "fg": "#5A189A", "font": ("Comic Sans MS", 12, "bold")}
entry_bg = "#FFE6C9"
entry_font = ("Comic Sans MS", 11)
button_bg = "#FFC785"
button_hover_bg = "#FFAD60"

# Labels and Entry Fields
labels = ["Date", "Earnings", "Exercise", "Study", "Diet", "Expenses"]
date_text, earning_text, exercise_text, study_text, diet_text, expense_text = (tk.StringVar() for _ in range(6))
entries = [date_text, earning_text, exercise_text, study_text, diet_text, expense_text]

for i, text in enumerate(labels):
    tk.Label(win, text=text, **label_style).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(win, textvariable=entries[i], font=entry_font, bg=entry_bg, width=30, bd=3, relief="groove").grid(row=i, column=1, padx=10, pady=5)

# Listbox with Scrollbar
frame = tk.Frame(win, bg="#FCC6FF")
frame.grid(row=6, column=0, columnspan=2, pady=10)

list1 = tk.Listbox(frame, height=8, width=60, bg="#FFE6C9", fg="#5A189A", font=("Comic Sans MS", 11), bd=3, relief="ridge")
list1.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = ttk.Scrollbar(frame, command=list1.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
list1.config(yscrollcommand=scrollbar.set)
list1.bind("<<ListboxSelect>>", select_row)

# Button Styles
button_style = {
    "font": ("Comic Sans MS", 11, "bold"),
    "fg": "#5A189A",
    "bg": button_bg,
    "activebackground": button_hover_bg,
    "bd": 3,
    "relief": "ridge",
    "width": 12,
    "pady": 5
}

def on_enter(e):
    e.widget["background"] = button_hover_bg

def on_leave(e):
    e.widget["background"] = button_bg

# Buttons without icons
buttons = [
    ("Add", add_cmd),
    ("Search", search_cmd),
    ("Delete", delete_cmd),
    ("View", view_cmd),
    ("Close", win.destroy)
]

# Adjust button alignment by centering them
button_frame = tk.Frame(win, bg="#FCC6FF")  # Create a frame for buttons
button_frame.grid(row=5, column=0, columnspan=2, pady=10)  # Center the frame

for i, (text, cmd) in enumerate(buttons):
    btn = tk.Button(
        button_frame,  # Place buttons inside the frame
        text=text,
        command=cmd,
        **button_style
    )
    btn.grid(row=0, column=i, padx=10, pady=5)  # Align buttons in a single row
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Status Label
status_label = tk.Label(win, text="", bg="#FCC6FF", fg="#5A189A", font=("Comic Sans MS", 11, "italic"))
status_label.grid(row=8, column=0, columnspan=4, pady=5)

win.mainloop()
