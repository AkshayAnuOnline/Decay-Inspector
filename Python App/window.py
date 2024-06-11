import tkinter as tk
from tkinter import * #for GUI
from screeninfo import get_monitors #for retrieving monitor information


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('FirebaseKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': '***************'
})

# Reference to your database
mq4 = db.reference('MQ4')
cam = db.reference('cam')

window = Tk()
window.title("Decay Inspector")
unable = tk.PhotoImage(file = f"Assets\\Unable.png")
error = tk.PhotoImage(file = f"Assets\\Error.png")
safe = tk.PhotoImage(file = f"Assets\\Safe.png")
notsafe = tk.PhotoImage(file = f"Assets\\NotSafe.png")
    


def checknow():
    # Fetch the current value of 'MQ4' from Firebase
    sensor_value = mq4.get()

    if sensor_value is not None:
        if sensor_value > 75:
            c1 = canvas.create_image(26, 57, image=notsafe, anchor=NW)
        else:
            c1 = canvas.create_image(26, 57, image=safe, anchor=NW)
        canvas.after(6000, lambda: canvas.itemconfig(c1, state='hidden'))
    else:
        # Handle the case when sensor value is None
        print("Sensor value is not available")



def values():

    extra_window2 = tk.Toplevel()
    extra_window2.iconbitmap(f"Assets\DI.ico")

    WIN_WIDTH = 1663
    WIN_HEIGHT = 935
    extra_window2.geometry(
        f"{WIN_WIDTH}x{WIN_HEIGHT}+{(get_monitors()[0].width - WIN_WIDTH) // 2}+{(get_monitors()[0].height - WIN_HEIGHT) // 2}")
    extra_window2.configure(bg="#FFFFFF")
    extra_window2.title("Food Scan - Decay Inspector")
    canvas = Canvas(
    extra_window2,
    bg = "#FFFFFF",
    height = 935,
    width = 1663,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    fooddetected = cam.get()
    fooddetected = cam.get()
    if fooddetected == "Orange":
        background_img = PhotoImage(file=f"Assets/Orange.png")
    elif fooddetected == "Banana":
        background_img = PhotoImage(file=f"Assets/Banana.png")

    background = canvas.create_image(
        831.5, 467.5,
        image=background_img)
    extra_window2.resizable(False, False)
    extra_window2.mainloop()

window.iconbitmap(f"Assets\DI.ico")
WIN_WIDTH = 1100
WIN_HEIGHT = 618
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{(get_monitors()[0].width - WIN_WIDTH)//2}+{(get_monitors()[0].height - WIN_HEIGHT)//2}")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 618,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Assets/background.png")
background = canvas.create_image(
    550.0, 309.0,
    image=background_img)

img0 = PhotoImage(file = f"Assets/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = checknow,
    relief = "flat")

b0.place(
    x = 63, y = 510,
    width = 117,
    height = 40)

img1 = PhotoImage(file = f"Assets/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = values,
    relief = "flat")

b1.place(
    x = 922, y = 510,
    width = 117,
    height = 40)

window.resizable(False, False)
window.mainloop()
