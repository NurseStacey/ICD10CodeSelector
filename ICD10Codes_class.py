
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
        dict_labels = ['ICD10_Code', 'description', 'billable', 'category', 'sub_category', 'selected', 'expanded']
        this_file = open('my_ICD10_file.txt','r')

        for one_line in this_file.readlines():
            
            this_code_data = one_line.replace('\n','').split('@')

            if len(this_code_data[0])>3:
                this_code_data[0] = this_code_data[0][:3] + '.' + this_code_data[0][3:]
                
            self.all_codes.append(dict(zip(dict_labels, [this_code_data[0], this_code_data[1], this_code_data[2] == '1',this_code_data[3], this_code_data[4],None, False ])))
            # one_code = ICD10_Code(this_code_data[0],this_code_data[2]=='1',this_code_data[1],int(this_code_data[3]))
            # self.all_codes.append(one_code)

        this_file.close()

        self.categories = []
        dict_labels = ['range_string', 'lower_boundary',
                       'upper_boundary', 'description', 'billable', 'selected']
        this_file = open('General_Categories.txt', 'r')

        for one_line in this_file.readlines():
            one_line_partitioned = one_line.replace('\n', '').partition('  ')
            range_partitioned = one_line_partitioned[0].partition('-')
            lower_boundary = Simple_Code_Class(range_partitioned[0])
            upper_boundary = Simple_Code_Class(range_partitioned[2])


            self.categories.append(
                dict(zip(dict_labels, [one_line_partitioned[0], lower_boundary, upper_boundary, one_line_partitioned[2],False, False])))

        this_file.close()

        dict_labels.append('category')

        self.sub_categories = []

        this_file = open('Subcategories.txt', 'r')

        for one_line in this_file.readlines():
            one_line_partitioned = one_line.replace('\n', '').partition('  ')
            range_partitioned = one_line_partitioned[0].partition('-')
            lower_boundary = Simple_Code_Class(range_partitioned[0])
            upper_boundary = Simple_Code_Class(range_partitioned[2])

            this_category=None
            for one_category in self.categories:
                if IsAGreaterThanB_ICD10code(lower_boundary, one_category['lower_boundary']) or lower_boundary.code_string == one_category['lower_boundary'].code_string:
                    if not IsAGreaterThanB_ICD10code(upper_boundary, one_category['upper_boundary']):
                        this_category = one_category['range_string']
                        break

            self.sub_categories.append(
                dict(zip(dict_labels, [one_line_partitioned[0], lower_boundary, upper_boundary, one_line_partitioned[2], False, None, this_category])))

        this_file.close()

    def Search(self, search_term):

        search_results = []

        for index in range(len(search_term)):

            search_results = search_results + \
                [x for x in self.all_codes if search_term[:len(
                    search_term)-index].lower() in x['description'].lower()]
            if (len(search_term)-index)==5:
                break

        return search_results


