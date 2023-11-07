from owlready2 import *
from tkinter import *
from functools import partial
owlready2.JAVA_EXE = "C:\\Users\\klesh\\.jdks\\openjdk-21\\bin\\java.exe"


def color_config(widget, color, event):
    widget.configure(foreground=color)

root = Tk()
root.geometry("800x600")  # Increased width for more space
frm = root

title = Frame(frm)
title.pack(padx=20, pady=20)

text = Label(title, text="University Circus", font=("Helvetica", 24))  # Increase font size
text.pack()

bod = Frame(frm, width=800, highlightbackground="black", highlightthickness=1)
bod.pack(padx=20, pady=20, fill="both", expand=True)

# Center the subjects, books, and students frames
center_frame = Frame(bod)
center_frame.pack(fill="both", expand=True)
center_frame.columnconfigure(0, weight=1)  # Make the frame expand horizontally

subjects = Frame(center_frame)
subjects.pack(anchor="nw", padx=5, pady=10)
labs = Frame(center_frame)
labs.pack(anchor="nw", padx=5, pady=10)
students = Frame(center_frame)
students.pack(anchor="nw", padx=5, pady=10)

onto = get_ontology("./onto.owl").load()
library = onto.get_namespace("http://test.org/onto.owl")

sync_reasoner()

info = Frame(center_frame)
info.pack(fill="both", expand=True)

# Function to set the font and align text to center
def set_font_and_align(label, size, align="center"):
    label.configure(font=("Helvetica", size), anchor=align)

def show(lab):
    pop_up = Toplevel(root)
    pop_up.title("Information")

    # Set the size of the pop-up window
    pop_up.geometry("600x400")  # Adjust the width and height as needed

    # Center the pop-up window on the screen
    window_width = pop_up.winfo_reqwidth()
    window_height = pop_up.winfo_reqheight()
    position_right = int(pop_up.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(pop_up.winfo_screenheight() / 2 - window_height / 2)
    pop_up.geometry("+{}+{}".format(position_right, position_down))

    info_frame = Frame(pop_up, padx=20, pady=10)
    info_frame.pack()

    info_text = []

    # info_text.append(f"{lab.name}")

    for c in lab.is_a:
        try:
            info_text.append(f"{c.label[0]}: {lab.name}")
        except:
            pass

    Label(info_frame, text=" | ".join(info_text), font=("Helvetica", 14)).pack(anchor="nw")

    for prop in lab.get_properties():
        label_text = f"{prop.label[0]}:"
        values = [value.name for value in prop[lab]]
        values_text = "\n".join(f"- {value}" for value in values)
        Label(info_frame, text=f"{label_text}\n{values_text}", padx=10, font=("Helvetica", 12)).pack(anchor="nw")

    # Close button to close the pop-up window
    close_button = Button(pop_up, text="Close", command=pop_up.destroy)
    close_button.pack()

text1 = Label(labs, text="Лаби:", font=("Helvetica", 20))
text1.pack(anchor="nw")

for lab in library.LabWork.instances():
    text = Label(labs, text=lab.name, font=("Helvetica", 16), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "green"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, book=lab:show(book))

text2 = Label(students, text="Роботяги-студенти:", font=("Helvetica", 20))
text2.pack(anchor="nw")

for lab in library.Student.instances():
    text = Label(students, text=lab.name, font=("Helvetica", 16), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "green"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, book=lab:show(book))

text3 = Label(subjects, text="Предмети:", font=("Helvetica", 20))
text3.pack(anchor="nw")

for subject in library.Subject.instances():
    text = Label(subjects, text=subject.name, font=("Helvetica", 16), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "green"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, book=subject:show(book))


root.mainloop()




