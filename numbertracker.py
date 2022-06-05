vfrom ast import operator
from inspect import trace
from tkinter import *
from tokenize import String
from turtle import heading, position
from unittest import result
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
root.title("Number Tracker")
root.geometry("925x500+300+200")
root.resizable(False,False)
root.config(bg="#fff")

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


# ==========================background=====================================
heading=Label(root,text="Pelacak Nomer",font=("Nunito",15,"bold"), fg='black')
heading.place(x=400,y=40)

#Entry
Entry_back=PhotoImage(file="assets/search.png")
Label(root, image=Entry_back).place(x=530,y=110)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,font=("Arial",20),justify="center")
enter_number.place(x=548,y=114)

#button
search_image=PhotoImage(file="assets/search.png")
search=Button(image=search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=530,y=170)


country=Label(root,text="Country:",bg="#fff",fg="black",font=("arial",10,"bold"))
country.place(x=530,y=270)
sim=Label(root, text="SIM:",bg="#fff",fg="black",font=("arial",10,"bold"))
sim.place(x=740,y=270)
zone=Label(root,text="TimeZone:",bg="#fff",fg="black",font=("arial",10,"bold"))
zone.place(x=530,y=330)
clock=Label(root,text="Phone Time:",bg="#fff",fg="black",font=("arial", 10,"bold"))
clock.place(x=740,y=330)
longitude=Label(root, text="Longitude:",bg="#fff",fg="black",font=("arial", 10,"bold"))
longitude.place(x=530,y=390)
latitude=Label(root, text="Latitude:",bg="#fff",fg="black",font=("arial",10,"bold"))
latitude.place(x=740,y=390)
root.mainloop()