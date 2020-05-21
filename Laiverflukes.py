from tkinter import *
from tkinter import messagebox
import time
import os
import re
from tkinter.font import Font

window = Tk()
window.title("Laiverflukes")
window.geometry("400x450+120+120")
window.resizable(False, False)
window.configure(bg='bisque4')
def new_acc():
    def done():
      if(current_name.get()=="" or current_password.get()==""):
        messagebox.showwarning("Error", "Invalid username or password!")
      else:
        c_name=current_name.get()
        c_password=current_password.get()
        file = open("turtle.txt","w")
        file.write(c_name+"#"+c_password)
        account.destroy()

    account = Toplevel()
    account.configure(bg='bisque4')
    account.geometry("400x450+120+120")
    account.resizable(False, False)
    Label(account,text="Create New Account...",font=my_font1,bg='bisque4').place(x=125, y=10)
    Label(account, text="Enter your name:", font=my_font1,bg='bisque4').place(x=50, y=150)
    Entry(account, textvariable=current_name,bg='bisque3').place(x=173, y=150)
    Label(account, text="Enter Password:", font=my_font1,bg='bisque4').place(x=55, y=175)
    Entry(account, textvariable=current_password, show="*",bg='bisque3').place(x=173, y=175)
    Button(account, text="Done", command=done,bg='bisque3').place(x=173, y=200)


def wel_window():
 try:
  file = open("turtle.txt", "r")
  detail = file.read()
  identity = detail.split('#', 2)
  t_name = typed_name.get()
  t_passwrd = typed_password.get()
  if t_name==identity[0] and t_passwrd==identity[1]:
    welcome = Toplevel()
    welcome.geometry("400x450+120+120")
    welcome.resizable(False, False)
    welcome.configure(bg='bisque4')
    def destroy_everything():
        welcome.destroy()
        window.quit()
    Label(welcome, text="Welcome", font=my_font1,bg='bisque4').place(x=170, y=10)
    Label(welcome, text="I am Laiverflukes", font=my_font1,bg='bisque4').place(x=147, y=37)
    Label(welcome, text="I can perform whatever you want !", font=my_font2,bg='bisque4').place(x=100, y=62)
    Label(welcome, text="I can open...", font=my_font2,bg='bisque4').place(x=55, y=150)
    Button(welcome, text="Microsoft Office    ", command=ms_office,bg='bisque3').place(x=158, y=180)
    Button(welcome, text="Applications           ", command=application,bg='bisque3').place(x=158, y=220)
    Button(welcome, text="Other Tools             ", command=other_tools,bg='bisque3').place(x=158, y=260)
    Button(welcome, text="System ShutDown ", command=shutdown,bg='bisque3').place(x=158, y=305)
    Button(welcome, text="LogOut", command=destroy_everything,bg='bisque3').place(x=158, y=355)
  else:
      messagebox.showwarning("Login Error","Incorrect username or password")
 except(FileNotFoundError):
     messagebox.showwarning("Login Error", "First create your account !")
def other_tools():
    mytools = Toplevel()
    mytools.geometry("400x450+120+120")
    mytools.configure(bg='bisque4')
    def paint():
        os.startfile("C:\\Windows\\System32\\mspaint.exe")
    def wordpad():
        os.startfile("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
    def destroytools():
        mytools.destroy()
    Label(mytools, text="Other Tools", font=my_font1,bg='bisque4').place(x=170, y=10)
    Label(mytools, text="I can open..", font=my_font2,bg='bisque4').place(x=55, y=100)
    Button(mytools, text="Paint               ", command=paint,bg='bisque3').place(x=158, y=160)
    Button(mytools, text="WordPad        ", command=wordpad,bg='bisque3').place(x=158, y=200)
    Button(mytools, text="Go back..", command=destroytools,bg='bisque3').place(x=158, y=290)
def shutdown():
    def shut_it():
        os.startfile("C:\\Windows\\System32\\shutdown.exe")
    def destroy_shut():
        shut.destroy()
    shut = Toplevel()
    shut.configure(bg='bisque4')
    shut.geometry("400x450+120+120")
    shut.resizable(False, False)
    Label(shut, text="System ShutDown", font=my_font1, bg='bisque4').place(x=140, y=10)
    Label(shut, text="Are you sure ?", font=my_font2,bg='bisque4').place(x=155, y=100)
    Label(shut, text="Your system will shut down anyhow !!!", font=my_font2,bg='bisque4').place(x=90, y=140)
    Button(shut, text="ShutDown ", command=shut_it,bg='bisque3').place(x=120, y=200)
    Button(shut, text="Go Back... ", command=destroy_shut,bg='bisque3').place(x=220, y=200)

def application():
    myapp = Toplevel()
    myapp.geometry("400x450+120+120")
    myapp.resizable(False, False)
    myapp.configure(bg='bisque4')
    def notepd():
        os.startfile("c:\\windows\\System32\\notepad.exe")
    def mychrome():
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome")
    def mytask():
        os.startfile("c:\\windows\\System32\\Taskmgr.exe")
    def destroyapp():
        myapp.destroy()
    Label(myapp, text="Applications", font=my_font1,bg='bisque4').place(x=170, y=10)
    Label(myapp, text="I can open..", font=my_font2,bg='bisque4').place(x=55, y=100)
    Button(myapp, text="Notepad             ",command=notepd,bg='bisque3').place(x=158, y=140)
    Button(myapp, text="Google Chrome",command=mychrome,bg='bisque3').place(x=158, y=180)
    Button(myapp, text="Task Manager    ",command=mytask,bg='bisque3').place(x=158, y=220)
    Button(myapp, text="Go back..",command=destroyapp,bg='bisque3').place(x=158, y=290)

def ms_office():
    microsoft_off = Toplevel()
    microsoft_off.geometry("400x450+120+120")
    microsoft_off.resizable(False, False)
    microsoft_off.configure(bg='bisque4')
    Label(microsoft_off, text="Microsoft Office", font=my_font1,bg='bisque4').place(x=170, y=10)

    def setpath():
        if b.get() == 64:
            path = "C:\\Program Files\\Microsoft Office\\"
        elif b.get() == 32:
            path = "C:\\Program Files (x86)\\Microsoft Office\\"

        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.EXE' in file:
                    files.append(os.path.join(r, file))
        return files

    def PowerPnt():
        files = setpath()
        for f in files:
            pattern = re.compile(r'POWERPNT.EXE', re.I)
            match = re.search(pattern, f)
            if match:
                # print(files.index(f), end=" ")
                # print(f)
                os.startfile(f)
                break
            else:
                continue

    def Word():
        files = setpath()
        for f in files:
            pattern = re.compile(r'WORD.EXE', re.I)
            match = re.search(pattern, f)
            if match:
                # print(files.index(f), end=" ")
                # print(f)
                os.startfile(f)
                break
            else:
                continue

    def Excel():
        files = setpath()
        for f in files:
            pattern = re.compile(r'EXCEL.EXE', re.I)
            match = re.search(pattern, f)
            if match:
                # print(files.index(f), end=" ")
                # print(f)
                os.startfile(f)
                break
            else:
                continue

    def onenote():
        files = setpath()
        for f in files:
            pattern = re.compile(r'ONENOTE.EXE', re.I)
            match = re.search(pattern, f)
            if match:
                # print(files.index(f), end=" ")
                # print(f)
                os.startfile(f)
                break
            else:
                continue
    def infopath():
        files = setpath()
        for f in files:
            pattern = re.compile(r'INFOPATH.EXE', re.I)
            match = re.search(pattern, f)
            if match:
                # print(files.index(f), end=" ")
                # print(f)
                os.startfile(f)
                break
            else:
                continue
    def destroymicro():
        microsoft_off.destroy()
    b = IntVar()
    b.set(64)

    Label(microsoft_off, text="Choose your system bit :", font=my_font2,bg='bisque4').place(x=55, y=55)
    Radiobutton(microsoft_off, text="64 bits", variable=b, value=64,bg='bisque4').place(x=55, y=85)
    Radiobutton(microsoft_off, text="32 bits", variable=b, value=32,bg='bisque4').place(x=55, y=115)
    Label(microsoft_off, text="I can open...", font=my_font2,bg='bisque4').place(x=55, y=145)
    Button(microsoft_off, text="MS PowerPoint", command=PowerPnt,bg='bisque3').place(x=158, y=175)
    Button(microsoft_off, text="MS Word           ", command=Word,bg='bisque3').place(x=158, y=215)
    Button(microsoft_off, text="MS Excel            ", command=Excel,bg='bisque3').place(x=158, y=255)
    Button(microsoft_off, text="MS OneNote     ",command=onenote,bg='bisque3').place(x=158, y=295)
    Button(microsoft_off, text="MS InfoPath      ",command=infopath,bg='bisque3').place(x=158, y=335)
    Button(microsoft_off, text="Go back..", command=destroymicro,bg='bisque3').place(x=158, y=385)

my_font1 = Font(family='Times',size=12)
my_font2 = Font(size=10)
my_font3 = Font(family='Times',size=20,underline=1)
typed_name=StringVar()
current_name=StringVar()
typed_password=StringVar()
current_password=StringVar()
Label(window,text="Laiverflukes",font=my_font3,bg="bisque4").place(x=140,y=20)
Label(window,text="Enter your name:",font=my_font1,bg='bisque4').place(x=50,y=150)
Entry(window,textvariable=typed_name,bg='bisque3').place(x=173,y=150)
Label(window,text="Enter Password:",font=my_font1,bg='bisque4').place(x=55,y=175)
Entry(window,textvariable=typed_password,show="*",bg='bisque3').place(x=173,y=175)
Button(window,text="Login",command=wel_window,bg='bisque3').place(x=173,y=200)
Button(window,text="       Create New Account       ",command=new_acc,bg='bisque3').place(x=125,y=275)

window.mainloop()
