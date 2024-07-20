from tkinter import Tk, Label, Entry, Button,messagebox,Frame
# ! constants
padx=20
pady=20
def login_attempt():
  username = username_entry.get()
  password = password_entry.get()
  # ! Replace this with your login validation logic (checking a database)
  if username == "admin" and password == "1234":
    print("Login successful!")
    messagebox.showinfo("Success", "Login successful!")
  else:
    print("Invalid username or password")
    messagebox.showerror("Error", "Invalid username or password")
    
# ! Create the Root screen 
root = Tk()

# ! Create the Root screen frame
root_frame = Frame(root, bg="#e0e0e0", padx=padx, pady=pady)
root_frame.place(relx=0.5, rely=0.5,anchor='center')

# ! Set title and screen size
root.title("Login Screen")
root.geometry("450x250")
root.resizable(False, False)

# ! Set background color
root.configure(bg="#e0e0e0")  # Light gray background

# ! Style labels
username_label = Label(root_frame, text="Username:", font=("Arial", 12, "bold"), fg="#333333")  # Black text
username_label.grid(row=0, column=0, pady=pady, padx=padx)  # Add padding

password_label = Label(root_frame, text="Password:", font=("Arial", 12, "bold"), fg="#333333")
password_label.grid(row=1, column=0, pady=pady, padx=padx)

# ! Style entry fields
username_entry = Entry(root_frame, font=("Arial", 12), bg="#ffffff", fg="#333333")  # White background, black text
username_entry.grid(row=0, column=1, pady=pady, padx=padx)

password_entry = Entry(root_frame, font=("Arial", 12), show="*", bg="#ffffff", fg="#333333")
password_entry.grid(row=1, column=1, pady=pady, padx=padx)

# ! Style button
login_button = Button(root_frame, text="Login", command=login_attempt, font=("Arial", 12, "bold"), bg="#3498DB", fg="#ffffff",width=10)  # Green button, white text
login_button.grid(row=2, columnspan=2, pady=10, padx=10)

root.mainloop()
