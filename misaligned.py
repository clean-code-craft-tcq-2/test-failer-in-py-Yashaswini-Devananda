color_code_pairs = []
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_code_pairs.(f'{i * 5 + j} | {major} | {minor}')
            print(f'{i * 5 + j} | {major} | {minor}')
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
