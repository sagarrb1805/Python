from tkinter import*
import pyqrcode
from PIL import Image,ImageTk

root=Tk()

C1=Canvas(root,width=500,height=800)
C1.pack()
L1=Label(root,text='QR Code Generator',fg='black',font=('Times new Roman',18))
C1.create_window(200,60,window=L1)
Name_label=Label(root,text='specify the link')
link_label=Label(root,text="link")
C1.create_window(200,100,window=Name_label)
C1.create_window(200,160,window=link_label)
Name=Entry(root)
link=Entry(root)
link_name=Name.get()

link_entry=link.get()
print(link_name)
print(link_entry)
def generate():
    link_name=Name.get()
    link_entry=link.get()
    file_name=link_name+'.png'
    print(link_entry)
    url=pyqrcode.create(link_entry)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    imagelabel=Label(image=Image)
    imagelabel.image=image
    C1.create_window(200,230,window=imagelabel)

button=Button(text='Generate QR Code',command=generate)

C1.create_window(200,180,window=Name)
C1.create_window(200,130,window=link)
C1.create_window(200,230,window=button)
root.mainloop()