from tkinter import *
import os

def restart():
    os.system("shutdown /r /t/ 1") 
    #/r is for restarting the os and /t is for including time delay e.g /t 1 = 1 second

def restart_time():
    os.system("shutdown /r /t  10")

def logout():
    os.system("shutdown -l")
    # -l is used for logging out of the os

def shutdown():
    os.system("shutdown /s /t/ 1")
    # /s is for shutting down the system
sd = Tk()
sd.title("ShutDown App")

#size of the gui panel height = 500px and width = 500px 
sd.geometry("500x500")  

# bg attribute is used to set background color 
sd.config(bg="#FF6363")


# creating buttons using Button function of tkinter module
r_button = Button(sd,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=80,height=60,width=200)

r_button = Button(sd,text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
r_button.place(x=150,y=220,height=60,width=200)

r_button = Button(sd,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
r_button.place(x=150,y=360,height=60,width=200)


# all the code should be above the mainloop() function call to run GUI
sd.mainloop()

