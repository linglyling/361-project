from tkinter import *
import os.path
import csv

root = Tk()



if (os.path.isfile("database.txt") == False):
    with open("database.txt", "w") as dbfile:
        dbfile.write("Title,Status,Watched,My Score,Notes\n")

def display_data():
    with open("database.txt") as display_file:
        file_reader = csv.reader(display_file)
        curr_row = 1
        curr_col = 1
        skip = True
        for row in file_reader:
            if (skip == TRUE):
                skip = False
                continue
            for i in row:
                main_label = Label(root, text=i).grid(row=curr_row, column=curr_col)
                curr_col+=1
            curr_col=1
            curr_row+=1


title = Label(root, text="Title")

display_data()
title.grid(row=0, column=1, padx=60)
status = Label(root, text="Status")
status.grid(row=0, column=2)
watched = Label(root, text="Watched")
watched.grid(row=0, column=3)
my_score = Label(root, text="My Score")
my_score.grid(row=0, column=4)
#notes/more?
notes = Label(root, text="Notes", padx=50)
notes.grid(row=0, column=5)


sort = Button(root, text="Sort", width=15)
sort.grid(row=0, column=6)

#add entry
def add_entry(title=""):
    #don't need to loop toplvl window for some reason
    add_window = Toplevel()
    add_window.title("Add New")
    add_title = Label(add_window, text="Title:")
    add_title.grid(row=0, column=1)
    add_status = Label(add_window, text="Status:")
    add_status.grid(row=1, column=1)
    add_watched = Label(add_window, text="Watched:")
    add_watched.grid(row=2, column=1)
    add_score = Label(add_window, text="My Score:")
    add_score.grid(row=3, column=1)
    add_notes = Label(add_window, text="Notes:")
    add_notes.grid(row=4, column=1)
    title_entry = Entry(add_window)
    title_entry.grid(row=0, column=2)
    title_entry.insert(0, title)

    status_entry = Entry(add_window)
    status_entry.grid(row=1, column=2)
    watched_entry = Entry(add_window)
    watched_entry.grid(row=2, column=2)
    score_entry = Entry(add_window)
    score_entry.grid(row=3, column=2)
    notes_entry = Entry(add_window)
    notes_entry.grid(row=4, column=2)

    def add_submit():
        with open("database.txt", "a") as addfile:
            addfile.write(title_entry.get() + "," + status_entry.get() + "," + watched_entry.get() + "," + score_entry.get() + "," + notes_entry.get() + "\n")
        display_data()
        add_window.destroy()

    add_submit = Button(add_window, text="Submit", width=15, command=add_submit)#need command
    add_submit.grid(row=0, column=3)
    add_delete = Button(add_window, text="Delete", width=15)
    add_delete.grid(row=1, column=3)
    add_import = Button(add_window, text="Import IMDb Info", width=15)
    add_import.grid(row=2, column=3)
    add_cancel = Button(add_window, text="Cancel", width=15, command=add_window.destroy)
    add_cancel.grid(row=3, column=3)



add = Button(root, text="Add New", width=15, command=add_entry)
add.grid(row=1, column=6)

def edit_entry():
    edit_window = Toplevel()
    title = Label(edit_window, text="Enter title:")
    title.grid(row=0, column=0)
    title_entry = Entry(edit_window)
    title_entry.grid(row=0, column=1)

    def edit_submit():
        with open("database.txt", "r") as f:
            lines = f.readlines()
        with open("database.txt", "w") as f:
            for line in lines:
                x = line[0:len(title_entry.get()) + 1]
                if line[0:len(title_entry.get()) + 1] != (title_entry.get() + ","):
                    f.write(line)
        add_entry(title_entry.get())
        edit_window.destroy()

    submit = Button(edit_window, text="Submit", command=edit_submit)
    submit.grid(row=0, column=2)


edit = Button(root, text="Edit Existing", width=15, command=edit_entry)
edit.grid(row=2, column=6)
delete = Button(root, text="Delete Entry", width=15)
delete.grid(row=3, column=6)
imdb = Button(root, text="Update with IMDb", width=15)
imdb.grid(row=4, column=6)
import1 = Button(root, text="Import", width=15)
import1.grid(row=5, column=6)


def export():
    with open('database.txt', 'r') as firstfile, open('export.txt', 'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    os.startfile("export.txt")

export1 = Button(root, text="Export", width=15, command=export)
export1.grid(row=6, column=6)
faqs = Button(root, text="FAQS", width=15)
faqs.grid(row=7, column=6)
help = Button(root, text="Help", width=15)
help.grid(row=8, column=6)


root.title("My Media List")
root.mainloop()

with open('database.txt', 'r') as fileoo:
    onion = fileoo.read()
print(onion)