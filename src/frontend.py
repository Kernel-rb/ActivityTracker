from tkinter import *
from tkcalendar import Calendar
import backend 

def get_selected_row() :
    pass

# we define the functions that will be called when the buttons are clicked
def view_cmd():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)
# search function
def search_cmd():
    listbox.delete(0, END)
    for row in backend.search(date_text.get(), study_text.get(), project_text.get(), github_repos_text.get(), roadmap_text.get(), notes_text.get()):
        listbox.insert(END, row)
# add function
def  add_cmd():
    backend.insert(date_text.get(), study_text.get(), project_text.get(), github_repos_text.get(), roadmap_text.get(), notes_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (date_text.get(), study_text.get(), project_text.get(), github_repos_text.get(), roadmap_text.get(), notes_text.get())) 

def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END, selected_tuple[6])

def delete_cmd():
    global selected_tuple
    backend.delete(selected_tuple[0])



# we define an object of the Tk class
app = Tk()
app.title("Activity Tracker Database")

# we create all the labels

l1 = Label(app, text="Date")
l1.grid(row=0, column=0)

l2 = Label(app, text="Study")
l2.grid(row=0, column=2)

l3 = Label(app, text="Project")
l3.grid(row=1, column=0)

l4 = Label(app, text="Github repos")
l4.grid(row=1, column=2)

l5 = Label(app, text="Roadmap")
l5.grid(row=2, column=0)

l6 = Label(app, text="Notes")
l6.grid(row=2, column=2)

# we create all the entries

date_text = StringVar()
e1 = Entry(app, textvariable=date_text)
e1.grid(row=0, column=1)

study_text = StringVar()
e2 = Entry(app, textvariable=study_text)
e2.grid(row=0, column=3)

project_text = StringVar()
e3 = Entry(app, textvariable=project_text)
e3.grid(row=1, column=1)

github_repos_text = StringVar()
e4 = Entry(app, textvariable=github_repos_text)
e4.grid(row=1, column=3)

roadmap_text = StringVar()
e5 = Entry(app, textvariable=roadmap_text)
e5.grid(row=2, column=1)

notes_text = StringVar()
e6 = Entry(app, textvariable=notes_text)
e6.grid(row=2, column=3)

# we create a listbox
listbox = Listbox(app, height=8, width=35)
listbox.grid(row=3, column=0, rowspan=9, columnspan=2, sticky="nsew")

# we create a scrollbar
sb = Scrollbar(app)
sb.grid(row=3, column=2, rowspan=9)

# we configure the listbox to use the scrollbar
listbox.bind('<<ListboxSelect>>', get_selected_row)


# we create all the buttons
# Define colors for the buttons
button_colors = {
    "Add": {"bg": "green", "fg": "white"},
    "Search": {"bg": "blue", "fg": "white"},
    "Delete": {"bg": "red", "fg": "white"},
    "View All": {"bg": "purple", "fg": "white"},
    "Close": {"bg": "gray", "fg": "white"}
}

# Create and configure the buttons with the specified colors
b1 = Button(app, text="Add", width=12, pady=5, bg=button_colors["Add"]["bg"], fg=button_colors["Add"]["fg"] , command=add_cmd)
b1.grid(row=3, column=3)

b2 = Button(app, text="Search", width=12, pady=5, bg=button_colors["Search"]["bg"], fg=button_colors["Search"]["fg"] , command=search_cmd)
b2.grid(row=4, column=3)

b3 = Button(app, text="Delete", width=12, pady=5, bg=button_colors["Delete"]["bg"], fg=button_colors["Delete"]["fg"] , command=delete_cmd)
b3.grid(row=5, column=3)

b4 = Button(app, text="View All", width=12, pady=5, bg=button_colors["View All"]["bg"], fg=button_colors["View All"]["fg"] , command=view_cmd)
b4.grid(row=6, column=3)

b5 = Button(app, text="Close", width=12, pady=5, bg=button_colors["Close"]["bg"], fg=button_colors["Close"]["fg"], command=app.destroy)
b5.grid(row=7, column=3)



 
app.mainloop()