from pytube import YouTube
from tkinter import *
from tkinter import messagebox, filedialog

#region UI
window=Tk()
window.configure(bg='yellow green')
window.iconbitmap('icons/5.ico')


#region geometry
window.geometry('510x360')
window.resizable(0,0)
window.title('Youtube Downloader')
positionright=int(window.winfo_screenwidth()/2-290/2)
positiondown=int(window.winfo_screenheight()/2-420/2)
window.geometry('+{}+{}'.format(positionright,positiondown))
#endregion


#region label entry
txtlink=StringVar()
Label(window,text='Youtube Downloader',font='times 18 italic',bg='yellow green').grid(row=0,column=1)
lbllink=Label(window,text="please enter your video's link:",font='arial 10 bold  ',highlightthickness=1,bg='yellow green',activebackground='yellow green',highlightbackground='yellow green').grid(row=1,column=1,pady='10')
entlink=Entry(window,width='65',font='arial 10 ',highlightthickness=1,textvariable=txtlink).grid(row=2,column=1,pady='5',padx='30',sticky='e')

txtsave=StringVar()
lblsave=Label(window,text="choose direction:",font='arial 10 bold ',highlightthickness=1,bg='yellow green',activebackground='yellow green',highlightbackground='yellow green').grid(row=5,column=1,pady='10')
entsave=Entry(window,width='52',font='arial 10 ',highlightthickness=1,textvariable=txtsave).grid(row=6,column=1,pady='5',padx='30',sticky='w')

txtname=StringVar()
lblname=Label(window,text="Change Your Video's Name (optional) :",font='arial 10 bold  ',highlightthickness=1,bg='yellow green',activebackground='yellow green',highlightbackground='yellow green').grid(row=3,column=1,pady='10')
entname=Entry(window,width='65',font='arial 10 ',highlightthickness=1,textvariable=txtname).grid(row=4,column=1,pady='5',padx='30',sticky='e')

#endregion


#regionFunction
def Downloadfunc():
    path=txtsave.get()
    if len(txtlink.get()) and len(txtsave.get()) !=0:

        try:

            getlink=YouTube(str(txtlink.get()))

        except:
            messagebox.showerror('error','connection error')
        file=getlink.streams.get_highest_resolution()

        try:
            if len(txtname.get())!=0:
                file.download(path,txtname.get()+'.mp4')
            else:
                file.download(path)

            messagebox.showinfo('Done','Video Downloaded')
        except:
            messagebox.showerror('Error','error in saving')
    else:
        messagebox.showerror('error',"video's link and direction must not be empty")
def Clearfunc():
    for text in window.winfo_children():
        if type(text)==Entry:
            text.delete(0, END)
def Aboutfunc():
    messagebox.showinfo('Developer','Mohammad Farokhi\n mohammadfarokhi99@gmail.com')







def Browsefunc():
    Download_Directory=filedialog.askdirectory(initialdir='Your Directory Path',title='Direction')
    txtsave.set(Download_Directory)

#endregion


#region button
btndownload=Button(window,text='Download',width='10',font='arial 10',highlightthickness=1,relief='groove',command=Downloadfunc,bg='pale violet red',highlightbackground='pale violet red',activebackground='pale violet red').grid(row=7,column=1,pady='10')
btnclear=Button(window,text='Clear',width='10',font='arial 10',highlightthickness=1,relief='groove',command=Clearfunc,bg='tan1',activebackground='tan1',highlightbackground='tan1').grid(row=8,column=1)
btnbrowse=Button(window,text='browse',width='10',font='arial 10',highlightthickness=1,relief='groove',bg='gray15',height='1',activebackground='gray15',fg='white',highlightbackground='gray15',command=Browsefunc).grid(row=6,column=1,pady='10',padx='25',sticky='e')
btnabout=Button(window,text='AboutDeveloper',width='15',font='times 10 italic',highlightthickness=1,relief='groove',bg='tan1',highlightbackground='tan1',activebackground='tan1',command=Aboutfunc).place(x='10',y='320')

#endregion
window.mainloop()
#endregion