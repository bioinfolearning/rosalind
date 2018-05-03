# I made these functions because I saw repetitive code in my Rosalind answers.
# since I am working in a Jupyter notebook I had to include paths since I keep the datasets and outputs separate

# get_string
# function that opens a file (given its name) and returns the string in it. 

def get_string(input_filename):
    file_location = "file_path/" + input_filename
    file = open(file_location)
    string = file.read().strip()
    return string

# get_strings
# pretty much the same as above but it does it with multiple sequences and returns a list of them

def get_strings(input_filename):
    file_location = "Rosalind_datasets/" + input_filename
    file = open(file_location)
    strings = file.readlines()
    return strings
    
# write_to_file
# writes the contents specified to a file (given its name)
# note: this function should only be used once per problem, or it will erase what was previously written

def write_to_file(input_filename, content):
    output_filename = make_output_filename(input_filename)
    file_location = "file_path/" + output_filename
    file = open(file_location, "w")
    file.write(content)
    file.close()
    
 # make_output_filename
 # because I'm lazy and can't be bothered   
    
 def make_output_filename(input_filename):
    filename = input_filename.split(".")
    output_filename = filename[0] + "_output.txt"
    return output_filename

# get_nums
# returns a list of numbers read from a single line in a specific file

def get_nums(input_filename):
    file_location = "file_path/" + input_filename
    file = open(file_location)
    nums_list = file.read().strip().split()
    nums = []
    for num in nums_list:
        nums.append(int(num))
    return nums

# make_iterator
# returns an iterator to go through specified format sequences in a file with BioPython

def make_iterator(input_filename, format_type):
    file_location = "file_path/" + input_filename
    iterator = SeqIO.parse(file_location, format_type)
    return iterator

# make_matrix
# given the number of columns and rows, creates a zero matrix with those dimensions

def make_matrix(columns, rows):
    matrix = []
    for i in range (0, columns):
        column = []
        for j in range(0, rows):
            column.append(0)
        matrix.append(column)
    return matrix

# make_list
# makes a zeroed list of specified length

def make_list(length):
    l = []
    for i in range(0, length):
        l.append(0)
    return l



