import os
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import subprocess
from time import strftime
import threading

dataPath = 'D:\\LaSalle\\Computer architecture\\Project\\Data'
peopleList = os.listdir(dataPath)
print('List of users: ', peopleList)

def capture_faces(person_name):
    subprocess.run(["python", "D:\\LaSalle\\Computer architecture\\Project\\Code\\FaceCapture.py", person_name])
    training()

def training():
    subprocess.run(["python", "D:\\LaSalle\\Computer architecture\\Project\\Code\\TrainingRF.py"])

def delete_user():
    subprocess.run(["python", "D:\\LaSalle\\Computer architecture\\Project\\Code\\DeleteUser.py"])

def edit_user():
    subprocess.run(["python", "D:\\LaSalle\\Computer architecture\\Project\\Code\\EditUser.py"])

def facial_recognition():
    subprocess.run(["python", "D:\\LaSalle\\Computer architecture\\Project\\Code\\FacialRecognition.py"])

def people():
    dataPath = 'D:\\LaSalle\\Computer architecture\\Project\Data'
    peopleList = os.listdir(dataPath)
    print('List of users: ', peopleList)

def create_user():
    person_name = entry_name.get()
    person_id = entry_id.get()

    if person_name and person_id:
        capture_faces(person_name, person_id)
    else:
        show_message("Please enter a valid name and ID.")


def show_message(message):
    messagebox.showinfo("LaSalle College", message)


def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    window.after(1000, update_time)


def display_user_list():
    dataPath = 'D:\\LaSalle\\Computer architecture\\Project\Data'
    peopleList = os.listdir(dataPath)
    user_list = "\n".join(peopleList)
    show_message("User List:\n" + user_list)


def run_facial_recognition():
    while True:
        facial_recognition()

def start_facial_recognition():
    threading.Thread(target=run_facial_recognition, daemon=True).start()

window = tk.Tk()
window.attributes('-fullscreen', True)
window.title("LaSalle College")
window.configure(bg="black")

start_facial_recognition()

title_font = tkfont.Font(family="Arial", size=45, weight="bold")
button_font = tkfont.Font(family="Arial", size=25)
refresh_button_font = tkfont.Font(family="Arial", size=15)
note_font = tkfont.Font(family="Arial", size=12)

label = tk.Label(window, text="ATTENDANCE", fg="white", bg="black", font=title_font)
label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

entry_frame = tk.Frame(window, bg="black")
entry_frame.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

label_id = tk.Label(entry_frame, text="ID:", fg="white", bg="black", font=button_font)
label_id.grid(row=0, column=0, padx=5)

entry_id = tk.Entry(entry_frame, width=20, font=button_font, justify="center")
entry_id.grid(row=0, column=1, padx=5)

label_name = tk.Label(entry_frame, text="Name:", fg="white", bg="black", font=button_font)
label_name.grid(row=1, column=0, padx=5)

entry_name = tk.Entry(entry_frame, width=20, font=button_font, justify="center")
entry_name.grid(row=1, column=1, padx=5)

button_frame = tk.Frame(window, bg="black")
button_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button_refresh = tk.Frame(window, bg="black")
button_refresh.place(relx=0.9, rely=0.05, anchor=tk.CENTER)

button_list = tk.Frame(window, bg="black")
button_list.place(relx=0.9, rely=0.15, anchor=tk.CENTER)

create_user_button = tk.Button(
    button_frame,
    text="Create User",
    command=create_user,
    fg="white",
    bg="blue",
    width=10,
    font=button_font
)
delete_user_button = tk.Button(
    button_frame,
    text="Delete User",
    command=delete_user,
    fg="white",
    bg="red",
    width=10,
    font=button_font
)
edit_user_button = tk.Button(
    button_frame,
    text="Edit User",
    command=edit_user,
    fg="black",
    bg="yellow",
    width=10,
    font=button_font
)
refresh_button = tk.Button(
    button_refresh,
    text="Refresh",
    command=training,
    fg="black",
    bg="lightblue",
    width=10,
    font=refresh_button_font
)
button_user_list = tk.Button(
    button_list,
    text="User List",
    command=display_user_list,
    fg="black",
    bg="orange",
    width=10,
    font=refresh_button_font
)

create_user_button.pack(pady=10)
delete_user_button.pack(pady=10)
edit_user_button.pack(pady=10)
refresh_button.pack(pady=10)
button_user_list.pack(pady=10)

label = tk.Label(
    window,
    text="After Delete/Edit a user please click on Refresh",
    fg="white",
    bg="black",
    font=note_font
)
label.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

clock_label = tk.Label(window, text="", fg="white", bg="black", font=("Arial", 40))
clock_label.place(relx=0.02, rely=0.02)

update_time()

window.mainloop()