#What I have to do
#1. Open file and read DNA string
#2. Replace every T nucleotide with a U
#3. write new RNA string into a file

#setting file names
input_file_name = "filename.txt"
output_file_name = "output_filename.txt"

#open file and prepare DNA string
DNA_string_file = open(input_file_name)
DNA_string = DNA_string_file.read().strip()

#replace every 'T' with 'U'
RNA_string = DNA_string.replace("T","U")

#open output file and write RNA string to it
output_file = open(output_file_name, "w")
output_file.write(RNA_string)
output_file.close()
