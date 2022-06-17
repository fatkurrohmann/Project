import code                         
from tkinter import *
from tkinter import messagebox
from numpy import sign
import ast
import csv
import pandas as pd

root=Tk()                                   #definisi eksekusi program 
root.title("Number Tracker")                #membuat judul program Number Tracker
root.geometry("925x500+300+200")            #mengatur ukuran program
root.configure(bg="#fff")                   #membuat background program menjadi putih
root.resizable(False,False)                 #mengatur ukuran program agar tidak bisa di perbesar atau di perkecil    
#-------------------------------------------------------------------------------------------------------------------
def masuk():                                        #membuat fungsi dari command masuk ketika button signin ditekan
    userData = pd.read_csv('data.csv')              #membuat variabel userData dengan nilai dari data.csv
    df = pd.DataFrame(userData)                     #membuat variabel df dengan nilai dari userData
    if user.get()=="" or pas.get()=="":             #membuat kondisi jika user atau pas kosong
        messagebox.showerror("Error", "All field required")                                 #membuat pesan error jika field kosong
    elif (len(df[(df.namaPengguna == user.get()) & (df.kataSandi == pas.get())]) > 0):      #membuat kondisi jika user dan pas sama dengan data yang ada di data.csv
        root.destroy()                                                                      #menghapus root
        import numbertracker                                                                #melakukan import numbertracker
    else:                                                                                           
        messagebox.showerror("Error", "Email atau Password Anda salah")                     #membuat pesan error jika email atau passalah

def btn_sign_up():                                                                          #membuat fungsi dari command signup ketika button signup ditekan
    root.destroy()                                                                          #menghapus root
    import registrasi                                                                       #melakukan import file registrasi
    

img = PhotoImage(file="assets/login.png")                                                   #memasukkan gambar login.png ke dalam frame
Label(root,image=img,bg='white').place(x=50,y=50)                                           #membuat label dengan gambar login.png

frame=Frame(root,width=350,height=350,bg="white")                                           #membuat frame dengan ukuran 350x350 dan bg putih
frame.place(x=480,y=70)                                                                     #membuat frame dengan posisi x=480 dan y=70

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold')) #membuat label dengan text Sign in dan font Microsoft YaHei UI Light dan ukuran 23
heading.place(x=100,y=5)                                                                                #membuat label dengan posisi x=100 dan y=5
#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):                                                                        #membuat fungsi dari command on_enter
    user.delete(0,'end')                                                                #menghapus isi dari user

def on_leave(e):                                                                        #membuat fungsi dari command on_leave
    name=user.get()                                                                     #membuat variabel name dengan isi dari user
    if name=='':                                                                        #membuat kondisi jika name kosong
        user.insert(0,'Username')                                                       #menambahkan isi dari user
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))           #membuat tempat untuk entry username
user.place(x=30,y=80)                                                                                       #membuat entry username dengan posisi x=30 dan y=80
user.insert(0,'Username')                                                                                   #menambahkan isi dari user
user.bind('<FocusIn>',on_enter)                                                                             #membuat tempat untuk entry password
user.bind('<FocusOut>',on_leave)                                                                            #membuat fungsi dari command on_leave

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)                                #membuat frame dengan ukuran 295x2 dan bg hitam

#-------------------------------------------------------------------------------------------------------------------
def on_enter(e):                                                                            #membuat fungsi dari command on_enter
    pas.delete(0,'end')                                                                     #menghapus isi dari pas

def on_leave(e):                                                                            #membuat fungsi dari command on_leave
    name=pas.get()                                                                          #membuat variabel name dengan isi dari pas
    if name=='':                                                                            #membuat kondisi jika name kosong
        pas.insert(0,'Password')                                                            #menambahkan isi dari pas
pas = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))       #membuat tempat untuk entry password
pas.place(x=30,y=150)                                                                               #membuat entry password dengan posisi x=30 dan y=150
pas.insert(0,'Password')                                                                            #menambahkan isi dari pas
pas.bind('<FocusIn>',on_enter)                                                                      #membuat tempat untuk entry password
pas.bind('<FocusOut>',on_leave)                                                                     #membuat fungsi dari command on_leave

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)                    #membuat frame dengan ukuran 295x2 dan bg hitam

#-------------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0, command=masuk).place(x=35,y=204)  #membuat button signin dengan ukuran 39x7 dan bg #57a1f8 dan fg white dan border 0 dan command masuk
Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))      #membuat label dengan text Don't have an account? dan font Microsoft YaHei UI Light dan ukuran 9
Label.place(x=75,y=270)                                                                             #membuat label dengan posisi x=75 dan y=270 

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=btn_sign_up)      #membuat button signup dengan ukuran 6x0 dan bg white dan border 0 dan command btn_sign_up
sign_up.place(x=215,y=270)          #membuat button signup dengan posisi x=215 dan y=270






root.mainloop()            #membuat root menjalankan fungsi mainloop