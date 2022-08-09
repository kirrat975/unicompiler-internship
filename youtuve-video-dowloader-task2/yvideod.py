import tkinter as tk
from tkinter import *
from pytube import YouTube

from tkinter import filedialog,messagebox

def Widgets():
    
    hLabel=Label(root,text="Youtube Video Downloader",bg="black",fg="white",borderwidth=10,relief=RAISED,
                 font=('Book Antiqua', 30))
    hLabel.grid(row=0,column=1,padx=20,pady=20)
    

    linkLabel=Label(root,text="Enter Youtube URL:",bg="white",borderwidth=5)
    linkLabel.grid(row=1,column=0,padx=10,pady=10)
    root.linktxt=Entry(root,width=60,textvariable=videoLink,borderwidth=5)
    root.linktxt.grid(row=1,column=1,padx=10,pady=10)
    destLabel=Label(root,text="Download Folder",bg="white",borderwidth=5)
    destLabel.grid(row=2,column=0,padx=10,pady=10)
    root.desttxt=Entry(root,width=60,textvariable=dlPath,borderwidth=5)
    root.desttxt.grid(row=2,column=1,padx=3,pady=3)
    BrBtn=Button(root,text="Browse", command=browselink ,width=10,bg="lightpink",borderwidth=8)
    BrBtn.grid(row=2,column=2,padx=1,pady=1)
    DlBtn=Button(root,text="Download  Youtube Video Link",command=dvidlink,width=25,bg="limegreen",
                 borderwidth=8)
    DlBtn.grid(row=3,column=1,padx=3,pady=3)

def browselink():
    dl_dir=filedialog.askdirectory(initialdir=r"C:\Users\aa\Downloads",title="Save Video")
    dlPath.set(dl_dir)
def dvidlink():
    url=videoLink.get()
    folder = dlPath.get()
    getvid = YouTube(url)
    print("Title of Video:",getvid.title)
    print("Length of Video:",getvid.length)
    print(getvid.streams.filter(only_video=True))
    print("\n")
    print(getvid.streams.filter(progressive=True))
    getstream = getvid.streams.get_highest_resolution()
    getstream.download(folder)
    messagebox.showinfo("Success","Youtube Video Downloaded succssfully  at \n" + folder)





root=tk.Tk();
root.geometry("850x300")
root.resizable(True,True)
root.title("Youtube Video Downloader")
root.config(background="red")
videoLink=StringVar()
dlPath=StringVar()
Widgets()
root.mainloop()
