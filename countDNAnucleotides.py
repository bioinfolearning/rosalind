#What I have to do
#1. Open the file with the DNA string
#2. Read from the file
#3. Keep tally of nucleotides
#4. Create a new file and write the tally in the order A C G and T

from helperfunctions import get_string, write_to_file, make_output_filename

#setting file names
input_filename = "filename.txt"

#opening file and setting up DNA string for counting
DNA_string = get_string(input_filename)

#make a tally of nucleotides
nucleotide_tally = (str(DNA_string.count("A")) + " " +
                    str(DNA_string.count("C")) + " " +
                    str(DNA_string.count("G")) + " " +
                    str(DNA_string.count("T")))

#write tally to new file
write_to_file(input_filename, nucleotide_tally)
