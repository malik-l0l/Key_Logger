"""
-- FOR LEARNING PURPOSE ONLY --
This is how hackers monitor your keyboard.
This program is extremely dangerous.
"""

from tkinter import *


def do_something(event):
    """
    display which key is pressed in the label
    :param event: event listener
    :return: None
    """

    print("You pressed : " + event.keysym)
    label.config(text=event.keysym)

    """
    The program below makes the code very dangerous.
    It will create a text-file 'not_spy.txt',
    which contains every keystroke you pressed in the keyboard
    after this program is executed in your computer
    
    NOTE:
    1) we can hide this text file in your computer using os module
    2) we can later transfer this file to a remote server 
        when internet connection is established.
    """
    # if len(event.keysym) > 1:
    #     print(x := f" ({event.keysym}) ", end="")
    #     with open("not_spy.txt", 'a+') as f:
    #         f.write(x)
    # else:
    #     print(x := event.keysym, end="")
    #     with open("not_spy.txt", 'a+') as f:
    #         f.write(x)


window = Tk()
window.geometry('210x50')
window.resizable(False, False)
window.title('Key-T')

window.bind('<Key>', do_something)  # listen for events in keyboard.

label = Label(window, font=('Impact', 30))
label.pack()

window.mainloop()
