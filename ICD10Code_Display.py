from Colors import *

class One_Code_Line():
    def __init__(self, x_offset, tag, description, is_billable, selected, layer):

        self.tag = tag
        self.is_billable = is_billable
        self.description = description
        #normally I hate using one letter for a variable this but it's only cartesian coordinates anyway
        self.y = 0
        self.x_offset = x_offset
        self.expanded = False
        self.selected = selected
        self.layer = layer

class ICD10Code_DisplayClass():
    def __init__(self, The_Codes, The_Canvas):

        self.The_Codes = The_Codes
        self.The_Canvas = The_Canvas
        self.the_lines=[]
        self.The_Canvas.set_button_click_event(self.single_click)
        self.Create_Initial_Lines()


    def Create_Initial_Lines(self):
        x_offset1 = 10
        for one_category in self.The_Codes.categories:

            self.the_lines.append(One_Code_Line(
                x_offset1, one_category['range_string'], one_category['description'], False, False, 'category'))

    def Add_ICD10_Lines(self, subcategory):
        x_offset3 = 90

        index = 0
        for index in range(len(self.the_lines)):
            if self.the_lines[index].tag == subcategory:
                selected = self.the_lines[index].selected
                break

        these_codes = [
            x for x in self.The_Codes.all_codes if x['sub_category'] == subcategory]

        for one_ICD10_code in these_codes:
            index += 1

            if one_ICD10_code['selected'] == selected or one_ICD10_code['selected'] == None:
                one_ICD10_code['selected'] = None

                self.the_lines.insert(index, One_Code_Line(
                    x_offset3, one_ICD10_code['ICD10_Code'], one_ICD10_code['description'], one_ICD10_code['billable'], selected, 'ICD10_Code'))
            else:
                self.the_lines.insert(index, One_Code_Line(
                    x_offset3, one_ICD10_code['ICD10_Code'], one_ICD10_code['description'], one_ICD10_code['billable'], one_ICD10_code['selected'], 'ICD10_Code'))


    def Remove_ICD10_Lines(self, subcategory):

        these_tags = [
            x['ICD10_Code'] for x in self.The_Codes.all_codes if x['sub_category'] == subcategory]

        self.the_lines = [x for x in self.the_lines if not x.tag in these_tags]

    def Remove_SubCategory_Lines(self, category):

        these_tags = [
            x['range_string'] for x in self.The_Codes.sub_categories if x['category'] == category]

        for one_line in [x for x in self.the_lines if x.tag in these_tags]:
            if one_line.expanded:
                self.Remove_ICD10_Lines(one_line.tag)

        self.the_lines = [x for x in self.the_lines if not x.tag in these_tags]

    def Add_SubCategory_Lines(self, category):
        x_offset1 = 10
        x_offset2 = 50
        x_offset3 = 90

        
        index = 0
        for index in range(len(self.the_lines)):
            if self.the_lines[index].tag == category:
                selected = self.the_lines[index].selected
                break

        these_codes = [
            x for x in self.The_Codes.sub_categories if x['category'] == category]

        for one_sub_category in these_codes:
            index+=1

        
            if one_sub_category['selected']==selected or one_sub_category['selected']==None:
                one_sub_category['selected']=None

                self.the_lines.insert(index, One_Code_Line(
                    x_offset2, one_sub_category['range_string'], one_sub_category['description'], False,selected, 'sub_category'))
            else:
                self.the_lines.insert(index, One_Code_Line(
                    x_offset2, one_sub_category['range_string'], one_sub_category['description'], False,one_sub_category['selected'], 'sub_category'))

    def populate_screen(self):

        y=10

        for one_line in self.the_lines:
            
            one_line.y = y
            #self.The_Canvas.Add_Line(one_line.tag,one_line.description, one_line.x_offset, y, one_line.expanded,one_line.selected)
            self.The_Canvas.Add_Line(one_line)
            
            y+=30

        # This is to update the scrolling region

        while y<900:
            self.The_Canvas.Add_BlankLine(y)
            y+=30

        self.The_Canvas.configure(scrollregion=self.The_Canvas.bbox("all"))

    def ICD10_code_selected(self, this_tag, this_line, bg_tag):
        this_code = next(
            x for x in self.The_Codes.all_codes if x['ICD10_Code'] == this_tag)

        if this_line.selected:
            this_code['selected'] = False
            this_line.selected = False
            self.The_Canvas.itemconfig(
                bg_tag, fill=get_color('AntiqueWhite'))
        else:
            this_code['selected'] = True
            this_line.selected = True
            self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))

    def sub_category_selected(self, this_tag, this_line, bg_tag):

        these_codes = [
            x for x in self.The_Codes.all_codes if x['sub_category'] == this_tag]

        this_codes = next(
            x for x in self.The_Codes.sub_categories if x['range_string'] == this_tag)

        selected = True
        new_color = 'Gold'

        if this_line.selected:
            selected = False
            new_color = 'AntiqueWhite'
            
        this_codes['selected'] = selected
        this_line.selected = selected
        self.The_Canvas.itemconfig(
            bg_tag, fill=get_color(new_color))
        if this_line.expanded:
            for one_code in these_codes:
                self.The_Canvas.itemconfig(
                    'bg'+one_code['ICD10_Code'], fill=get_color(new_color))
            else:
                for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == this_line.tag]:
                    one_icd10_code['expanded'] = None
        # else:
        #     this_codes['selected'] = True
        #     this_line.selected = True
        #     self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))
        #     if this_line.expanded:
        #         for one_code in these_codes:
        #             self.The_Canvas.itemconfig(
        #                 'bg'+one_code['ICD10_Code'], fill=get_color('Gold'))
        #         else:
        #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == this_line.tag]:
        #                 one_icd10_code.expanded = None  

    def category_selected(self, this_tag, this_line, bg_tag):

        these_codes = [
            x for x in self.The_Codes.sub_categories if x['category'] == this_tag]

        selected = True
        new_color = 'Gold'

        if this_line.selected:
            selected = False
            new_color = 'AntiqueWhite'

#        if this_line.selected:
#            this_line.selected = False
        self.The_Canvas.itemconfig(
            bg_tag, fill=get_color(new_color))

        this_line.selected = selected

        if this_line.expanded:
            for one_code in these_codes:
                one_sub_category_line = next(
                    x for x in self.the_lines if x.tag == this_tag)
                self.The_Canvas.itemconfig(
                    'bg'+one_code['range_string'], fill=get_color(new_color))
                one_code['selected'] = None
                one_sub_category_line.selected = selected

                if one_sub_category_line.expanded:
                    for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code.tag]:
                        self.The_Canvas.itemconfig(
                            'bg'+one_icd10_code['range_string'], fill=get_color(new_color))
                        one_icd10_code['selected'] = None
                        one_icd10_code_line = next(
                            x for x in self.the_lines if x.tag == this_tag)
                        one_icd10_code_line.selected = selected
        else:
            for one_code in these_codes:
                one_code['selected'] = None
                for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code['range_string']]:
                    one_icd10_code['selected'] = None
        # else:
        #     this_line.selected = True
        #     self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))

        #     if this_line.expanded:

        #         for one_code in these_codes:
        #             one_sub_category_line = next(
        #                 x for x in self.the_lines if x.tag == this_tag)
        #             self.The_Canvas.itemconfig(
        #                 'bg'+one_code['range_string'], fill=get_color('Gold'))
        #             one_code['selected'] = None
        #             one_sub_category_line.selected = True

        #             if one_sub_category_line.expanded:
        #                 for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code.tag]:
        #                     self.The_Canvas.itemconfig(
        #                         'bg'+one_icd10_code['range_string'], fill=get_color('Gold'))
        #                 one_icd10_code['selected'] = None
        #                 one_icd10_code_line = next(
        #                     x for x in self.the_lines if x.tag == this_tag)
        #                 one_icd10_code_line.selected = False
        #     else:
        #         for one_code in these_codes:
        #             one_code['selected'] = None
        #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code['range_string']]:
        #                 one_icd10_code['selected'] = None

    def plus_minus_process(self, tag_clicked):

        this_tag = tag_clicked.replace('plus_minus', '')
        this_line = next(x for x in self.the_lines if x.tag == this_tag)

        if this_line.layer == 'category':
            if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
                #self.The_Canvas.itemconfig(tag_clicked, text='-')
                this_line.expanded = True
                self.Add_SubCategory_Lines(this_tag)
            else:
                #self.The_Canvas.itemconfig(tag_clicked, text='+')
                this_line.expanded = False
                self.Remove_SubCategory_Lines(this_tag)
        else:
            if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
                #self.The_Canvas.itemconfig(tag_clicked, text='-')
                this_line.expanded = True
                self.Add_ICD10_Lines(this_tag)
            else:
                #self.The_Canvas.itemconfig(tag_clicked, text='+')
                this_line.expanded = False
                self.Remove_ICD10_Lines(this_tag)

        self.The_Canvas.delete('all')

        self.populate_screen()

    def single_click(self, event):
        
        tag_clicked = self.get_tag(event)
        
        if tag_clicked==None:
            return

        if 'plus_minus' in tag_clicked:
            self.plus_minus_process(tag_clicked)
            # this_tag = tag_clicked.replace('plus_minus', '')
            # this_line = next(x for x in self.the_lines if x.tag==this_tag)

            # if this_line.layer=='category':
            #     if self.The_Canvas.itemcget(tag_clicked, 'text')=='+':
            #         #self.The_Canvas.itemconfig(tag_clicked, text='-')
            #         this_line.expanded=True
            #         self.Add_SubCategory_Lines(this_tag)
            #     else:
            #         #self.The_Canvas.itemconfig(tag_clicked, text='+')
            #         this_line.expanded =False
            #         self.Remove_SubCategory_Lines(this_tag)
            # else:
            #     if self.The_Canvas.itemcget(tag_clicked, 'text') == '+':
            #         #self.The_Canvas.itemconfig(tag_clicked, text='-')
            #         this_line.expanded = True
            #         self.Add_ICD10_Lines(this_tag)
            #     else:
            #         #self.The_Canvas.itemconfig(tag_clicked, text='+')
            #         this_line.expanded = False
            #         self.Remove_ICD10_Lines(this_tag)

            # self.The_Canvas.delete('all')
            
            # self.populate_screen()
        elif 'code' in tag_clicked:

            this_tag = tag_clicked.replace('code', '')
            this_line = next(x for x in self.the_lines if x.tag == this_tag)
            bg_tag = tag_clicked.replace('code', 'bg')

            if this_line.layer=='category':
                self.category_selected(this_tag, this_line, bg_tag)
                # these_codes = [
                #     x for x in self.The_Codes.sub_categories if x['category'] == this_tag]

                
                # if this_line.selected:
                #     this_line.selected = False
                #     self.The_Canvas.itemconfig(
                #         bg_tag, fill=get_color('AntiqueWhite'))

                #     if this_line.expanded:
                #         for one_code in these_codes:
                #             one_sub_category_line = next(x for x in self.the_lines if x.tag == this_tag)
                #             self.The_Canvas.itemconfig(
                #                 'bg'+one_code['range_string'], fill=get_color('AntiqueWhite'))
                #             one_code['selected'] = None
                #             one_sub_category_line.selected = False

                #             if one_sub_category_line.expanded:
                #                 for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code.tag]:
                #                     self.The_Canvas.itemconfig(
                #                         'bg'+one_icd10_code['range_string'], fill=get_color('AntiqueWhite'))
                #                     one_icd10_code['selected'] = None
                #                     one_icd10_code_line = next(
                #                         x for x in self.the_lines if x.tag == this_tag)
                #                     one_icd10_code_line.selected = False
                #     else:
                #         for one_code in these_codes:
                #             one_code['selected'] = None
                #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code['range_string']]:
                #                 one_icd10_code['selected'] = None
                
                # else:
                #     this_line.selected = True
                #     self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))

                #     if this_line.expanded:
                        
                #         for one_code in these_codes:
                #             one_sub_category_line = next(x for x in self.the_lines if x.tag == this_tag)
                #             self.The_Canvas.itemconfig(
                #                 'bg'+one_code['range_string'], fill=get_color('Gold'))
                #             one_code['selected'] = None
                #             one_sub_category_line.selected = True

                #             if one_sub_category_line.expanded:
                #                 for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code.tag]:
                #                     self.The_Canvas.itemconfig('bg'+one_icd10_code['range_string'], fill=get_color('Gold'))
                #                 one_icd10_code['selected'] = None
                #                 one_icd10_code_line = next(
                #                     x for x in self.the_lines if x.tag == this_tag)
                #                 one_icd10_code_line.selected = False
                #     else:
                #         for one_code in these_codes:
                #             one_code['selected'] = None
                #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == one_code['range_string']]:
                #                 one_icd10_code['selected'] = None

            elif this_line.layer=='sub_category':
                self.sub_category_selected(this_tag, this_line, bg_tag)
                # these_codes = [
                #     x for x in self.The_Codes.all_codes if x['sub_category'] == this_tag]
                
                # this_codes = next(
                #     x for x in self.The_Codes.sub_categories if x['range_string'] == this_tag)

                
                # if this_line.selected:
                #     this_codes['selected']=False
                #     this_line.selected = False
                #     self.The_Canvas.itemconfig(
                #         bg_tag, fill=get_color('AntiqueWhite'))
                #     if this_line.expanded:
                #         for one_code in these_codes:
                #             self.The_Canvas.itemconfig(
                #                 'bg'+one_code['ICD10_Code'], fill=get_color('AntiqueWhite'))
                #         else:
                #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category']==this_line.tag]:
                #                 one_icd10_code['expanded'] = None
                # else:
                #     this_codes['selected']=True
                #     this_line.selected = True
                #     self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))
                #     if this_line.expanded:
                #         for one_code in these_codes:
                #             self.The_Canvas.itemconfig(
                #                 'bg'+one_code['ICD10_Code'], fill=get_color('Gold'))
                #         else:
                #             for one_icd10_code in [x for x in self.The_Codes.all_codes if x['sub_category'] == this_line.tag]:
                #                 one_icd10_code.expanded = None
            else:
                self.ICD10_code_selected(this_tag, this_line, bg_tag)
                # this_code = next(
                #     x for x in self.The_Codes.all_codes if x['ICD10_Code'] == this_tag)

                # if this_line.selected:
                #     this_code['selected'] = False
                #     this_line.selected = False
                #     self.The_Canvas.itemconfig(
                #         bg_tag, fill=get_color('AntiqueWhite'))
                # else:
                #     this_code['selected'] = True
                #     this_line.selected = True
                #     self.The_Canvas.itemconfig(bg_tag, fill=get_color('Gold'))

    def get_tag(self, event):

        x_coordinate = event.x
        y_coordinate = event.y

        #figure out if something expandible was pressed

        for one_line in self.the_lines:
            if one_line.layer=='ICD10_Code':
                if (one_line.y-5) < self.The_Canvas.canvasy(y_coordinate) < (one_line.y+18):
                    return 'code{0}'.format(one_line.tag)
            else:
                if (one_line.y-5) < self.The_Canvas.canvasy(y_coordinate) < (one_line.y+18):
                    if (one_line.x_offset-10) <= x_coordinate <= (one_line.x_offset+14):
                        return 'plus_minus{0}'.format(one_line.tag)
                    else:
                        return 'code{0}'.format(one_line.tag)

            # if (one_line.x_offset+10) <= x_coordinate <= (one_line.x_offset+95):
            #     if (one_line.y-5) < self.The_Canvas.canvasy(y_coordinate) < (one_line.y+18):
                    

        return None
