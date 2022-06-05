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

root = Tk()
root.title("Number Tracker")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
# ==========================background=====================================
bg = PhotoImage(file="assets/mainbg.png")
my_canvas = Canvas(root, width=1366, height=768)
my_canvas.pack(fill="both", expand=True,)
my_canvas.create_image(0, 0, anchor="nw", image=bg)


root.mainloop()