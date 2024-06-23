from tkinter import *
global root
global stop
stop=False
global move
move=False
root = Tk()
root.geometry("500x500")
root.configure(bg="white")
S_Canvas = Canvas(root,width=500,height=500,bg="white")
S_Canvas.pack()
global x
x=150
global y
y=100
global z
z=100
global t
t=150

def draw(x,y,z,t):
    S_Canvas.create_oval(x, y, z, t, fill="lightblue",outline="lightblue",)
def callback(e):
    a=e.x
    b=e.y
    global move
    if b>y and b<t and a<x and a>z:
        xc=z+25
        yc=y+25



        move=True
        print(a,b)
    else:

        move=False



pas=-0.5
pas1=-0.5
while not stop:

    S_Canvas.delete("all")
    root.bind('<Motion>', callback)
    draw(x, y, z, t)
    if not move:

        y = y + pas

        t = t + pas
        if y <= 25:
            if x <= 50:
                pas1 = pas1 * -1
            if z >= 450:
                pas1 = pas1 * -1

            x = x + pas1

            z = z + pas1
        if t >= 475:
            if x <= 50:
                pas1 = pas1 * -1
            if z >= 450:
                pas1 = pas1 * -1

            x = x + pas1

            z = z + pas1
        if y<=1:
            pas = pas * -1
            if x<=50:
                pas1=pas1*-1

                x = x + pas1

                z = z + pas1
            elif z>=450:

                pas1 = pas1 * -1

                x = x + pas1

                z = z + pas1
            else:

                x = x + pas1

                z = z + pas1

        if t>=499:
            pas = pas * -1
            if x <= 50:
                pas1 = pas1 * -1

                x = x + pas1

                z = z + pas1
            elif z >= 450:
                pas1 = pas1 * -1

                x = x + pas1

                z = z + pas1
            else:

                x = x + pas1

                z = z + pas1
    root.update()
root.mainloop()



