import os
import shutil
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

def edit_user(old_username, new_username):
    dataPath = 'D:\\LaSalle\\Computer architecture\\Project\\Data'
    old_personPath = os.path.join(dataPath, old_username)
    new_personPath = os.path.join(dataPath, new_username)

    if os.path.exists(old_personPath):
        if os.path.exists(new_personPath):
            messagebox.showinfo("User Already Exists", "User '{}' already exists.".format(new_username))
        else:
            try:
                os.rename(old_personPath, new_personPath)
                messagebox.showinfo("Rename Successful", "User '{}' renamed to '{}' successfully.".format(old_username, new_username))
            except OSError as e:
                messagebox.showerror("Rename Error", "Error renaming user '{}': {}".format(old_username, e))
    else:
        messagebox.showinfo("User Not Found", "User '{}' does not exist.".format(old_username))

def edit_user_gui():
    old_username = entry_old_username.get()
    new_username = entry_new_username.get()
    edit_user(old_username, new_username)

def return_to_gui():
    edit_window.destroy() 

edit_window = tk.Tk()
edit_window.attributes('-fullscreen', True)
edit_window.title("Edit User")
edit_window.configure(bg="black")

title_font = tkfont.Font(family="Arial", size=40, weight="bold")
button_font = tkfont.Font(family="Arial", size=25)

label_old_username = tk.Label(edit_window, text="Old Username:", fg="white", bg="black", font=title_font)
label_old_username.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

entry_old_username = tk.Entry(edit_window, width=20, font=button_font, justify="center")
entry_old_username.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

label_new_username = tk.Label(edit_window, text="New Username:", fg="white", bg="black", font=title_font)
label_new_username.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

entry_new_username = tk.Entry(edit_window, width=20, font=button_font, justify="center")
entry_new_username.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_edit_user = tk.Button(edit_window, text="Edit User", command=edit_user_gui, font=button_font, fg="black", bg="yellow")
button_edit_user.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button_return = tk.Button(edit_window, text="Return", command=return_to_gui, width=8, font=button_font)
button_return.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

edit_window.update_idletasks() 

window_width = edit_window.winfo_width()
window_height = edit_window.winfo_height()
center_x = int(edit_window.winfo_screenwidth() / 2 - window_width / 2)
center_y = int(edit_window.winfo_screenheight() / 2 - window_height / 2)

edit_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

edit_window.mainloop()
