#What I have to do
#1. Open the file with the DNA string
#2. Read from the file
#3. Keep tally of nucleotides
#4. Create a new file and write the tally in the order A C G and T

#setting file names
input_file_name = "filename.txt"
output_file_name = "output.txt"

#opening file and setting up DNA string for counting
DNA_string_file = open(input_file_name)
DNA_string = DNA_string_file.read().strip() #should only be one line

#make a tally of nucleotides
nucleotide_tally = (str(DNA_string.count("A")) + " " +
                    str(DNA_string.count("C")) + " " +
                    str(DNA_string.count("G")) + " " +
                    str(DNA_string.count("T")))

#write tally to new file
output_file = open(output_file_name, "w")
output_file.write(nucleotide_tally)
output_file.close()
