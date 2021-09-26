# import random
import tkinter as tk


root = tk.Tk()
root.title("Numbers To Words Converter")
root.geometry("400x400")


def conversion():
    
    def number_to_words(digit):
        roots = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
         6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 
         11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
         16:"sixteen", 17:"seventeen", 18:"eighteen",19:"nineteen", 20:"twenty", 
         30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

        if int(digit) in roots.keys():
            print (roots[int(digit)])
        
        elif len(digit) == 2:
            print (roots[int(digit[0]+'0')]+"-"+roots[int(digit[-1])])
            
        elif len(digit) == 3:
            if int(digit[1:]) == 0:
                print (roots[int(digit[0])]+ " hundred")
            elif int(digit[2]) != 0:
                print (roots[int(digit[0])]+ " hundred and "+roots[int(digit[1]+'0')]+"-"+roots[int(digit[-1])])
            else:
                print(roots[int(digit[0])]+ " hundred and "+roots[int(digit[1]+'0')] )
        else:
            print ("Try again")

        digit = int(entry.get())

        return number_to_words(digit)

def output():
    display = conversion()
    # creates text field

    display_dis = tk.Text(master=root, height=10, width=30)
    display_dis.grid(column=0, row=3)

    display_dis.insert(tk.END, display)


text1 = tk.Label(text="Type a number: ",font = ('Times New Roman',14, 'bold'), fg = 'black')
text1.grid(column=0, row=1)

entry = tk.Entry()
entry.grid(column=1, row=1)

button = tk.Button(text="Click Me", font = ('Times New Roman',14, 'bold'), fg = 'black', command=output)
button.grid(column=2, row=1)


root.mainloop()