import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import calculator 
import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self):
        np.random.seed(1)
        x = 4 + np.random.normal(0, 1.5, 200)

        fig, ax = plt.subplots()
        ax.ecdf(x)
        plt.show()

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Refraction Angle Calculator')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry('300x300')
        self.root.resizable(False, False)

        self.n1 = ctk.StringVar()
        self.n2 = ctk.StringVar()
        self.i1= ctk.StringVar()



    def clicked(self):
        try:
            local_n1, local_n2, local_i1 = float(self.n1.get()), float(self.n2.get()), float(self.i1.get())
        except:
            print('values affection error')
        ga = calculator.Main(local_n1, local_n2, local_i1)
        self.root.quit()
    
    def __run__(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(padx=10, pady=10, fill='x', expand=True)

        n1_button = ctk.CTkLabel(frame, text="n1:")
        n1_button.pack(fill='x', expand=True)

        n1_entry = ctk.CTkEntry(frame, textvariable=self.n1)
        n1_entry.pack(fill='x', expand=True)


        n2_button = ctk.CTkLabel(frame, text="n2:")
        n2_button.pack(fill='x', expand=True)

        n2_entry = ctk.CTkEntry(frame, textvariable=self.n2)
        n2_entry.pack(fill='x', expand=True)


        i1_button = ctk.CTkLabel(frame, text="i1:")
        i1_button.pack(fill='x', expand=True)

        i1_entry = ctk.CTkEntry(frame, textvariable=self.i1)
        i1_entry.pack(fill='x', expand=True)


        submit = ctk.CTkButton(frame, text="Submit", command=self.clicked)
        submit.pack(fill='x', expand=True, pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.__run__()
