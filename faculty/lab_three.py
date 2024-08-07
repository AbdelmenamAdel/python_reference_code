from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
from PIL import Image,ImageTk
from fontTools.ttLib import TTFont
import time
# font=TTFont("assets/Poppins-Regular.ttf")
root=Tk()
root_width=500
root_height=400
screen_height=root.winfo_screenwidth()
screen_width=root.winfo_screenheight()

def close():
    root.destroy()
def window_hide():
    root.withdraw()
    time.sleep(3)
    root.deiconify()
# def button_image():
#     # photo= PhotoImage(file="assets/image.png")
#     p_image=photo.subsample(2,10) 
#     return p_image
# x_base=int(screen_width)-root_width-150
# y_base = int(screen_height)-root_height-150
# root.iconbitmap("assets/image.ico")
def get_Entry():
    nameE = name.get()
    passwordE = password.get()
    if nameE == "abdo" and passwordE == "1234":
        print("Login successful!")
        messagebox.showinfo("Success", "Login successful!, "+"Welcome "+name.get())
    else:
        print("Invalid username or password")
        messagebox.showerror("Error", "Invalid username or password")
    return
root.config(bg="#e0e0e0") 
root.geometry(f"{root_width}x{root_height}")
root.resizable(False,False)
root.title("Login Screen")
root_frame=Frame(root,bg="#e0e0e0",padx=10,pady=10)
root_frame.place(relx=0.5,rely=0.5,anchor="center")
lbl = Label(root_frame, text="User Name : ", bg="#e0e0e0", font=("Poppins", 14, "bold"))
lbl.grid(row=0, column=0,padx=10,pady=10)

lbl2 = Label(root_frame, text="Password : ", bg="#e0e0e0", font=("Arial", 14, "bold"))
lbl2.grid(row=1, column=0,padx=10,pady=10)
name=StringVar()
txt = Entry(root_frame,textvariable=name,selectbackground="orange",selectforeground="blue",state=NORMAL)
txt.grid(row=0, column=1,padx=10,pady=10)
password=StringVar()
txt2 = Entry(root_frame,show="*",textvariable=password,selectbackground="orange",selectforeground="blue",state=NORMAL)
txt2.grid(row=1, column=1,padx=10,pady=10)
# photo=button_image()

btn=Button(root_frame,text="Login",font=("Poppins", 14, "bold"),bg="#3498DB",fg="#ffffff",width=10,command=get_Entry)
btn.grid(row=2,columnspan=2,padx=10,pady=10)

mainloop()