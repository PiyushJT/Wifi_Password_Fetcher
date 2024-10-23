# Importing neccessary things
import subprocess                   # for cmd command
import tkinter as tk                # for Gui
from tkinter import ttk
import tkinter.font as font         # for tkinter font
import wifi_qrcode_generator as qr  # for qr code
from PIL import ImageTk, Image      # for converting to image



# Setting up tkinter for gui
root= tk.Tk()
root.title('Wifi password')
root.geometry('400x700')
root.iconbitmap(r"assets\\icon.ico")  # icon



# displaying the text --- {wifi password of...} ---in orange color
label= tk.Label(root, text='\n\n Wifi password of...\n\n ', width=400, height=3, bg= 'black', fg= '#ffa500', font=('', 14))
label.pack()



# Getting wifi networks list from CMD
data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"]).decode("utf-8")
wifi = []
no_of_Networks = data.count("Profile     :")

for i in range(no_of_Networks):
    j = data.find("Profile     :")+14
    data = data[j:len(data)]
    k = data.find("    All")-2
    wifi_elmt = data[0:k]
    if wifi_elmt[-1] == "\r":
        wifi_elmt = wifi_elmt[0:-1]
    wifi.append(wifi_elmt)



# function to get password and its qr code
def entry_update(Ntwrk):
    # Getting output from CMD
    dataprfle = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles", Ntwrk, "key=clear"]).decode("utf-8")

    # Extractig password
    st = dataprfle.find("Key Content            :")+25
    end = dataprfle.find("Cost settings")-4
    password = dataprfle[st:end]

    # Displaying password
    hi.config(text= f'\n{password}\n')
 
    # Creating a QR Code Image
    qrCode = qr.wifi_qrcode(Ntwrk, False, 'WPA', password)

    # Saving the image as PNG file
    qrCode.save("assets\\code.png")

    imagechange()


# fuction to display qr code
def imagechange():
    image1= tk.PhotoImage(file= "assets\\code.png")
    image.configure(image= image1)
    image.image= image1



# Getting the right network using tkinter buttons
button={}
for i in wifi:
    def func(x=i):
        return entry_update(x)

    button[i]=ttk.Button(root, width=300, text=i, command= func)
    button[i].pack()



# Predisplay password and code and then modify it

# password
hi= tk.Label(root, text='\n<Password>\n', width=400, bg= 'black', fg= '#00ff00', font=('', 16))
hi.pack()

# qr code
image= tk.Label(root)
image.pack()



# Tkinter loop
root.mainloop()