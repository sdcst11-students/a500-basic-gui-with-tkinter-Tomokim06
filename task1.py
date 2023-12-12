import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("430x30")

box1 = tk.Entry(window,text="Entry widgets can be typed in", width=20)
text = tk.Label(window, text="X")
box2 = tk.Entry(window,text="Entry widgets can be typed in", width=20)
button = tk.Button(window,text="=", width=1, height=1)
box3 = tk.Entry(window,text="Entry widgets can be typed in", width=40)

box1.grid( row = 1, column = 1)
text.grid( row = 1, column = 2)
box2.grid( row = 1, column = 3)
button.grid( row = 1, column = 4)
box3.grid( row = 1, column = 5)

window.mainloop()

