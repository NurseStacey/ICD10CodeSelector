import tkinter as tk
from WidgetControls import *

class SearchFrame_Class(tk.Frame):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)   

        tk.Entry(self, name='new_search_term', font=tkfont.Font(
            family="Arial", size=13)).grid(row=1, column=1, columnspan=2)
        tk.Button(self, name='search_button', text='Search',  font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength = 90).grid(row=2, column=1)
        tk.Button(self, name='full_list', text='Return to Full List',  font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength =90).grid(row=2, column=2)

        ListScrollCombo(5, 15, tkfont.Font(
            family="Arial"), None,self,name='search_terms' ).grid(row=3, column=1)
        
        tk.Button(self, name='add_search_term', text='Add Search Term',  command=self.add_search_term, font=tkfont.Font(
                family="Arial", size=15), width=12, height=2, wraplength=110).grid(row=4, column=1)


    def add_search_term(self):
        self.nametowidget('search_terms').add_one_item(self.Get_Search_Text())

    def Set_Full_List_Button(self, function):

        self.nametowidget('full_list').configure(command=function)

    def Set_Search_Button(self, function):

        self.nametowidget('search_button').configure(command=function)

    def Get_Search_Text(self):

        temp = self.nametowidget('search_terms').get_all_items()
        return self.nametowidget('new_search_term').get()
