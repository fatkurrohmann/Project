from ast import operator
from inspect import trace
from tkinter import *
from tokenize import String
from turtle import heading, position
from unittest import result
from numpy import number, size
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Pelacak Nomer Telpon")
root.geometry("116x718")
root.resizable(False,False)
root.resizable(0,0)
root.state('zoomed')

def track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    #country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)
    #operator like idea, airtel, jio and many other
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)
    #Phone timezone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)
    #logitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    #time showing in phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

# ==========================background=====================================
bg = PhotoImage(file="background.png")
my_canvas = Canvas(root, width=1366, height=768)
my_canvas.pack(fill="both", expand=True,)
my_canvas.create_image(0, 0, anchor="nw", image=bg)
#make background full screen
my_canvas.config(width=root.winfo_screenwidth(), height=root.winfo_screenheight())



heading=Label(root,text="Pelacak Nomer",font=("Arial",15,"bold"),fg="blue")
heading.place(x=90,y=110)

#Entry
Entry_back=PhotoImage(file="search.png")
Label(root, image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,font=("Arial",20),justify="center")
enter_number.place(x=38,y=194)

#button
search_image=PhotoImage(file="search.png")
search=Button(image=search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=23,y=265)


country=Label(root,text="Country:",bg="#57adff",fg="black",font=("arial",10,"bold"))
country.place(x=50,y=420)
sim=Label(root, text="SIM:",bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=420)
zone=Label(root,text="TimeZone:",bg="#57adff",fg="black",font=("arial",10,"bold"))
zone.place(x=50,y=470)
clock=Label(root,text="Phone Time:",bg="#57adff",fg="black",font=("arial", 10,"bold"))
clock.place(x=200,y=470)
longitude=Label(root, text="Longitude:",bg="#57adff",fg="black",font=("arial", 10,"bold"))
longitude.place(x=50,y=520)
latitude=Label(root, text="Latitude:",bg="#57adff",fg="black",font=("arial",10,"bold"))
latitude.place(x=200,y=520)
root.mainloop()