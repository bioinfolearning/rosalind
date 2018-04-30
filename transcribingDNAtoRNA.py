#What I have to do
#1. Open file and read DNA string
#2. Replace every T nucleotide with a U
#3. write new RNA string into a file

from helperfunctions import get_string, write_to_file, make_output_filename

#setting filenames
input_filename = "filename.txt"

#open file and prepare DNA string
DNA_string = get_string(input_filename)

#replace every 'T' with 'U'
RNA_string = DNA_string.replace("T","U")

#open output file and write RNA string to it
write_to_file(input_filename, RNA_string)
