from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import object_detection as od
import imageio
import cv2
class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
    def init_window(self):
        self.master.title("Traffic Signal Detection System")
        self.pack(fill=BOTH,expand=1)
        self.line=[]
        self.rect=[]
        self.pos=[]
        self.counter=0
        menu =Menu(self.master)
        self.master.config(menu=menu)
        filemenu=Menu(menu)
        filemenu.add_command(label="Open",command=self.open)
        filemenu.add_command(label="Exit",command=self.exit)   
        filemenu.add_cascade(label="File",menu=filemenu)
        analyze=Menu(menu)
        analyze.add_command(label="Region Of Interest",command=self.regionOfInterest)
        menu.add_cascade(label="Analyze",menu=analyze)
        self.filename="assets/image.png"  
        self.imgsize=Image.open(self.filename)
        self.tkimage=ImageTk.PhotoImage(self.imgsize)
        self.w,self.h=self.tkimage.width(),self.tkimage.height()
        self.canvas=Canvas(self,width=self.w,height=self.h)    
        self.canvas.pack()
    def open_file(self):
        self.filename=filedialog.askopenfilename()
        cap=cv2.videoCapture(self.filename)
        reader=imageio.get_reader(self.filename)   
        fps=reader.get_meta_data()['fps']
        ret,image=cap.read()
        cv2.imwrite("assets/image.png",image)
        self.show_image("assets/image.png")
    def show_image(self,frame):
        self.imgsize=Image.open(frame)
        self.tkimage=ImageTk.PhotoImage(self.imgsize)
        self.w,self.h=self.tkimage.width(),self.tkimage.height()
        self.canvas.destroy()
        self.canvas=Canvas(self,width=self.w,height=self.h)
        self.canvas.create_image(0,0,anchor="nw",image=self.tkimage)
        self.canvas.pack()
    def regionOfInterest(self):
        self.master.config(cursor="plus")
        self.canvas.bind("<ButtonPre-1>",self.on_button_press)
    def client_exit(self):
        exit()

object=Window(Tk())
object.mainloop()

# w=root.winfo_screenwidth()
# h=str(root.winfo_screenheight())