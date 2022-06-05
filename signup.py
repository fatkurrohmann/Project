from cProfile import label
from tkinter import *
from tkinter import messagebox
import ast
from turtle import heading

from signin import on_enter, signup

window=Tk()
window.title("Number Tracker")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False,False)

def signup():
    username=user.get()
    password=password.get()
    konfirmasiPassword=konfirmasiPassword.get()

    if password==konfirmasiPassword:
        try:
            file=open("data.txt","r")
            d=file.read()
            r.ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open("data.txt","w")
            file.write(str(r))

            messagebox.showinfo("Success","Sign Up Success")
        except:
            file=open("data.txt","w")
            pp=str({'username':'password'})
            file.write(pp)
            file.close()
    else:
        massagebox.showerror("Error","Password not match")



img=PhotoImage(file="assets/SignUp.png")
Label(window,image=img,border=0,bg="white").place(x=50,y=90)

frame=Frame(window,width=350,height=390,bg="#fff")
frame.place(x=480,y=50)

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="#fff",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        password.insert(0,'Password')

password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    konfirmasiPassword.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        konfirmasiPassword.insert(0,'Confirm Password')

konfirmasiPassword = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
konfirmasiPassword.place(x=30,y=220)
konfirmasiPassword.insert(0,'Confirm Password')
konfirmasiPassword.bind('<FocusIn>',on_enter)
konfirmasiPassword.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#-------------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',font=('Microsoft YaHei UI Light',11,),border=0,command=signup).place(x=3,y=280)
label=Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign In',bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light',11,),border=0,cursor='hand2')
signin.place(x=197,y=335)







window.mainloop()