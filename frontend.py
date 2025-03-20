from tkinter import *
import backend  # Importing the backend file

def view_cmd():
    """Retrieve and display data in the listbox."""
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)

def add_cmd():
    """Insert user input into the database."""
    back.insert(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get())
    view_cmd()

def delete_cmd():
    """Delete selected entry from the database."""
    try:
        selected_item = list1.curselection()[0]
        data = list1.get(selected_item)
        back.delete(data[0])  # ID is the first element of tuple
        view_cmd()
    except IndexError:
        list1.insert(END, "Select an entry to delete.")

# Create the GUI window
win = Tk()
win.title("Daily Routine Tracker")
win.geometry("600x400")
win.configure(bg="#F3F4F6")

# Labels
labels_texts = ["Date", "Earnings", "Exercise", "Study", "Diet", "Expenses"]
positions = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]
for text, pos in zip(labels_texts, positions):
    Label(win, text=text, bg="violet", fg="white", font="Lato 12", borderwidth=2, relief="groove",
          padx=4, pady=4).grid(row=pos[0], column=pos[1], sticky="nsew")

# Entry Fields
date_text = StringVar()
earning_text = StringVar()
exercise_text = StringVar()
study_text = StringVar()
diet_text = StringVar()
expense_text = StringVar()

entries_positions = [(0, 1, date_text), (0, 3, earning_text), (1, 1, exercise_text),
                     (1, 3, study_text), (2, 1, diet_text), (2, 3, expense_text)]

entries = []
for pos in entries_positions:
    entry = Entry(win, textvariable=pos[2])
    entry.grid(row=pos[0], column=pos[1])
    entries.append(entry)

# Listbox with Scrollbar
list1 = Listbox(win, height=10, width=40)
list1.grid(row=3, column=0, rowspan=6, columnspan=2, sticky="nsew")

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=6, sticky="ns")
list1.config(yscrollcommand=sb.set)
sb.config(command=list1.yview)

# Buttons
Button(win, text="Add", width=12, pady=5, bg="violet", fg="white", font="Lato 12", borderwidth=2,
       relief="groove", padx=4, command=add_cmd).grid(row=3, column=3)

Button(win, text="Search", width=12, pady=5, bg="violet", fg="white", font="Lato 12", borderwidth=2,
       relief="groove", padx=4).grid(row=4, column=3)

Button(win, text="Delete", width=12, pady=5, bg="violet", fg="white", font="Lato 12", borderwidth=2,
       relief="groove", padx=4, command=delete_cmd).grid(row=5, column=3)

Button(win, text="View All", width=12, pady=5, bg="violet", fg="white", font="Lato 12", borderwidth=2,
       relief="groove", padx=4, command=view_cmd).grid(row=6, column=3)

Button(win, text="Close", width=12, pady=5, bg="violet", fg="white", font="Lato 12", borderwidth=2,
       relief="groove", padx=4, command=win.destroy).grid(row=7, column=3)

# Run the GUI
win.mainloop()
