import tkinter as tk
from WidgetControls import *

class SearchFrame_Class(tk.Frame):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.The_Codes = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)   

        self.which_categories = []
        # tk.Entry(self, name='new_search_term', font=tkfont.Font(
        #     family="Arial", size=13)).grid(row=1, column=1, columnspan=2)

        this_row=2
        tk.Button(self, name='search_button',underline=0, text='Search',  font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength = 90).grid(row=this_row, column=1, pady=5)
        tk.Button(self, name='full_list', underline=0, text='Return to Full List', command=self.clear_search_term, font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength=90).grid(row=this_row, column=2, pady=5)

        this_row += 1
        tk.Button(self, name='clear_list', underline=0, text='Clear Search Term List',  font=tkfont.Font(
            family="Arial", size=12), width=12, height=3, wraplength=90).grid(row=this_row, column=1, pady=5)

        tk.Button(self, name='add_search_term', underline=0, text='Add Search Term',  command=self.add_search_term, font=tkfont.Font(
            family="Arial", size=15), width=12, height=2, wraplength=140).grid(row=this_row, column=2, pady=5)

        this_row += 1


        ListScrollEntryCombo(15, 15, tkfont.Font(
            family="Arial", size=15), None, self, name='search_terms_combo').grid(row=this_row, column=1, stick='news', pady=5)

        
        ListScrollCombo(5, 15, tkfont.Font(
            family="Arial", size=15), None, 'Terms to Search For', self, name='search_terms').grid(row=4, column=2, stick='news', pady=5)
        
        self.nametowidget('search_terms_combo').set_double_click(
            self.add_search_term)

    def clear_search_term(self):
        self.nametowidget('search_terms').clear_listbox()

    def Set_Codes(self, The_Codes):
        self.The_Codes = The_Codes
        self.Initialize_Word_List(
            self.The_Codes.Get_Words(self.which_categories))

    def Set_Focus_Search_Term(self):
        self.nametowidget('search_terms_combo').set_focus_entry()
    
    def Initialize_Word_List(self, word_list):
        self.nametowidget('search_terms_combo').add_item_list(word_list)

    def add_search_term(self, e=None):
        
        self.nametowidget('search_terms').add_one_item(
            self.nametowidget('search_terms_combo').get_selected_text())

    def Set_Full_List_Button(self, function):

        self.nametowidget('full_list').configure(command=function)

    def Set_Search_Button(self, function):

        self.nametowidget('search_button').configure(command=function)

    def Get_All_Search_Text(self):

        search_terms = self.nametowidget('search_terms').get_all_items()

        return search_terms
    
    def set_word_list(self, word_list):
        self.nametowidget('search_terms_combo').add_item_list(word_list)

    def Add_Category(self, which_category):
        self.which_categories.append(which_category)
        self.Initialize_Word_List(
            self.The_Codes.Get_Words(self.which_categories))

    def Remove_Category(self, which_category):
        self.which_categories.remove(which_category)
        self.Initialize_Word_List(
            self.The_Codes.Get_Words(self.which_categories))

    def Get_Selected_Categories(self):
        return self.which_categories

