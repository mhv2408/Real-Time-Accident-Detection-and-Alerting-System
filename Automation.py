from email import message
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def Msg(name,msg):
    startfile('C:\\Users\\MHV24\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    sleep(25)

    click(x=272, y=149)

    sleep(2)

    write(name)

    sleep(2)

    click(x=173, y=293)

    sleep(2)

    click(x=801, y=986)

    sleep(2)

    write(msg)

    press('enter')

#Msg('Triplet',"Gate Ranker Vamsi")
