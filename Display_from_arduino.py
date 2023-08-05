import tkinter
from tkinter import Button
import time
import serial

h = 500
w = 1000

def create_animation_window():
     global window
     window = tkinter.Tk()
     window.title("Tkinter Animation Demo")
     window.geometry(f'{w}x{h}')
     
     return window

def create_animation_canvas(window):
      canvas = tkinter.Canvas(window)
      canvas.pack(fill="both", expand=True)
      exit_button = Button(window, text="Exit", command=window.destroy)
      exit_button.pack(pady=20)
      return canvas

def animate(window, canvas):
    colour=['','','','']
    dist=['']*4
    #c=0

    rect_width = 166
    rect_height = 300
    rect_thick = 5

    rect_x0 = (w / 2) - (rect_width / 2)
    rect_y0 = (h / 2) - (rect_height / 2)
    rect_x1 = (w / 2) + (rect_width / 2)
    rect_y1 = (h / 2) + (rect_height / 2)

    oval1 = None
    oval2 = None
    oval3 = None
    oval4 = None
    vehicle=None
    
# =============================================================================
#     image = tkinter.PhotoImage(file="C:\\Kshitij Aphale\\Study\\College\\IITJ\\Academics\\Sem 2\\Non Graded\\Engineering Design 2\\car image.png")
#     label = tkinter.Label(animation_window, image=image)
#     label.place(x=rect_x0,y=rect_y0)
# =============================================================================
    
    
    
    while(True):
       
        
        try:
            arduinodata1=None
            
            arduinodata1=arduino.readline()
            arduinodata = (str(arduinodata1[0:len(arduinodata1)].decode("utf-8")))
           
            
        except:
            continue
        
        print(arduinodata)
    
        dist=arduinodata.split(' ')
        for i in range(4):
            dist[i]=int(dist[i])
    

        
        window.update()
        canvas.delete(oval1)
        canvas.delete(oval2)
        canvas.delete(oval3)
        canvas.delete(oval4)
        canvas.delete(vehicle)
        time.sleep(0.001)

        for i in range(4):
            if((dist[i])>=200):
                colour[i]='green'
            elif ((dist[i]) < 200 and int(dist[i])>= 100):
                colour[i] = 'yellow'
            elif ((dist[i]) < 100):
                colour[i]= 'red'

        vehicle=canvas.create_rectangle(rect_x0, rect_y0, rect_x1, rect_y1, width=rect_thick)
        oval1 =canvas.create_oval(rect_x0 - 30 - ((dist[0])), rect_y0, rect_x0 - ((dist[0])), rect_y0 + 30 , fill=colour[0])
        oval2 =canvas.create_oval(rect_x1 + ((dist[1])), rect_y0, rect_x1 + ((dist[1])) + 30, rect_y0 + 30, fill=colour[1])
        oval3 =canvas.create_oval(rect_x0 - 30 - ((dist[2])), rect_y1 - 30, rect_x0 - ((dist[2])), rect_y1, fill=colour[2])
        oval4 =canvas.create_oval(rect_x1 + ((dist[3])), rect_y1 - 30, rect_x1 + ((dist[3])) + 30, rect_y1, fill=colour[3])
    
        
arduino=serial.Serial('COM4',9600)
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
try:
    animate(animation_window,animation_canvas)
    
except Exception as e:
    print(e)
    pass
    
        
        
arduino.close()

