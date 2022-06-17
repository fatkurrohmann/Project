from ast import operator                        #importing operator
from inspect import trace                       #def track():
from tkinter import *                           #importing tkinter
from tokenize import String                     #def track():
from turtle import heading, position            
from unittest import result
from numpy import number, size
import phonenumbers                             #mengimport library phonenumbers
from phonenumbers import carrier                
from phonenumbers import geocoder
from phonenumbers import timezone
from setuptools import Command
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from PIL import Image, ImageTk
import csv                                      #mengimport csv
import pandas as pd                             #mengimport library pandas
from tkinter import messagebox                  #mengimport library messagebox

root=Tk()                                                   #definisi eksekusi program
root.title("Number Tracker")                                #membuat judul program Number Tracker
root.geometry("925x500+300+200")                            #mengatur ukuran program 
root.resizable(False,False)                                 #membuat agar program tidak dapat diperbesar atau diperkecil
root.config(bg="#fff")                                      #membuat background program menjadi putih

def track():                                                        #memanggil librari dengan fungsi track
    enter_number=entry.get()                                        #membuat variabel enter_number dengan nilai dari entry
    number=phonenumbers.parse(enter_number)                         #membuat variabel number dengan nilai dari phonenumbers
    #country
    locate=geocoder.description_for_number(number,'en')             #membuat variabel locate dengan nilai dari geocoder
    country.config(text=locate)                                     #membuat text pada label country dengan nilai dari locate
    #operator like idea, airtel, jio and many other
    operator=carrier.name_for_number(number,'en')                   #membuat variabel operator dengan nilai dari carrier
    sim.config(text=operator)                                       #membuat text pada label sim dengan nilai dari operator
    #Phone timezone
    time = timezone.time_zones_for_number(number)                   #membuat variabel time dengan nilai dari timezone
    zone.config(text=time)                                          #membuat text pada label zone dengan nilai dari time
    #logitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")            #membuat variabel geolocator dengan nilai dari Nominatim
    location = geolocator.geocode(locate)                           #membuat variabel location dengan nilai dari geolocator

    lng=location.longitude                                          #membuat variabel lng dengan nilai dari location
    lat=location.latitude                                           #membuat variabel lat dengan nilai dari location
    longitude.config(text=lng)                                      #membuat text pada label longitude dengan nilai dari lng
    latitude.config(text=lat)                                       #membuat text pada label latitude dengan nilai dari lat

    #time showing in phone
    obj = TimezoneFinder()                                                                          #membuat variabel obj dengan nilai dari TimezoneFinder
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)                         #membuat variabel result dengan nilai dari obj 

    def track():                                                                                
        if enter_number=="":
            messagebox.showerror("Error", "All field required")
        else:
            pencarian = { "number": [enter_number], "country": [locate], "operator": [operator], "timezone": [result], "longitude": [lng], "latitude": [lat] }
            hasil = pd.DataFrame(pencarian)
            hasil.to_csv('hasil.csv', mode='a', header=False, index=False)
            messagebox.showinfo("Success", "Data has been saved")
# ==========================gambar=========================================

# ==========================background=====================================
heading=Label(root,text="Pelacak Nomer",font=("Nunito",15,"bold"), fg='black')              #membuat label heading dengan font Nunito, ukuran 15, dan warna huruf black
heading.place(x=400,y=40)                                                                   #membuat label heading dengan posisi x 400 dan y 40

#Entry
Entry_back=PhotoImage(file="assets/search.png")                                             #memasukkan gambar search.png ke dalam program untuk background entry
Label(root, image=Entry_back).place(x=530,y=110)                                            #membuat label dengan posisi x 530 dan y 110

entry=StringVar()                                                                                       #membuat variabel entry dengan nilai string
enter_number=Entry(root,textvariable=entry,width=17,font=("Arial",20),justify="center")                 #membuat entry dengan nilai string, ukuran 17, font Arial, dan text center
enter_number.place(x=548,y=114)                                                                         #membuat entry dengan posisi x 548 dan y 114

#button
search_image=PhotoImage(file="assets/search.png")                                                    #memasukkan gambar search.png ke dalam program untuk background button
search=Button(image=search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)  #membuat button dengan gambar search.png, borderwidth 0, cursor hand2, bd 0, font arial, dan command track
search.place(x=530,y=170)                                                                            #membuat button dengan posisi x 530 dan y 170


country=Label(root,text="Country:",bg="#fff",fg="black",font=("arial",10,"bold"))                    #membuat label country dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
country.place(x=530,y=270)
sim=Label(root, text="SIM:",bg="#fff",fg="black",font=("arial",10,"bold"))                           #membuat label sim dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
sim.place(x=740,y=270)                                                                               #membuat label sim dengan posisi x 740 dan y 270
zone=Label(root,text="TimeZone:",bg="#fff",fg="black",font=("arial",10,"bold"))                      #membuat label zone dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
zone.place(x=530,y=330)                                                                              #membuat label zone dengan posisi x 530 dan y 330
clock=Label(root,text="Phone Time:",bg="#fff",fg="black",font=("arial", 10,"bold"))                  #membuat label clock dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
clock.place(x=740,y=330)                                                                            #membuat label clock dengan posisi x 740 dan y 330
longitude=Label(root, text="Longitude:",bg="#fff",fg="black",font=("arial", 10,"bold"))             #membuat label longitude dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
longitude.place(x=530,y=390)                                                            #membuat label longitude dengan posisi x 530 dan y 390
latitude=Label(root, text="Latitude:",bg="#fff",fg="black",font=("arial",10,"bold"))    #membuat label latitude dengan background putih, warna huruf black, font arial, ukuran 10, dan bold
latitude.place(x=740,y=390)                                                             #membuat label latitude dengan posisi x 740 dan y 390
root.mainloop()                                                                         #membuat root mainloop