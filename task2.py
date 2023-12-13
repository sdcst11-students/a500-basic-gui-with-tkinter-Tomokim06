import tkinter as tk

window = tk.Tk()
window.title("T-Town veterinary Clinic Database ")
window.geometry("565x190")

dogphoto = tk.PhotoImage(file="dog.png")
button1 = tk.Button(window,text="Search by Name")
textbox = tk.Entry(window, width=20)
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Next >")
button4 = tk.Button(window, text="Save Entry")
label = tk.Label(window, image=dogphoto)

text1 = tk.Label(window, text="Name")
text2 = tk.Label(window, text="Type")
text3 = tk.Label(window, text="Breed")
text4 = tk.Label(window, text="Owner")
text5 = tk.Label(window, text="Birthdate")
clientdb = tk.Label(window, text="Client Database")
entry1 =tk.Entry(window, width=15)
entry2 =tk.Entry(window, width=15)
entry3 =tk.Entry(window, width=15)
entry4 =tk.Entry(window, width=15)
entry5 =tk.Entry(window, width=15)

button1.place(x=340, y=1)
button2.place(x=3, y=163)
button3.place(x=516, y=163)
button4.place(x= 230, y = 163)
textbox.place(x=440,y=1)
label.place(x=1, y=1)
clientdb.place(x= 220, y=50)

text1.place(x=35, y=100)
text2.place(x=138, y=100)
text3.place(x=245, y=100)
text4.place(x=355, y=100)
text5.place(x=465, y=100)

entry1.place(x=10, y=120)
entry2.place(x=111, y=120)
entry3.place(x=218, y=120)
entry4.place(x=335, y=120)
entry5.place(x=447, y=120)

window.mainloop()

