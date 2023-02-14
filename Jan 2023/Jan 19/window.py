
import tkinter as tk

window = tk.Tk()

window.geometry("300x300")
label = tk.Label(text="This is an window to the world.", font=("Helvetica", 12, "bold"))
label.place(x=30, y=100)

window.mainloop()