import tkinter as tk
from WidgetControls import *

class SearchFrame_Class(tk.Frame):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)   

        tk.Entry(self, name='search_term', font=tkfont.Font(
            family="Arial", size=13)).grid(row=1, column=1)
        tk.Button(self, name='search_button', text='Search',  font=tkfont.Font(
            family="Arial", size=13)).grid(row=2, column=1)

    def Set_Search_Button(self, function):

        self.nametowidget('search_button').configure(command=function)

    def Get_Search_Text(self):

        return self.nametowidget('search_term').get()