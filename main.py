import tkinter as tk
from tkinter import ttk
import calculator 

root = tk.Tk()
root.title('Refraction Angle Calculator')

root.geometry('300x200+50+50')
root.resizable(False, False)

n1 = tk.StringVar()
n2 = tk.StringVar()
i1= tk.StringVar()

def clicked():
    try: 
        local_n1, local_n2, local_i1 = float(n1.get()), float(n2.get()), float(i1.get())
    except: 
        print('values affection error')
    ga = calculator.Main(local_n1, local_n2, local_i1)
    root.quit()
    
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)


n1_button = ttk.Label(frame, text="n1:")
n1_button.pack(fill='x', expand=True)

n1_entry = ttk.Entry(frame, textvariable=n1)
n1_entry.pack(fill='x', expand=True)


n2_button = ttk.Label(frame, text="n2:")
n2_button.pack(fill='x', expand=True)

n2_entry = ttk.Entry(frame, textvariable=n2)
n2_entry.pack(fill='x', expand=True)


i1_button = ttk.Label(frame, text="i1:")
i1_button.pack(fill='x', expand=True)

i1_entry = ttk.Entry(frame, textvariable=i1)
i1_entry.pack(fill='x', expand=True)


login_button = ttk.Button(frame, text="Submit", command=clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
