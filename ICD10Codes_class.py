from datetime import datetime
import copy
from dataclasses import dataclass
import pickle
import os
import re

@dataclass
class One_ICD10_Code():
    ICD10_Code:str
    description:str
    is_billable:bool
    category:str
    sub_category:str
    selected:bool

@dataclass
class One_Word():
    the_word:str
    the_categories:list[str]

class Simple_Code_Class():
    def __init__(self, code_string):
        self.code_string = code_string
        self.characters = [*code_string]

@dataclass
class One_Category():
    range_string:str
    lower_boundary: Simple_Code_Class
    upper_boundary: Simple_Code_Class
    description:str
    selected:bool
    expanded:bool
    category:str    


class Simple_Code_Class():
    def __init__(self, code_string):
        self.code_string = code_string
        self.characters = [*code_string]

def IsAGreaterThanB_ICD10code(A, B):

    if A.characters[0] > B.characters[0]:
        return True
    elif A.characters[0] < B.characters[0]:
        return False

    if A.characters[1] > B.characters[1]:
        return True
    elif A.characters[1] < B.characters[1]:
        return False

    if A.characters[2] <= B.characters[2]:
        return False

    return True

class All_Codes_Class():
    def __init__(self):

        self.all_codes = []
        self.categories = []
        self.sub_categories = []
        self.initial_word_list = []

    def set_sub_categories(self, these_sub_categories):
        self.sub_categories = these_sub_categories

    def set_categories(self, these_categories):
        self.categories=these_categories

    def set_codes(self, search_results):
        self.all_codes=search_results

    def set_initial_word_list(self, this_initial_word_list):
        self.initial_word_list = this_initial_word_list

    def Load_Big_Data(self):

        this_file = open('my_ICD10_file.txt', 'r')

        for one_line in this_file.readlines():
            this_code_data = one_line.replace('\n', '').split('@')
            self.all_codes.append(One_ICD10_Code(
                this_code_data[0], this_code_data[1], this_code_data[2] == '1', this_code_data[3], this_code_data[4], False))

        this_file.close()

        this_file = open('General_Categories.txt', 'r')

        for one_line in this_file.readlines():
            one_line_partitioned = one_line.replace('\n', '').partition('  ')
            range_partitioned = one_line_partitioned[0].partition('-')
            lower_boundary = Simple_Code_Class(range_partitioned[0])
            upper_boundary = Simple_Code_Class(range_partitioned[2])

            self.categories.append(One_Category(one_line_partitioned[
                0], lower_boundary, upper_boundary, one_line_partitioned[2], False, False, None))

        this_file.close()

        this_file = open('Subcategories.txt', 'r')

        for one_line in this_file.readlines():
            one_line_partitioned = one_line.replace('\n', '').partition('  ')
            range_partitioned = one_line_partitioned[0].partition('-')
            lower_boundary = Simple_Code_Class(range_partitioned[0])
            upper_boundary = Simple_Code_Class(range_partitioned[2])

            this_category = None
            for one_category in self.categories:
                if IsAGreaterThanB_ICD10code(lower_boundary, one_category.lower_boundary) or lower_boundary.code_string == one_category.lower_boundary.code_string:
                    if not IsAGreaterThanB_ICD10code(upper_boundary, one_category.upper_boundary):
                        this_category = one_category.range_string
                        break

            self.sub_categories.append(One_Category(one_line_partitioned[
                0], lower_boundary, upper_boundary, one_line_partitioned[2], False, None, this_category))

        this_file.close()

        this_file = open('initial_word_list.txt', 'r')

        for one_line in this_file.readlines():
            one_line = one_line.replace('\n', '')
            the_pieces = one_line.split(',')
            this_word = One_Word(the_pieces[0], the_pieces[1:])

            self.initial_word_list.append(this_word)

        self.initial_word_list.sort(key=lambda x: x.the_word)

        this_file.close()

    def Create_Initial_Word_List(self):
        possible_words = []

        preposition_file = open('Prepositions.txt','r')
        prepositions = []
        for one_line in preposition_file.readlines():
            prepositions.append(one_line.replace('\n',''))

        for one_code in self.all_codes:
            
            for one_word in one_code.description.split():
                one_word=re.sub('[().\%[\]\,]', '', one_word)

                if len(one_word)==0:
                    break

                while not one_word[0].isalnum() and len(one_word)>3:
                    one_word = one_word[1:]

                percent_alpha = len([x for x in one_word if x.isalpha()])/len(one_word)
                    
                one_word = one_word.lower()
                #this_word = ''.join(filter(str.isalpha, one_word)).lower()

                if one_word not in prepositions and len(one_word)>2 and one_word not in possible_words and percent_alpha>0.8:
                    possible_words.append(one_word)



        possible_words.sort()
        this_file=open('initial_word_list.txt','w')
        for one_word in possible_words:
            this_file.write(one_word)

            which_categories = [x.category for x in self.all_codes if one_word in x.description.lower()]
            which_categories = [*set(which_categories)]
            for one_category in which_categories:
                this_file.write(',' + one_category)

            this_file.write('\n')


        this_file.close()

    def Get_Words(self, which_categories=[]):

        if which_categories==[]:
            return [x.the_word for x in self.initial_word_list]

        return_list = []
        for one_category in which_categories:
            return_list = return_list + [x.the_word for x in self.initial_word_list if one_category in x.the_categories]

        return_list = [*set(return_list)]
        
        return_list.sort()
        
        return return_list
    
    def Search(self, search_terms):

        # selected_categories = [x.range_string for x in self.categories if x.selected]
        # selected_sub_categories = [
        #     x.range_string for x in self.sub_categories if x.selected]

        # with open('temporary_all_data.pkl', 'wb') as f:
        #     pickle.dump(self.all_codes, f)

        # if not selected_sub_categories==[] or not selected_categories==[]:
        #     self.all_codes = [x for x in self.all_codes if (x.category in selected_categories) or (x.sub_category in selected_sub_categories)]
        
        search_results = []

        list_to_search = [x for x in self.all_codes if x.selected]
        codes_in_list = []

        if list_to_search == []:
            list_to_search = self.all_codes

        for one_code in list_to_search:
            add_code=True
            for one_search_term in search_terms:
                if one_search_term.lower() not in one_code.description.lower():
                    add_code=False
                    break
            if add_code:
                search_results.append(one_code)
                codes_in_list.append(one_code.ICD10_Code)


        # with open('temporary_all_data.pkl', 'rb') as f:
        #     self.all_codes = pickle.load(f)

        # os.remove('temporary_all_data.pkl')

        these_categories = [x for x in self.categories if x.range_string in [
            y.category for y in search_results]]
        these_sub_categories = [x for x in self.sub_categories if x.range_string in [
            y.sub_category for y in search_results]]

        this_initial_word_list = [x for x in self.initial_word_list if not [
            y for y in x.the_categories if y in [z.range_string for z in these_categories]] == []]

        codes_added = []

        for one_code in codes_in_list:
            for index in reversed(range(3,len(one_code))):
                if not one_code[:index] in codes_in_list and not one_code[:index] in codes_added:
                    this_code = next(
                        (x for x in self.all_codes if x.ICD10_Code == one_code[:index]), None)
                    if not this_code==None:
                        search_results.append(this_code)
                        codes_added.append(this_code.ICD10_Code)

                

        search_results_objects = All_Codes_Class()
        search_results_objects.set_categories(these_categories)
        search_results_objects.set_sub_categories(these_sub_categories)
        search_results_objects.set_codes(search_results)
        search_results_objects.set_initial_word_list(this_initial_word_list)
            
        return search_results_objects


