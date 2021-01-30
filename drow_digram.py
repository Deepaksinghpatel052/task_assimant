from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

create_circle(100, 100, 20, myCanvas)
# create_circle(50, 25, 10, myCanvas)
myCanvas.create_line(100, 120, 130, 150)
create_circle(140, 160, 20, myCanvas)

myCanvas.create_line(140, 180, 200, 200)

create_circle(220, 200, 20, myCanvas)
myCanvas.create_line(240, 200, 290, 180)

create_circle(300, 170, 20, myCanvas)

myCanvas.create_line(310, 150, 320, 120)

myCanvas.create_line(120, 100, 300, 100)
create_circle(320, 100, 20, myCanvas)

root.mainloop()