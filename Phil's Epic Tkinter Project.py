#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry('850x400')
root.title('Tkinter Project')

def openFile():
    root.filename = askopenfilename(initialdir='images', title='Select a File')

def save():
    Files = [('All Files', '*.*'),
        ('Python Files', '*.py'),
        ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = Files, defaultextension = Files)
    
def cut():
    global clipboard
    clipboard = textBox.selection_get()
    
def paste():
    global clipboard
    textBox.insert(END, str(clipboard))
    
def copy():
    global clipboard
    clipboard = textBox.selection_get()
    
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=save)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Cut Ctrl+x", command=cut)
editmenu.add_command(label="Copy Ctrl+c", command=copy)
editmenu.add_command(label="Paste Ctrl+v", command=paste)

menubar.add_cascade(label="Edit", menu=editmenu)

#add image function
def add_image():
    textBox.image_create(END, image = myImg)

#text box
textBox = Text(root, width=45, height=20, selectbackground='yellow', selectforeground='black', font='Helvetica')
textBox.grid(row=0, column=3, rowspan=20, padx=5, pady=5, stick=W+E)
textBox.insert(END, 'You can use this box to see if your cut, copy, and paste     menu items work.')
myImg = ImageTk.PhotoImage(Image.open('nycpic1.jpg'))
textBox.insert(END, '\n\nWrite your message here!\n\n')
textBox.image_create(END, image = myImg)
imgBtn = Button(root, text='Add Image', command=add_image)
imgBtn.grid(row=18, column=3, padx=8, stick=W)
exitBtn = Button(root, text='Exit', command=root.destroy)
exitBtn.grid(row=19, column=3, padx=8, stick=W)

#scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL) 
scrollbar.grid(row=0, column=2, stick=N+S, rowspan=20)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=scrollbar.set) 
scrollbar['command'] = canvas.yview 

#list box
states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
listBox = Listbox(root, listvariable=states, height=20, yscrollcommand = scrollbar.set)
listBox.grid(row=0, column=0, padx=5, pady=5, stick=N, rowspan=20)
index = 0
for i in states:
    listBox.insert(index, i)
    index = index+1
listBox.selectedindex = 0

#configure alternating colors in listbox
i = 1
while i < listBox.size():
    listBox.itemconfig(i,{'bg':'#E6E6FA'})
    i = i + 2

    
#present selections
presentDescription = Label(root, text="Select a present to send to this state's capital!", fg='white', bg='black')
presentDescription.grid(row=0, column=1, padx=5, pady=5, stick=N)
present = StringVar()
present.set('Five Crates of Chocolate')
radioBtn1 = Radiobutton(root, text='Five Crates of Chocolate', variable=present, value='Five Crates of Chocolate')
radioBtn1.grid(row=1, column=1, stick=W)
radioBtn2 = Radiobutton(root, text='Ten Pounds of Ice Cream', variable=present, value='Ten Pounds of Ice Cream')
radioBtn2.grid(row=2, column=1, stick=W)
radioBtn3 = Radiobutton(root, text='A Giant Fruit Basket', variable=present, value='A Giant Fruit Basket')
radioBtn3.grid(row=3, column=1, stick=W)

#press to send button and function
def send(present):
    sentLabel = Label(root, text='')
    sentLabel.grid(row=5, column=1)
    sentLabel = Label(root, text='Great choice! This item\nwill be shipped immediately.\n' + str(present) + ' will be sent\nto the state of ' + str(listBox.get(ACTIVE)) + '.')
    sentLabel.grid(row=5, column=1)

sendBtn = Button(root, text='Press to Send', command=lambda: send(present.get()))
sendBtn.grid(row=4, column=1, padx=5, stick=E)

scrollbar.config( command = listBox.yview)
root.config(menu=menubar)
mainloop()

