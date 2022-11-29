import tkinter as tk
import tkinter.messagebox as tkm
import math

def button_click(event):
    btn = event.widget
    i = btn["text"]
    siki=entry.get()

    if len(siki) >= 14:
        entry.delete(0, tk.END)
        entry.insert(0,"Error")

    elif i == "=":
        siki=entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    elif i == "C":
        entry.delete(0, tk.END)

    elif i == "√":
        siki=entry.get()
        res = math.sqrt(eval(siki))
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    elif i == "**2":
        siki= eval(entry.get())
        res = siki*siki
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    else:
        entry.insert(tk.END, i)

root = tk.Tk()
root.geometry("400x600")

entry=tk.Entry(root, justify="right", width = 10, font = ("",40))
entry.grid(row = 0, column=0, columnspan=4,sticky=tk.W+tk.E)

r = 1
c = 0
kei = ["**2","√","C"]

for Q in kei:
    button = tk.Button(root, text = f"{Q}", width=4, height=2, font = ("", 30))
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

r = 2
c = 0

for i in range(9,-1,-1):
    button = tk.Button(root, text = f"{i}", width=4, height=2, font = ("", 30))
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

A = 1
B = 5
KEI = [".","%","="]

for C in KEI:
    button = tk.Button(root, text = f"{C}", width=4, height=2, font = ("", 30))
    button.grid(row = B, column = A)
    button.bind("<1>",button_click)
    A += 1
 

n = 1
m = 3
ope = ["/", "*","-","+"]

for w in ope:
    button = tk.Button(root, text = f"{w}", width=4, height=2, font = ("", 30))
    button.grid(row = n, column = m)
    button.bind("<1>",button_click)
    m += 1
    if m % 3 == 1:
        n += 1
        m = 3


root.mainloop()
