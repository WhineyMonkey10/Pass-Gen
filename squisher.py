# Imports
from Numbers.num2 import *
from Numbers.num3 import *
from Numbers.num4 import *
from Numbers.num5 import *
from Numbers.num6 import *
from Numbers.num7 import *
from Characters.char2 import *
from Characters.char3 import *
from Characters.char4 import *
from Characters.char5 import *
from Characters.char6 import *
import PySimpleGUI as sg
import os


# Function
def getPass():
    # Main
    clear = lambda: os.system('clear')
    
    password1 = findFirst1()
    password2 = findFirst2()
    password3 = findFirst3()
    password4 = findFirst4()
    password5 = findFirst5()
    password6 = findFirst6()
    char1 = findChar1()
    char2 = findChar2()
    char3 = findChar3()
    char4 = findChar4()
    char5 = findChar5()
    print (password1, char1, password2, char2, password3, char3, password4, char4, password5, char5, password1, char1, password2, char2, password3, char3, password4, char4, password5, char5)
    
    layout = [[sg.Text("Please Check The Console For Your Password")]], [sg.Button("OK")]

    # Create the window
    window = sg.Window("Password Generator", layout)

    # Create an event loop
    while True:
     event, values = window.read()
     # End program if user closes window or
     # presses the OK button
     if event == "OK" or event == sg.WIN_CLOSED:
            clear()
            break
            

    window.close()