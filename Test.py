# from datetime import datetime
# import copy
# import sys
# import pickle
# from dataclasses import dataclass

# @dataclass
# class One_ICD10_Code():
#     ICD10_Code:str
#     description:str
#     billable:bool
#     category:str
#     sub_category:str
#     selected:bool
#     expanded:bool

# this_file = open('my_ICD10_file.txt','r')

# the_data = []
# the_data_2=[]

# dict_labels = ['ICD10_Code', 'description', 'billable',
#     'category', 'sub_category', 'selected', 'expanded']


# for one_line in this_file.readlines():

#     this_code_data = one_line.replace('\n', '').split('@')

#     if len(this_code_data[0]) > 3:
#         this_code_data[0] = this_code_data[0][:3] + \
#             '.' + this_code_data[0][3:]

#     the_data.append(dict(zip(dict_labels, [
#                                 this_code_data[0], this_code_data[1], this_code_data[2] == '1', this_code_data[3], this_code_data[4], None, False])))

#     the_data_2.append(One_ICD10_Code(this_code_data[0], this_code_data[1], this_code_data[2] == '1', this_code_data[3], this_code_data[4], None, False))

# copy_of_codes = copy.deepcopy(the_data)
# search_string = 'urinate'
# search_results_one = []

# start_time = datetime.now()

# original_length = len(the_data_2)
# original_memory_size = sys.getsizeof(the_data_2)

# # for index in range(len(search_string)):
# #     search_results_one = search_results_one + \
# #         [x for x in the_data_2 if search_string[:len(
# #             search_string)-index].lower() in x.description.lower()]

# #     the_data_2 = [x for x in the_data_2 if x not in search_results_one]
# #     if (len(search_string)-index) == 5:
# #          break

# for index in range(len(search_string)):
#     search_results_one = search_results_one + \
#         [x for x in the_data_2 if search_string[:len(
#             search_string)-index].lower() in x.description.lower() and x not in search_results_one]

#     if (len(search_string)-index) == 5:
#         break
    

# # original_length=len(the_data)
# # original_memory_size = sys.getsizeof(the_data)



# # for index in range(len(search_string)):
# #     search_results_one = search_results_one + \
# #         [x for x in the_data if search_string[:len(
# #             search_string)-index].lower() in x['description'].lower() and x not in search_results_one]

# #     if (len(search_string)-index) == 5:
# #         break

# total_time =  datetime.now() - start_time

# print("Total Time Difference : {} Milliseconds\n".format(total_time))
# print("{} records".format(len(search_results_one)))

# start_time = datetime.now()
# search_results_two = []

# copy_of_codes = copy.deepcopy(the_data_2)

# for index in range(len(search_string)):

#     search_results_two = search_results_two + \
#         [x for x in copy_of_codes if search_string[:len(
#             search_string)-index].lower() in x.description.lower()]

#     copy_of_codes = [x for x in copy_of_codes if x not in search_results_two]
#     if (len(search_string)-index) == 5:
#         break

# copy_of_codes = copy.deepcopy(the_data)

# for index in range(len(search_string)):

#     search_results_two = search_results_two + \
#         [x for x in copy_of_codes if search_string[:len(
#             search_string)-index].lower() in x['description'].lower()]

#     copy_of_codes = [x for x in copy_of_codes if x not in search_results_two]
#     if (len(search_string)-index) == 5:
#         break

from datetime import datetime

class Solution_two(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        return_value = []

        while num>=1000:
            return_value.append('M')
            num-=1000

        if num>=900:
            return_value.append('C')
            return_value.append('M')
            num-=900

        if num>=500:
            return_value.append('D')
            num -= 500

        if num >= 400:
            return_value.append('C')
            return_value.append('D')
            num -= 400

        while num>=100:
            return_value.append('C')
            num -= 100

        if num >= 90:
            return_value.append('X')
            return_value.append('C')
            num -= 90

        if num >= 50:
            return_value.append('L')
            num -= 50

        if num >= 40:
            return_value.append('X')
            return_value.append('L')
            num -= 40

        while num >= 10:
            return_value.append('X')
            num -= 10

        if num >= 9:
            return_value.append('I')
            return_value.append('X')
            num -= 9

        if num >= 5:
            return_value.append('V')
            num -= 5

        if num >= 4:
            return_value.append('I')
            return_value.append('V')
            num -= 4

        while num >= 1:
            return_value.append('I')
            num -= 1

        return ''.join(return_value)
        
    def romanToInt(self, s):

        this_dict ={}
        this_dict['A']=4
        this_dict['B']=9
        this_dict['C']=100
        this_dict['D']=500
        this_dict['E']=40
        this_dict['F']=90
        this_dict['I']=1
        this_dict['G']=400
        this_dict['H']=900
        this_dict['L']=50
        this_dict['M']=1000
        this_dict['V']=5
        this_dict['X']=10


        s=s.replace('IV', 'A')
        s=s.replace('IX', 'B')
        s=s.replace('XL', 'E')
        s=s.replace('XC', 'F')
        s=s.replace('CD', 'G')
        s = s.replace('CM', 'H')

        s_list = []
        s_list[:0] = s

        return sum ([this_dict[x] for x in s_list])

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """



        A_Ord = ord('A')
        the_chars =[0 for x in range(26)]
        the_chars[ord('I')-A_Ord]=1
        the_chars[ord('V')-A_Ord] = 5
        the_chars[ord('X')-A_Ord]=10
        the_chars[ord('L')-A_Ord]=50
        the_chars[ord('C')-A_Ord]=100
        the_chars[ord('D')-A_Ord] = 500
        the_chars[ord('M')-A_Ord] = 1000

        return_value = 0
        
        while not len(s)==0:
            

            which_position = len(s)-1
            if which_position==0:
                return_value += the_chars[ord(s[which_position])-A_Ord]
                return return_value

            this_char = s[which_position]
            this_char_index = ord(this_char)
            while s[which_position-1]==this_char:
                which_position -= 1
                if which_position==0:
                    break

            number_char=len(s)-which_position
            return_value += the_chars[this_char_index-A_Ord]*number_char

            if the_chars[ord(s[which_position-1])-A_Ord] < the_chars[this_char_index-A_Ord]:
                which_position -= 1
                return_value -= the_chars[ord(s[which_position])-A_Ord]

            s=s[:which_position]

        return return_value
    

start_time = datetime.now()
print("Begin Time:", start_time.strftime('%H:%M:%S.%f'))
print(str(Solution_two().intToRoman(1994)))
end_time = datetime.now()
print("Begin Time:", end_time.strftime('%H:%M:%S.%f'))
total_time = end_time-start_time
print("Total Time:", str(total_time))
