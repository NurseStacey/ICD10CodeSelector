#this is only for building my_ICD10_file.txt




class One_Code_Class():
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

    if A.characters[2] < B.characters[2]:
        return False

    return True

categories = []
dict_labels = ['range_string', 'lower_boundary',
                'upper_boundary', 'description', 'billable', 'selected']
#this_file = open('General_Categories.txt', 'r')

# for one_line in this_file.readlines():
#     one_line_partitioned = one_line.replace('\n', '').partition('  ')
#     range_partitioned = one_line_partitioned[0].partition('-')
#     lower_boundary = One_Code_Class(range_partitioned[0])
#     upper_boundary = One_Code_Class(range_partitioned[2])

#     categories.append(
#         dict(zip(dict_labels, [one_line_partitioned[0], lower_boundary, upper_boundary, one_line_partitioned[2], False, False])))

# this_file.close()


# sub_categories = []
# dict_labels = ['range_string', 'lower_boundary',
#                'upper_boundary', 'description', 'category']
# this_file = open('Subcategories.txt', 'r')

# for one_line in this_file.readlines():
#     one_line_partitioned = one_line.replace('\n', '').partition('  ')
#     range_partitioned = one_line_partitioned[0].partition('-')
#     lower_boundary = One_Code_Class(range_partitioned[0])
#     upper_boundary = One_Code_Class(range_partitioned[2])

#     this_category = None
#     last_category = categories[0]
#     for one_category in categories:
        
#         #if (not IsAGreaterThanB_ICD10code(lower_boundary, one_category['lower_boundary'])) or lower_boundary.code_string == one_category['lower_boundary'].code_string:
#         if not IsAGreaterThanB_ICD10code(lower_boundary, one_category['lower_boundary']):
#             #if not IsAGreaterThanB_ICD10code(upper_boundary, one_category['upper_boundary']):
#             #this_category = last_category['range_string']
#             break
#         else:
#             last_category = one_category

#     this_category = last_category['range_string']
#     sub_categories.append(
#         dict(zip(dict_labels, [one_line_partitioned[0], lower_boundary, upper_boundary, one_line_partitioned[2], this_category])))

# this_file.close()

# all_codes = []
# dict_labels = ['order', 'ICD10Code_String',
#                'Billable', 'Abbreviation', 'Description']
# this_file = open('icd10cm_order_2022.txt', 'r')

# # counter=0
# for one_line in this_file.readlines():
#     positions_to_partition_on=[0,5,14,16,77,len(one_line)]
#     one_code_element = [one_line.replace('\n','')[x:y] for x, y in zip(
#         positions_to_partition_on, positions_to_partition_on[1:])]
#     one_code_element = [x.strip() for x in one_code_element]
#     one_code_element = dict(zip(dict_labels, one_code_element))
#     one_code_element['ICD10Code'] = One_Code_Class(
#         one_code_element['ICD10Code_String'])

#     #one_code_element['Category'] = len(sub_categories)-1
#     last_sub_category=sub_categories[0]
#     for one_sub_category in sub_categories:
#         if not IsAGreaterThanB_ICD10code(one_code_element['ICD10Code'], one_sub_category['lower_boundary']):
#             #if not IsAGreaterThanB_ICD10code(one_code_element['ICD10Code'], one_sub_category['upper_boundary']):
#             # one_code_element['sub_category'] = last_sub_category['range_string']
#             # one_code_element['category'] = last_sub_category['category']
#             break
#         else:
#             last_sub_category = one_sub_category

#     one_code_element['sub_category'] = last_sub_category['range_string']
#     one_code_element['category'] = last_sub_category['category']
#     all_codes.append(one_code_element)
#     # counter += 1
#     # if counter==1000:
#     #     break

# this_file = open('my_ICD10_file.txt', 'w')

# for one_code in all_codes:
#     this_file.write(one_code['ICD10Code_String'] + '@')
#     this_file.write(one_code['Description'] + '@')
#     this_file.write(one_code['Billable'] + '@')
#     this_file.write(one_code['category'] + '@')
#     this_file.write(one_code['sub_category'] + '\n')

# this_file.close()


    