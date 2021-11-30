from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
# from firebase_admin import firestore, _sseclient
# import RPi.GPIO as GPIO
# import time
dbjson = '/Users/William/Desktop/Light/light-d7c0b-aef8206d738e.json'
cred = credentials.Certificate(dbjson)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://light-d7c0b.firebaseio.com/'
})
ref = db.reference()
light1 = ref.child('light1')

def listener(message):
    return (message)

#print((_sseclient.Event().data('data')))
# light1.set(False) #Setting light1 to False
#print("--------------------------------------------------------------------------")
#print (light1.listen(listener("")))

#Switch Mode
# if light1.get() == False:
#     light1.set(True)
#     print("Light is on")
# else:
#     light1.set(False)
#     print("Light is off")

from tkinter import *
root = Tk()
root.title('On/Off Switch!')
root.geometry("500x300")
is_on = True
my_label = Label(root,
    text = "The Switch Is On!",
    fg = "green",
    font = ("Helvetica", 32))
 
my_label.pack(pady = 20)
 
# Define our switch function
def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        my_label.config(text = "The Switch is Off",
                        fg = "black")
        is_on = False
        light1.set(False)
    else:
        on_button.config(image = on)
        my_label.config(text = "The Switch is On", fg = "green")
        is_on = True
        light1.set(True)
 
# Define Our Images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")
 
# Create A Button
on_button = Button(root, image = on, bd = 0,
                   command = switch)
on_button.pack(pady = 50)
 
# Execute Tkinter
root.mainloop()