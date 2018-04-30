#What I have to do
#1. Open the file with the DNA string
#2. Read from the file
#3. Keep tally of nucleotides
#4. Create a new file and write the tally in the order A C G and T

#setting file names
input_file_name = "filename.txt"
output_file_name = "output.txt"

DNA_string_file = open(input_file_name)
DNA_string = DNA_string_file.readlines().strip() #should only be one line
output_file = open(output_file_name)
output_file.write(str(DNA_string.count("A")) + " " +
                  str(DNA_string.count("C")) + " " +
                  str(DNA_string.count("G")) + " " +
                  str(DNA_string.count("T")))
