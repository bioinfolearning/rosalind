# I made these functions because I saw repetitive code in my Rosalind answers.
# since I am working in a Jupyter notebook I had to include paths since I keep the datasets and outputs separate

# get_string
# function that opens a file (given its name) and returns the string in it. 

def get_string(input_filename):
    file_location = "file_path/" + input_filename
    file = open(file_location)
    string = file.read().strip()
    return string
    
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