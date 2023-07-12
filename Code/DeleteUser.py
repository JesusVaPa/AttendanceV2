import os
import shutil
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

def delete_user(username):
    dataPath = 'D:\\LaSalle\\Computer architecture\\Project\\Data'
    personPath = os.path.join(dataPath, username)

    if os.path.exists(personPath):
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete user '{}'?".format(username))
        if confirm:
            try:
                shutil.rmtree(personPath)
                messagebox.showinfo("Deletion Successful", "User '{}' deleted successfully.".format(username))
            except OSError as e:
                messagebox.showerror("Deletion Error", "Error deleting user '{}': {}".format(username, e))
        else:
            messagebox.showinfo("Deletion Canceled", "Deletion of user '{}' canceled.".format(username))
    else:
        messagebox.showinfo("User Not Found", "User '{}' does not exist.".format(username))

def delete_user_gui():
    username = entry_username.get()
    delete_user(username)

def return_to_gui():
    delete_window.destroy()  

delete_window = tk.Tk()
delete_window.attributes('-fullscreen', True)
delete_window.title("Delete User")
delete_window.configure(bg="black")

title_font = tkfont.Font(family="Arial", size=40, weight="bold")
button_font = tkfont.Font(family="Arial", size=25)

label = tk.Label(delete_window, text="Enter the username to delete:", fg="white", bg="black", font=title_font)
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

entry_username = tk.Entry(delete_window, width=20, font=button_font, justify="center")
entry_username.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_delete_user = tk.Button(delete_window, text="Delete User", command=delete_user_gui, width=10, font=button_font, fg="white", bg="red")
button_delete_user.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button_return = tk.Button(delete_window, text="Return", command=return_to_gui, width=8, font=button_font)
button_return.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

delete_window.mainloop()
