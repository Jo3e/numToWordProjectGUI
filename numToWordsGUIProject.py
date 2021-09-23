from tkinter import *


def conversion():
    programcode


    


root = Tk()
input_label = Label(text='Input a number:', font = ('verdana',14, 'bold italic'), bg = 'white', fg = 'purple')
conv_button = Button(text = 'Enter', font =('verdana', 12, 'bold italic'), fg = 'white', bg = 'blue', command = conversion)
entry = Entry(font=('Verdana', 16), width=3)

output_label = Label(font = ('verdana', 16, 'bold italic'))


input_label.grid(row=0, column=0)
entry.grid(row=0, column=1)

conv_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
mainloop()