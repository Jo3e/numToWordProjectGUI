
import tkinter as tk





def format_number():
    display_label['text'] = f"{command}"

    

    
def number_to_words(digit):
        roots = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
         6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 
         11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
         16:"sixteen", 17:"seventeen", 18:"eighteen",19:"nineteen", 20:"twenty", 
         30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

        if int(digit) in roots.keys():
            return (roots[int(digit)])
            
            
        elif len(digit) == 2:
            return (roots[int(digit[0]+'0')]+"-"+roots[int(digit[-1])])
            
        elif len(digit) == 3:
            if int(digit[1:]) == 0:
                return (roots[int(digit[0])]+ " hundred")
                
            elif int(digit[2]) != 0:
                return (roots[int(digit[0])]+ " hundred and "+roots[int(digit[1]+'0')]+"-"+roots[int(digit[-1])])
               
            else:
                return (roots[int(digit[0])]+ " hundred and "+roots[int(digit[1]+'0')])
               
        else:
            return ("Try again")

        
        

if __name__ == "__main__":    

    HEIGHT= 500
    WIDTH=600
    root = tk.Tk()
    root.title("Numbers To Words Converter")
    #root.geometry("400x400")
    
    canvas = tk.Canvas(root,height =HEIGHT, width = WIDTH)
    canvas.pack()

    # background_image = tk.PhotoImage(file='imagee.png')
    # background_label = tk.Label(root,image=background_image)
    # background_label.place(relwidth=1,relheight=1)


    frame = tk.Frame(root,bg= '#d6d6c2',bd=5)
    frame.place(relx=0.1, rely=0.1, relwidth=0.75,relheight=0.1,anchor='nw')

    input_text = tk.Label(frame,text="Type a number:", fg = '#ffffff', bg="#666633",font=40)
    input_text.place(relx=0,rely=0,relwidth=0.25,relheight=1)

    entry = tk.Entry(frame,font=40)
    entry.place(relx=0.25,rely=0,relwidth=0.4,relheight=1)

    button = tk.Button(frame, text='Click Me!', fg="#ffffff", bg='#666633',font=40, command =lambda:number_to_words(entry.get()))
    button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

    display_frame = tk.Frame(root,bg="#d6d6c2",bd=5)
    display_frame.place(relx=0.1,rely=0.3,relwidth=0.75,relheight=0.5, anchor='nw')

    display_label =  tk.Label(display_frame,text="" )
    display_label.place(relwidth=1,relheight=1 ) 

    root.mainloop()