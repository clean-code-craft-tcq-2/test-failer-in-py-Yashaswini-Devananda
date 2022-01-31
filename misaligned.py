def get_len_of_longest_item_in_string_list (string_list):
    len_of_longest_item = len(string_list[0])
    for x in string_list:
        if len(x) > len_of_longest_item:
            len_of_longest_item = len(x)
    return len_of_longest_item
    
def digit_count(num):
    quotient = 2
    digit_count = 0
    temp = num
    while (quotient >= 1 ):
        quotient = temp/10
        temp = quotient
        digit_count+=1
    return digit_count
 
color_code_pairs = []

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_pair_digit_count = digit_count(len(major_colors)*len(minor_colors))
    max_color_length_of_major_colors = get_len_of_longest_item_in_string_list(major_colors)
    max_color_length_of_minor_colors = get_len_of_longest_item_in_string_list(minor_colors)
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_code_pairs.append((f'{(i * 5 + j)+1 : >{color_pair_digit_count}} | {major : <{max_color_length_of_major_colors}} | {minor : <{max_color_length_of_minor_colors}}'))
            print(color_code_pairs[i * 5 + j])
    return len(major_colors) * len(minor_colors)

def test_alignment():
    last_num_pos = []
    first_separator_pos = []
    second_separator_pos = []
    for color_pair in color_code_pairs:
        got_first_separator = False
        for pos in range(len(color_pair)):
            # print (pos, color_pair[pos])
            if color_pair[pos] == "|":
                if got_first_separator == False:
                    first_separator_pos.append(pos)
                    if (first_separator_pos[0] != pos):
                        return False
                    got_first_separator = True
                else:
                    second_separator_pos.append(pos)
                    if (second_separator_pos[0] != pos):
                        return False
            if color_pair[len(color_pair)-1-pos].isnumeric():
                # print (pos, len(color_pair)-1-pos, color_pair[len(color_pair)-1-pos])
                last_num_pos.append(len(color_pair)-1-pos) 
                if (last_num_pos[0] != len(color_pair)-1-pos):
                    return False
                break
    # print(last_num_pos)         
    # print(first_separator_pos)         
    # print(second_separator_pos)    
    return True
    
result = print_color_map()
print("All is well (maybe!)\n")
test_alignment_result = test_alignment()
assert(test_alignment_result == True)
