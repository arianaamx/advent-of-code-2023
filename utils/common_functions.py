def grab_all_lines_from_file(file_name):
    file = open(file_name, "r")
    file_array = file.readlines()

    # remove `/n` from each line using list comprehension
    file_array = [i.strip() for i in file_array]
    return file_array