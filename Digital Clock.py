import tkinter as tk
from time import strftime

def update_time():
   
    current_time = strftime('%H:%M:%S') 
    current_day = strftime('%A, %B %d, %Y') 
    l1.config(text=f"{current_time}\n{current_day}")
    l1.after(1000, update_time)


window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x150") 


l1 = tk.Label(window, font=("Arial",15, "bold"), bg="black", fg="white")
l1.pack(expand=True, fill="both")


update_time()


window.mainloop()