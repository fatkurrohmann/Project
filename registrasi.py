from cProfile import label
from tkinter import *                                                           #gunakan library tkinter untuk membuat GUI
from tkinter import messagebox                                                  #gunakan massagebox untuk menampilkan pesan error dan success
from turtle import heading                                                      #gunakan turtle 
import csv                                                                      #gunakan library csv untuk menyimpan data
import pandas as pd                                                             #gunakan library pandas
from setuptools import Command                                                              


window=Tk()                                                                         #definisi eksekusi program
window.title("Number Tracker")                                                      #membuat judul program
window.geometry("925x500+300+200")                                                  #definisi ukuran dan posisi program
window.configure(bg="#fff")                                                         #membuat background program menjadi putih
window.resizable(False,False)                                                       #membuat program tidak dapat diubah ukuran

user = StringVar()                                                              #mengatur inputan username berupa string
pas = StringVar()                                                               #mengatur inputan password berupa string

def daftar():                                                                                        #fungsi daftar dari command di button 
    if user.get()=="Username" or pas.get()=="Password":                                              #jika username atau password kosong
        messagebox.showerror("Error", "All fields are required")                                     #maka akan muncul pesan error
    else:
        newuser = {'namaPengguna' : [user.get()],                                                    #jika username dan password tidak kosong
                    'kataSandi' : [ pas.get()]}                                                      #maka akan menyimpan data username dan password
        registeruser = pd.DataFrame(newuser)                                                         #membuat dataframe dari data yang diinputkan
        registeruser.to_csv('data.csv', mode='a', index=False, header=False)                         #menyimpan data ke dalam file csv
        messagebox.showinfo("Success", "Register Successfully")                                      #menampilkan pesan success
     

def sign():                                                                       #fungsi sign in dari command di button
    window.destroy()                                                              #menghapus window
    import login                                                                  #memanggil file login

img=PhotoImage(file="assets/SignUp.png")                                                            #memasukkan gambar ke dalam window
Label(window,image=img,border=0,bg="white").place(x=50,y=90)                                        #membuat label dengan gambar

frame=Frame(window,width=350,height=390,bg="#fff")                                                                      #membuat frame
frame.place(x=480,y=50)                                                                                                 #menentukan lokasi dari frame

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="#fff",font=("Microsoft YaHei UI Light",23,"bold"))              #membuat label dengan font dan warna Microsoft YaHei UI Light ukuran 23
heading.place(x=100,y=5)                                                                                            #menentukan lokasi dari label

#------------------------------------------------------------------------------------------------------------------- 
def on_enter(e):                                                                        #fungsi on_enter dari command di entry
    user.delete(0,'end')                                                                #menghapus isi dari entry username
def on_leave(e):                                                                        #fungsi on_leave dari command di entry
    if user.get()=='':                                                                  #jika username kosong
        user.insert(0,'Username')                                                       #maka akan menampilkan username

user = Entry(frame,textvariable=user,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))             #membuat entry username         
user.place(x=30,y=80)                                                                                                           #mengatur posisi inputan username
user.insert(0,'Username')                                                                                                       #mengatur isi dari entry yakni berupa 'username'
user.bind('<FocusIn>',on_enter)                                                                                                 #membuat tulisan username fokus
user.bind('<FocusOut>',on_leave)                                                                                                #membuat entry password fokus

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)                                   #membuat frame dengan warna black
#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):                                                    #fungsi on_enter dari command di entry
    pas.delete(0,'end')                                             #menghapus isi dari entry password
def on_leave(e):                                                    #fungsi on_leave dari command di entry
    if user.get()=='':                                              #jika password kosong
        pas.insert(0,'Password')                                    #maka akan menampilkan password

pas=Entry(frame,textvariable=pas,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))                    #membuat entry password
pas.place(x=30,y=150)                                                                                                              #mengatur posisi inputan password
pas.insert(0,'Password')                                                                                                           #mengatur isi dari entry yakni berupa 'password'
pas.bind('<FocusIn>',on_enter)                                                                                                     #membuat tulisan password fokus
pas.bind('<FocusOut>',on_leave)                                                                                                    #membuat entry password fokus

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)                         #membuat frame dengan warna black
#-------------------------------------------------------------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',font=('Microsoft YaHei UI Light',11,),border=0, command=daftar).place(x=3,y=280)#membuat button dengan font Microsoft YaHei UI Light ukuran 11
label=Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft YaHei UI Light",9)) #membuat label dengan font Microsoft YaHei UI Light ukuran 9
label.place(x=90,y=340)                                                                               #mengatur posisi label

signin=Button(frame,width=6,text='Sign In',bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light',11,),border=0,cursor='hand2',command=sign) #membuat button dengan font Microsoft YaHei UI Light ukuran 11
signin.place(x=197,y=335)     #mengatur posisi button


window.mainloop()             #memanggil window agar dapat dijalankan