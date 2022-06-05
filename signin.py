import code
from tkinter import *
from tkinter import messagebox
from numpy import sign
import ast

root=Tk()
root.title("Number Tracker")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

#-------------------------------------------------------------------------------------------------------------------
#Proses login dan setelah login berhasil masuk ke dasb
def signin():
    username=user.get()
    password=code.get()
    if username=='admin' or password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.configure(bg="white")
        screen.mainloop()
    else:
        messagebox.showinfo("Login Failed","Username and Password is incorrect")
#-------------------------------------------------------------------------------------------------------------------
#User Signup
def signup():
    window=Tk()
    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
    img=PhotoImage(file="assets/SignUp.png")
    lbl =Label(window,image=img,border=0,bg="white")
    lbl.place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg="red")
    frame.place(x=480,y=90)

    window.mainloop()




img=PhotoImage(file="assets/login.png")
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#-------------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
Label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)






root.mainloop()