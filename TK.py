from Tkinter import *
from tkFileDialog import askopenfilename
from Image1 import start1,end1
from ImageTk import PhotoImage
from PIL import Image

global dest

def start():
    start1(filename,input_text)

def end():
    global dest
    dest = end1()


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Steganography")
        self.root.grid()
        self.create_widgets()

    def create_widgets(self):
        global button,text
        button = Button(self.root, text = "Upload Your Image")
        button["command"] = self.upload_image
        button.pack()
        label = Label(self.root, text = "Enter Msg to be Hidden" , fg="red", font=("Arial", 10))
        label.pack()
        text = Text(self.root)
        text.pack()
        self.root.mainloop()

    def retrieve(self):
        global input_text
        input_text = text.get('1.0','end-1c')

    def upload_image(self):
        global filename,dest
        self.retrieve()
        filename = askopenfilename()
        start()
        end()
        button.destroy()
        self.root.destroy()
        self.another()


    def another(self):
        root = Tk()
        img = PhotoImage(Image.open(dest))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        label = Label(root, text = "This is Your Image" , fg="red",  font=("Arial", 10))
        label.pack()
        label1 = Label(root, text = "Path = "+dest , fg="red",  font=("Arial", 10))
        label1.pack()
        root.mainloop()
        
       
def initiate():
    app = App()


