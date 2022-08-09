
from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
from pygame import mixer
import os

root=tk.Tk()
root.title("MP3 Music Player")
root.geometry("920x670+290+85")
root.configure(bg="black")
root.resizable(False,False)
root.iconbitmap(r'C:\Users\aa\aud player\mp3logo.ico')

mixer.init()
def opnfolder():
    fpath=filedialog.askdirectory()
    if fpath:
        os.chdir(fpath)
        songs=os.listdir(fpath)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                pylist.insert(END, song)

def mplay():
    mname=pylist.get(ACTIVE)
    mixer.music.load(pylist.get(ACTIVE))
    mixer.music.set_volume(0.7)
    print("Time Duration :",mixer.music.get_pos()/1000)
    mixer.music.play()
    music.config(text=mname[0:-4])
#for icons


ticon=PhotoImage(file=r"C:\Users\aa\aud player\logo2.png")
tlabel=Label(root,image=ticon,width=920,height=300,bg="white").pack()

#buttons
#play
playbtn=PhotoImage(file=r"C:\Users\aa\aud player\play.png")
Button(root,image=playbtn,command=mplay,bd=5,padx=5,pady=5).place(x=100,y=400)

#pause
pausebtn=PhotoImage(file=r"C:\Users\aa\aud player\pause.png")
Button(root,image=pausebtn,command=mixer.music.pause,bd=5,padx=5,pady=5,width=64,height=64).place(x=30,y=500)

#resume
resbtn=PhotoImage(file=r"C:\Users\aa\aud player\resume.png")
Button(root,image=resbtn,command=mixer.music.unpause,bd=5,padx=5,pady=5,width=64,height=64).place(x=115,y=500)

#stop
stopbtn=PhotoImage(file=r"C:\Users\aa\aud player\stop.png")
Button(root,image=stopbtn,command=mixer.music.stop, bd=5,padx=5,pady=5,width=64,height=64).place(x=200,y=500)

#mlabel
music=Label(root,text="",font=('Book Antiqua',12,"italic"),fg="white",bg="#0f1a2b")
music.place(x=185,y=330,anchor="center")
#menu
menu=PhotoImage(file=r"C:\Users\aa\aud player\menu.png")
Label(root,image=menu,bg="white",width=600,height=750).pack(padx=10,pady=50,side=RIGHT)

ms_frame=Frame(root,bd=2,relief=RIDGE)
ms_frame.place(x=345,y=400,width=550,height=200)

Button(root,text="Open Folder",command=opnfolder,bd=5,width=15,height=1,font=('Book Antiqua',10,"bold"),
       fg="white",bg="blue").place(x=325,y=360)
scr=Scrollbar(ms_frame)
pylist=Listbox(ms_frame,width=100,font=('Book Antiqua',12,"bold"),bg="#33333a",fg="grey"
               ,selectbackground="green",cursor="hand2",bd=2,yscrollcommand=scr.set)

scr.config(command=pylist.yview)

scr.pack(side=RIGHT,fill=Y)

pylist.pack(side=LEFT,fill=BOTH)






root.mainloop()
