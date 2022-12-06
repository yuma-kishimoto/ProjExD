import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy,mx,my
    if key == "Up": 
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[mx][my] == 1:
        if key == "Up": 
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1

    cx, cy = mx*50 + 25, my*50 + 25

    ax = 1275
    ay = 625
    canvas.coords("Tori", cx, cy)
    canvas.coords("Tori2", ax, ay)
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    

    maze_lst = mm.make_maze(27, 14)
    mm.show_maze(canvas, maze_lst)

    mx,my = 1,1
    cx, cy = mx*50 + 25, my*50 + 25

    ax = 1275
    ay = 625
    
    Tori = tk.PhotoImage(file="fig/8mini.png")
    Tori2 = tk.PhotoImage(file="fig/6mini.png")
    
    canvas.create_image(ax, ay, image=Tori2, tag="Tori2")
    canvas.create_image(cx, cy, image=Tori, tag="Tori")
    
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)


    main_proc()
    root.mainloop()