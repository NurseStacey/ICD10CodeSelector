import tkinter as tk
from WidgetControls import *
from ICD10Codes_class import *
from tkinter import font as tkfont
from ICD10Code_Display import *
from SearchFrame import *
from datetime import datetime
from tkinter import messagebox

def test_nothing():
    ICD10Code_DisplayObj.Add_1000_dummy_lines()

def Raise_Full_List():
    ICD10Code_DisplayObj.populate_screen()

def add_search_term(e):
    SearchFrame_Obj.add_search_term()

def Search_Button():
    the_times=[]
    #the_times.append(datetime.now())
    search_results = The_Codes.Search(
        SearchFrame_Obj.Get_All_Search_Text())
    #the_times.append(datetime.now())
    The_Canvas.Add_Search_Results(search_results)
    #the_times.append(datetime.now())
    # for one_time in the_times:
    #     print("Time:", one_time.strftime('%H:%M:%S.%f'))

def focus_search_entry(e):
    SearchFrame_Obj.Set_Focus_Search_Term()

def expand_mode(e):

    which_row=int(Canvas_Controls.nametowidget('row_entry').get())
    if which_row>ICD10Code_DisplayObj.get_number_rows():
        messagebox.showerror('Error', 'Please enter a smaller number for the row number.')
    
    if which_row<1:
        messagebox.showerror(
            'Error', 'Please enter a number greater than zero for the row number.')

def select_mode(e):
    pass

def only_digits(char):
    return char.isdigit()

The_Window = tk.Tk()
The_Window.title('ICD 10 Code Selector')

The_Canvas_Frame = ScrollingFrame(The_Window)
The_Canvas_Frame.grid(row=1, column=1, sticky='news')

The_Canvas = The_Canvas_Frame.canvas
The_Codes = All_Codes_Class()
#The_Codes.Create_Initial_Word_List()

ICD10Code_DisplayObj = ICD10Code_DisplayClass(The_Codes, The_Canvas)

ICD10Code_DisplayObj.populate_screen()
#ICD10Code_DisplayObj.populate_screen_test()

SearchFrame_Obj = SearchFrame_Class(The_Window)
SearchFrame_Obj.Set_Search_Button(Search_Button)
SearchFrame_Obj.Set_Full_List_Button(Raise_Full_List)
SearchFrame_Obj.Initialize_Word_List(The_Codes.Get_Words())

SearchFrame_Obj.grid(row=1, column=2, sticky='news')

Canvas_Controls = tk.Frame(The_Window)
Canvas_Controls.grid(row=2, column=1, sticky='news')

tk.Label(Canvas_Controls, text='Ctrl-e - Expand', fg=expand_color, font=tkfont.Font(
    family="Arial", size=20)).grid(padx=20,row=1, column=1, sticky='w')
tk.Label(Canvas_Controls, text='Ctrl-l - Select',
         fg=highlight_color,font=tkfont.Font(
             family="Arial", size=20)).grid(padx=20, row=2, column=1, sticky='w')

tk.Label(Canvas_Controls, text='Which_row', font=tkfont.Font(
    family="Arial", size=20)).grid(padx=20,row=1, column=2, sticky='w')          
validation = The_Window.register(only_digits)      
tk.Entry(Canvas_Controls, text='Ctrl-l - Select',validate='key', validatecommand=(validation, '%S'),
         fg=highlight_color,name='row_entry', font=tkfont.Font(
             family="Arial", size=20)).grid(padx=40, row=1, column=3, sticky='w')

w, h = The_Window.winfo_screenwidth(), The_Window.winfo_screenheight()
The_Window.geometry("%dx%d+0+0" % (w, h))

The_Window.bind('<Control-Key-t>', focus_search_entry)
The_Window.bind('<Control-Key-a>', add_search_term)
The_Window.bind('<Control-Key-s>', Search_Button)
The_Window.bind('<Control-Key-r>', Raise_Full_List)
The_Window.bind('<Control-Key-e>', expand_mode)
The_Window.bind('<Control-Key-l>', select_mode)

Canvas_Controls.nametowidget('row_entry').focus_set()

The_Window.mainloop()


