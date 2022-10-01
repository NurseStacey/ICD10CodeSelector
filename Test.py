from datetime import datetime
import copy
import sys
import pickle
from dataclasses import dataclass

@dataclass
class One_ICD10_Code():
    ICD10_Code:str
    description:str
    billable:bool
    category:str
    sub_category:str
    selected:bool
    expanded:bool

this_file = open('my_ICD10_file.txt','r')

the_data = []
the_data_2=[]

dict_labels = ['ICD10_Code', 'description', 'billable',
    'category', 'sub_category', 'selected', 'expanded']


for one_line in this_file.readlines():

    this_code_data = one_line.replace('\n', '').split('@')

    if len(this_code_data[0]) > 3:
        this_code_data[0] = this_code_data[0][:3] + \
            '.' + this_code_data[0][3:]

    the_data.append(dict(zip(dict_labels, [
                                this_code_data[0], this_code_data[1], this_code_data[2] == '1', this_code_data[3], this_code_data[4], None, False])))

    the_data_2.append(One_ICD10_Code(this_code_data[0], this_code_data[1], this_code_data[2] == '1', this_code_data[3], this_code_data[4], None, False))

copy_of_codes = copy.deepcopy(the_data)
search_string = 'urinate'
search_results_one = []

start_time = datetime.now()

original_length = len(the_data_2)
original_memory_size = sys.getsizeof(the_data_2)

# for index in range(len(search_string)):
#     search_results_one = search_results_one + \
#         [x for x in the_data_2 if search_string[:len(
#             search_string)-index].lower() in x.description.lower()]

#     the_data_2 = [x for x in the_data_2 if x not in search_results_one]
#     if (len(search_string)-index) == 5:
#          break

for index in range(len(search_string)):
    search_results_one = search_results_one + \
        [x for x in the_data_2 if search_string[:len(
            search_string)-index].lower() in x.description.lower() and x not in search_results_one]

    if (len(search_string)-index) == 5:
        break
    

# original_length=len(the_data)
# original_memory_size = sys.getsizeof(the_data)



# for index in range(len(search_string)):
#     search_results_one = search_results_one + \
#         [x for x in the_data if search_string[:len(
#             search_string)-index].lower() in x['description'].lower() and x not in search_results_one]

#     if (len(search_string)-index) == 5:
#         break

total_time =  datetime.now() - start_time

print("Total Time Difference : {} Milliseconds\n".format(total_time))
print("{} records".format(len(search_results_one)))

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

S06.816D
start_time = datetime.now()
with open('temporary_all_data.pkl', 'wb') as f:
    pickle.dump(the_data_2, f)
total_time =  datetime.now() - start_time
print("Total Time Difference for dump: {} Milliseconds\n".format(total_time))

start_time = datetime.now()
search_results_two = []
for index in range(len(search_string)):

    search_results_two = search_results_two + \
        [x for x in the_data_2 if search_string[:len(
            search_string)-index].lower() in x.description.lower()]

    the_data_2 = [x for x in the_data_2 if search_string[:len(
        search_string)-index].lower() not in x.description.lower()]

    if (len(search_string)-index) == 5:
        break

total_time = datetime.now() - start_time
print("Total Time Difference for search: {} Milliseconds\n".format(total_time))
start_time = datetime.now()

with open('temporary_all_data.pkl', 'rb') as f:
    the_data_2 = pickle.load(f)

total_time =  datetime.now() - start_time

print("Total Time Difference to reload : {} Milliseconds\n".format(total_time))
print("{} records".format(len(search_results_two)))

post_search_length=len(the_data)
post_search_memory_size = sys.getsizeof(the_data)

differences=[]
# for i in range(len(copy_of_codes)):
#     if not the_data[i]==copy_of_codes[i]:
#         differences.append(copy_of_codes)

# print("Size of original array = {}".format(original_memory_size))
# print("Length of original array = {}".format(original_length))
# print("Size of copied array after process = {}".format(
#     post_search_memory_size))
# print("Length of copied array after process = {}".format(
#     post_search_length))

# copy_of_codes = copy.deepcopy(the_data)
# print("Size of copied array before process = {}".format(sys.getsizeof(copy_of_codes)))
# print("Length copied array before process = {}".format(
#     len(copy_of_codes)))

if not differences==[]:
    print('differences')
else:
    print('no differences')
