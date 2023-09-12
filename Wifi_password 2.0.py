# Importing neccessary things
import subprocess
import tkinter as tk
from tkinter import ttk
import tkinter.font as font



# Setting up tkinter for gui
root= tk.Tk()
root.title('Wifi password')
root.geometry('400x380')



# displaying the text --- {wifi password of...} ---in blue color
label= tk.Label(root, text='\n\n Wifi password of...\n\n ', width=400, height=3, bg= 'black', fg= '#0000ff', font=('', 14))
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



# function to get password and display it
def entry_update(Ntwrk):
    # Getting output from CMD
    dataprfle = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles", Ntwrk, "key=clear"]).decode("utf-8")

    # Extractig password
    st = dataprfle.find("Key Content            :")+25
    end = dataprfle.find("Cost settings")-4
    password = dataprfle[st:end]

    # Displaying password
    hi.config(text= f'\n\n\n{password}\n\n')


# Getting the right network using tkinter buttons
button_dict={}
for i in wifi:
    def func(x=i):
        return entry_update(x)

    button_dict[i]=ttk.Button(root, width=300, text=i, command= func)
    button_dict[i].pack()



# Predisplay password then modify it
hi= tk.Label(root, text='\n\n<Password>\n\n', width=400, bg= 'black', fg= '#00ff00', font=('', 16))
hi.pack()


# Tkinter loop
root.mainloop()