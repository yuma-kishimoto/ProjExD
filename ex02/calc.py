import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押された")

root = tk.Tk()
root.title("押すな")
root.geometry("300x500")

button = tk.Button(root,text ="0",width=4,height=2)
button.font = ("",30)
button.bind("<1>", button_click)
button.grid(10,0)
button.pack()
