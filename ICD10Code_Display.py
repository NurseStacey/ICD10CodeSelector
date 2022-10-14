from Colors import *


class One_Code_Line():
    def __init__(self, x_offset, tag, description, is_billable, selected, layer, expanded):

        self.tag = tag
        self.is_billable = is_billable
        self.description = description
        #normally I hate using one letter for a variable this but it's only cartesian coordinates anyway
        self.y1 = 0
        self.y2 = 0
        self.x_offset = x_offset
        self.expanded = expanded
        self.selected = selected
        self.layer = layer

class ICD10Code_DisplayClass():
    def __init__(self, The_Codes, The_Canvas, SearchFrame_Obj):

        self.The_Codes = The_Codes
        self.The_Canvas = The_Canvas
        self.SearchFrame_Obj = SearchFrame_Obj

        self.the_lines=[]
        self.The_Canvas.set_button_click_event(self.single_click)
        self.Create_Initial_Lines()


    def replace_codes(self, The_Codes):
        self.The_Codes = The_Codes
        self.the_lines = []
        self.Create_Initial_Lines()

    def Create_Initial_Lines(self):
        x_offset1 = 40
        for one_category in self.The_Codes.categories:

            self.the_lines.append(One_Code_Line(
                x_offset1, one_category.range_string, one_category.description, False, False, 'category', False))

    def find_tag_index(self, tag):
        
        for index in range(len(self.the_lines)):
            if self.the_lines[index].tag == tag:
                return index

    def Add_ICD10_Lines(self, tag, this_type):

        this_index = self.find_tag_index(tag)
        selected = self.the_lines[this_index].selected
        x_offset3 = self.the_lines[this_index].x_offset + 30 

        if this_type=='sub_category':
            length_to_compare=3
        else:
            length_to_compare = len(tag)+1

        new_codes = []

        codes_to_display = []
        if this_type == 'sub_category':
            codes_to_display = [x for x in self.The_Codes.all_codes if x.sub_category == tag and len(
                x.ICD10_Code) == length_to_compare]
        else:
            codes_to_display = [x for x in self.The_Codes.all_codes if x.ICD10_Code[:len(tag)] == tag and len(
                x.ICD10_Code) == length_to_compare]

        for one_ICD10_code in codes_to_display:

            try:
                upper_code = next(
                    x for x in new_codes if x in one_ICD10_code.ICD10_Code)
            except StopIteration:
                upper_code = None

            if upper_code == None:
                this_index += 1
            else:
                this_index = self.find_tag_index(upper_code)+1
                new_codes.remove(upper_code)

            if one_ICD10_code.selected == selected or one_ICD10_code.selected == None:
                one_ICD10_code.selected = None

                self.the_lines.insert(this_index, One_Code_Line(
                    x_offset3, one_ICD10_code.ICD10_Code, one_ICD10_code.description, one_ICD10_code.is_billable, selected, 'ICD10_Code', False))
            else:
                self.the_lines.insert(this_index, One_Code_Line(
                    x_offset3, one_ICD10_code.ICD10_Code, one_ICD10_code.description, one_ICD10_code.is_billable, one_ICD10_code.selected, 'ICD10_Code', False))

            new_codes.append(one_ICD10_code.ICD10_Code)


    def Remove_ICD10_Lines(self, subcategory, this_type):

        if this_type == 'sub_category':
            these_tags = [
                x.ICD10_Code for x in self.The_Codes.all_codes if x.sub_category == subcategory]
        else:
            these_tags = [
                x.ICD10_Code for x in self.The_Codes.all_codes if (subcategory in x.ICD10_Code and not subcategory==x.ICD10_Code)]

        self.the_lines = [x for x in self.the_lines if not x.tag in these_tags]

    def Remove_SubCategory_Lines(self, category):

        these_tags = [
            x.range_string for x in self.The_Codes.sub_categories if x.category == category]

        for one_line in [x for x in self.the_lines if x.tag in these_tags]:
            if one_line.expanded:
                self.Remove_ICD10_Lines(one_line.tag, 'sub_category')

        self.the_lines = [x for x in self.the_lines if not x.tag in these_tags]

    def Add_SubCategory_Lines(self, category):
        x_offset2 = 80

        index = 0
        for index in range(len(self.the_lines)):
            if self.the_lines[index].tag == category:
                selected = self.the_lines[index].selected
                break

        these_codes = [
            x for x in self.The_Codes.sub_categories if x.category == category]

        for one_sub_category in these_codes:
            index+=1

        
            if one_sub_category.selected==selected or one_sub_category.selected==None:
                one_sub_category.selected=None

                self.the_lines.insert(index, One_Code_Line(
                    x_offset2, one_sub_category.range_string, one_sub_category.description, False,selected, 'sub_category', False))
            else:
                self.the_lines.insert(index, One_Code_Line(
                    x_offset2, one_sub_category.range_string, one_sub_category.description, False,one_sub_category.selected, 'sub_category', False))

    def populate_screen_test(self):
        
        for index in range(1000):
            self.The_Canvas.Create_Dummy_Line(index*30)

    def Add_1000_dummy_lines(self):
        # self.test_index+=1
        # self.The_Canvas.delete('all')
        # for index in range(self.test_index*1000):
        #     self.The_Canvas.Create_Dummy_Line(index*30)

        # self.The_Canvas.configure(scrollregion=self.The_Canvas.bbox("all"))
        pass

    def get_number_rows(self):

        return len(self.the_lines)
        
    def populate_screen(self):

        self.The_Canvas.delete('all')
        next_y=10

        for index in range(len(self.the_lines)):
        #for one_line in self.the_lines:
            one_line = self.the_lines[index]   
            one_line.y1 = next_y
            self.The_Canvas.Add_Line(one_line, index+1)
            
            next_y = one_line.y2 +30

        # This is to update the scrolling region

        while next_y < 900:
            self.The_Canvas.Add_BlankLine(next_y)
            next_y += 30

        self.The_Canvas.configure(scrollregion=self.The_Canvas.bbox("all"))


    def ICD10_code_selected(self, this_tag, this_line, bg_tag):
        this_code = next(
            x for x in self.The_Codes.all_codes if x.ICD10_Code == this_tag)

        if this_line.selected:
            this_code.selected = False
            this_line.selected = False
            self.The_Canvas.itemconfig(
                bg_tag, fill=background_color)
        else:
            this_code.selected = True
            this_line.selected = True
            self.The_Canvas.itemconfig(bg_tag, fill=highlight_color)

        if this_line.selected:
            self.SearchFrame_Obj.Add_Category(this_code.category)
        else:
            self.SearchFrame_Obj.Remove_Category(this_code.category)

    def sub_category_selected(self, this_tag, this_line, bg_tag, type):

        if type=='sub_category':
            these_codes = [
                x for x in self.The_Codes.all_codes if x.sub_category == this_tag]
            these_lines = [ x for x in self.the_lines if x.tag in [y.ICD10_Code for y in these_codes]]

            this_code = next(
                x for x in self.The_Codes.sub_categories if x.range_string == this_tag)                
        else:
            these_codes = [
                x for x in self.The_Codes.all_codes if this_tag in x.ICD10_Code] 
            this_code = next(
                x for x in self.The_Codes.all_codes if x.ICD10_Code == this_tag)   
            these_lines = [x for x in self.the_lines if x.tag in [
                y.ICD10_Code for y in these_codes]]

        selected = True
        new_color = highlight_color

        if this_line.selected:
            selected = False
            new_color = background_color

        this_code.selected = selected
        this_line.selected = selected
        for y in range(this_line.y1, this_line.y2+1, 30):
            self.The_Canvas.itemconfig(
                bg_tag+str(y), fill=new_color)

        if this_line.expanded:
            for one_code in these_codes:

                this_one_code_line = next((x for x in these_lines if x.tag==one_code.ICD10_Code), None)

                if not this_one_code_line==None:
                    for y in range(this_one_code_line.y1, this_one_code_line.y2+1,30):
                        self.The_Canvas.itemconfig(
                            'bg'+one_code.ICD10_Code+str(y), fill=new_color)
            else:
                for one_icd10_code in [x for x in self.The_Codes.all_codes if x.sub_category == this_line.tag]:
                    one_icd10_code.expanded = None

    def category_selected(self, this_tag, this_line, bg_tag):
        

        these_codes = [
            x for x in self.The_Codes.sub_categories if x.category == this_tag]

        selected = True
        new_color = highlight_color
        this_code = next(
            x for x in self.The_Codes.categories if x.range_string == this_tag)

        if this_line.selected:
            selected = False
            new_color = background_color

        if selected:
            self.SearchFrame_Obj.Add_Category(this_tag)
        else:
            self.SearchFrame_Obj.Remove_Category(this_tag)
#        if this_line.selected:
#            this_line.selected = False
        for y in range(this_line.y1, this_line.y2+1, 30):
            self.The_Canvas.itemconfig(
                bg_tag+str(y), fill=new_color)

        this_line.selected = selected
        this_code.selected = selected
        if this_line.expanded:
            for one_code in these_codes:
                one_sub_category_line = next(
                    x for x in self.the_lines if x.tag == this_tag)
                self.The_Canvas.itemconfig(
                    'bg'+one_code.range_string, fill=new_color)
                one_code.selected = None
                one_sub_category_line.selected = selected

                if one_sub_category_line.expanded:
                    for one_icd10_code in [x for x in self.The_Codes.all_codes if x.sub_category == one_sub_category_line.tag]:
                        self.The_Canvas.itemconfig(
                            'bg'+one_icd10_code.range_string, fill=new_color)
                        one_icd10_code.selected = None
                        one_icd10_code_line = next(
                            x for x in self.the_lines if x.tag == this_tag)
                        one_icd10_code_line.selected = selected
        else:
            for one_code in these_codes:
                one_code.selected = None
                for one_icd10_code in [x for x in self.The_Codes.all_codes if x.sub_category == one_code.range_string]:
                    one_icd10_code.selected = None

    def plus_minus_process(self, tag_clicked):

        this_tag = tag_clicked.replace('plus_minus', '')
        this_line = next(x for x in self.the_lines if x.tag == this_tag)


        if this_line.layer == 'category':
            if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
                
                this_line.expanded = True
                self.Add_SubCategory_Lines(this_tag)
            else:
                this_line.expanded = False
                self.Remove_SubCategory_Lines(this_tag)
        elif this_line.layer == 'sub_category':
            this_code = next(
                    x for x in self.The_Codes.sub_categories if x.range_string == this_tag)  
            if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
                this_line.expanded = True
                self.Add_ICD10_Lines(this_tag, 'sub_category')
            else:
                this_line.expanded = False
                self.Remove_ICD10_Lines(this_tag, 'sub_category')
        else:
            this_code = next(
                x for x in self.The_Codes.all_codes if x.ICD10_Code == this_tag)
            if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
                this_line.expanded = True
                self.Add_ICD10_Lines(this_tag, 'icd10_code')
            else:
                this_line.expanded = False
                self.Remove_ICD10_Lines(this_tag, 'icd10_code')
        

        self.populate_screen()

    def expand_this_row(self, which_row):

        this_line = self.the_lines[which_row-1]
        tag = 'plus_minus{0}'.format(this_line.tag)
        self.plus_minus_process(tag)

    def select_this_row(self, which_row):
        this_line = self.the_lines[which_row-1]
        tag = 'code{0}'.format(this_line.tag)
        self.code_selected_proces(tag)

    def code_selected_proces(self, tag_clicked):
        this_tag = tag_clicked.replace('code', '')
        this_line = next(x for x in self.the_lines if x.tag == this_tag)
        bg_tag = tag_clicked.replace('code', 'bg')

        if this_line.layer == 'category':
            self.category_selected(this_tag, this_line, bg_tag)

        elif this_line.layer == 'sub_category':
            self.sub_category_selected(
                this_tag, this_line, bg_tag, 'sub_category')

        else:
            self.sub_category_selected(
                this_tag, this_line, bg_tag, 'ICD_10Code')


    def single_click(self, event):
        
        tag_clicked = self.get_tag(event)
        
        if tag_clicked==None:
            return

        if 'plus_minus' in tag_clicked:
            self.plus_minus_process(tag_clicked)
        elif 'code' in tag_clicked:
            self.code_selected_proces(tag_clicked)




    def get_tag(self, event):

        #figure out if something expandible was pressed

        for one_line in self.the_lines:
            if one_line.layer=='ICD10_Code' and one_line.is_billable:
                if (one_line.y1-5) < self.The_Canvas.canvasy(event.y) < (one_line.y2+18):
                    return 'code{0}'.format(one_line.tag)
            else:
                if (one_line.y1-5) < self.The_Canvas.canvasy(event.y) < (one_line.y2+18):
                    if (one_line.x_offset-10) <= event.x <= (one_line.x_offset+14):
                        return 'plus_minus{0}'.format(one_line.tag)
                    else:
                        return 'code{0}'.format(one_line.tag)

        return None
