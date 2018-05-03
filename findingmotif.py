#What to do:
# 1. Get the strings from file
# 2. use find() on the DNA string until it returns -1, everytime one is found, change the first base to *
# 3. keep track of the indexes
# 4. write indexes to file

from helperfunctions import write_to_file, get_strings, make_output_filename

input_filename = "filename.txt"

dna_strings = get_strings(input_filename)
dna_string = dna_strings[0].strip()
substring = dna_strings[1].strip()

substring_index = dna_string.find(substring)
indexes = []

while(substring_index != -1):
    indexes.append(str(substring_index+1))
    dna_string = dna_string[:substring_index] + "*" + dna_string[substring_index+1:]
    substring_index = dna_string.find(substring)
    
index_string = " ".join(indexes)

write_to_file(input_filename, index_string)

#this was tricky because the answer was in 1-based numbering and I goofed.



