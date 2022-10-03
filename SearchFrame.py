import tkinter as tk
from WidgetControls import *

class SearchFrame_Class(tk.Frame):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)   

        # tk.Entry(self, name='new_search_term', font=tkfont.Font(
        #     family="Arial", size=13)).grid(row=1, column=1, columnspan=2)
        tk.Button(self, name='search_button',underline=0, text='Search',  font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength = 90).grid(row=2, column=1)
        tk.Button(self, name='full_list', underline=0, text='Return to Full List',  font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength =90).grid(row=2, column=2)


        tk.Button(self, name='add_search_term', text='Add Search Term',  command=self.add_search_term, font=tkfont.Font(
                family="Arial", size=15), width=12, height=2, wraplength=140).grid(row=4, column=1)

        ListScrollEntryCombo(15, 15, tkfont.Font(
            family="Arial", size=15), None, self, name='search_terms_combo').grid(row=4, column=1, stick='news')

        ListScrollCombo(5, 15, tkfont.Font(
            family="Arial", size=15), None, 'Terms to Search For',self, name='search_terms').grid(row=4, column=2, stick='news')
        
    def Set_Focus_Search_Term(self):
        self.nametowidget('search_terms_combo').set_focus_entry()

    
    def Initialize_Word_List(self, word_list):
        self.nametowidget('search_terms_combo').add_item_list(word_list)

    def add_search_term(self):
        
        self.nametowidget('search_terms').add_one_item(
            self.nametowidget('search_terms_combo').get_selected_text())

    def Set_Full_List_Button(self, function):

        self.nametowidget('full_list').configure(command=function)

    def Set_Search_Button(self, function):

        self.nametowidget('search_button').configure(command=function)

    def Get_All_Search_Text(self):

        search_terms = self.nametowidget('search_terms').get_all_items()
        new_text = self.Get_Search_Text()
        if new_text not in search_terms:
            search_terms.append(new_text)

        return search_terms

    def Get_Search_Text(self):
        return_text = self.nametowidget('new_search_term').get()
        self.nametowidget('new_search_term').delete(0,tk.END)
        
        return return_text
