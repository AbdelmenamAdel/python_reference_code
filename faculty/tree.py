from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
root=Tk()
def insert_table():
    pass
columns=('1','2','3','4')
headers=("name","age","job","pay")
tree=ttk.Treeview(root,columns=columns,show="headings",selectmode="browse")
for col,head in zip(columns,headers):
    tree.heading(col,text=head)
    tree.column(col,anchor="center")
scrollbartree=ttk.Scrollbar(root,orient="vertical",command=tree.yview)
tree.configure(yscrollcommand=scrollbartree.set)
tree.place(x=0,y=0,height=500)
btn=Button(root,text="insert",command=tree.insert)
root.mainloop()