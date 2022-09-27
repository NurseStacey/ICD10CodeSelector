import tkinter as tk
from WidgetControls import *
from ICD10Codes_class import *
from tkinter import font as tkfont
from ICD10Code_Display import *
from SearchFrame import *

def Search_Button():
    search_results = The_Codes.Search(SearchFrame_Obj.Get_Search_Text())
    
    The_Canvas.Add_Search_Results(search_results)

The_Window = tk.Tk()
The_Window.title('ICD 10 Code Selector')

The_Canvas_Frame = ScrollingFrame(The_Window)
The_Canvas_Frame.grid(row=1, column=1, sticky='news')

The_Canvas = The_Canvas_Frame.canvas
The_Codes = All_Codes_Class()
ICD10Code_DisplayObj = ICD10Code_DisplayClass(The_Codes, The_Canvas)

ICD10Code_DisplayObj.populate_screen()

SearchFrame_Obj = SearchFrame_Class(The_Window)
SearchFrame_Obj.Set_Search_Button(Search_Button)

SearchFrame_Obj.grid(row=1, column=2, sticky='news')


The_Window.mainloop()



