import tkinter as tk
from WidgetControls import *
from ICD10Codes_class import *
from tkinter import font as tkfont
from ICD10Code_Display import *
from SearchFrame import *
from datetime import datetime

def test_nothing():
    ICD10Code_DisplayObj.Add_1000_dummy_lines()

def Raise_Full_List():
    ICD10Code_DisplayObj.populate_screen()
        
def Search_Button():
    the_times=[]
    #the_times.append(datetime.now())
    search_results = The_Codes.Search(
        SearchFrame_Obj.Get_Search_Text())
    #the_times.append(datetime.now())
    The_Canvas.Add_Search_Results(search_results)
    #the_times.append(datetime.now())
    # for one_time in the_times:
    #     print("Time:", one_time.strftime('%H:%M:%S.%f'))

The_Window = tk.Tk()
The_Window.title('ICD 10 Code Selector')

The_Canvas_Frame = ScrollingFrame(The_Window)
The_Canvas_Frame.grid(row=1, column=1, sticky='news')

The_Canvas = The_Canvas_Frame.canvas
The_Codes = All_Codes_Class()
ICD10Code_DisplayObj = ICD10Code_DisplayClass(The_Codes, The_Canvas)

ICD10Code_DisplayObj.populate_screen()
#ICD10Code_DisplayObj.populate_screen_test()

SearchFrame_Obj = SearchFrame_Class(The_Window)
SearchFrame_Obj.Set_Search_Button(Search_Button)
SearchFrame_Obj.Set_Full_List_Button(Raise_Full_List)


SearchFrame_Obj.grid(row=1, column=2, sticky='news')


The_Window.mainloop()



