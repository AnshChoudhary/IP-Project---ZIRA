from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as connector
import pandas
import yagmail
import subprocess
 
def sendmail():
    mainwindow = Tk()
    mainwindow.geometry('800x525')
    mainwindow.configure(background = "#0C4C5D")

    headinglabel = Label(mainwindow, text="ZIRA Mail", font='times 24 bold underline')
    itemlabel = Label(mainwindow, text="Recepient's mail ID: ", font='times 12 bold')
    txtbillno = Entry(mainwindow)
    txtdata = Entry(mainwindow, width=70)
    namelabel = Label(mainwindow, text="Subject: ", font='times 12 bold')
    txtname= Entry(mainwindow,width=50)

    def savedataentry():
        to = txtbillno.get()
        subject = txtname.get()
        content = txtdata.get()

    def sendmail():
        yagmail.register("anshc19@gmail.com", "mark1901")
        # setting up the mail portal
        yag = yagmail.SMTP('anshc19@gmail.com')
        yag.send(to = txtbillno.get(), subject = txtname.get(), contents = txtdata.get())

    btnshowbillinfo = Button(mainwindow, text='Save', width=15, font='times 10 bold', command=savedataentry)
    btnsendinfo = Button(mainwindow, text='Send', width=15, font='times 10 bold', command = sendmail)

    headinglabel.place(x=300, y=15)
    itemlabel.place(x=50, y=80)
    txtbillno.place(x=220,y=80)
    btnshowbillinfo.place(x = 50,y=450)
    txtdata.place(x=50, y=200)
    namelabel.place(x=50,y=150)
    txtname.place(x=150,y = 150)
    btnsendinfo.place(x = 200,y=450)

    mainwindow.mainloop()


def downloadsong():
    mainwindow = Tk()
    mainwindow.geometry('500x400')
    mainwindow.configure(background = "#0C4C5D")
    itemlabel = Label(mainwindow, text="Song Name: ", font='times 12 bold')
    txtbillno = Entry(mainwindow)

    def downloadit():
        music = txtbillno.get()
        cmd = "spotdl --song '{}'".format(music)    # commands to be run on the command prompt 
        returned_value = subprocess.call(cmd, shell=True)    # runs commands on the Command Prompt
        print('returned value:', returned_value)  

    btndownloadinfo = Button(mainwindow, text='Download', width=15, font='times 10 bold', command = downloadit)
    itemlabel.place(x=50, y=80)
    txtbillno.place(x=220,y=80)
    btndownloadinfo.place(x = 200,y=250)
    mainwindow.mainloop()
