#What we're going to do
#1. get the DNA string
#2. switch each nucleotide to its complement but in lowercase, so it does not affect the conversion of other nucleotides
#3. make the strand uppercase, and then reverse it
#4. write the reverse complement to a new file

#import the functions from helperfunctions.py
from helperfunctions import get_string, write_to_file, make_output_filename

#setting the filename
input_filename = "filename.txt"

#get the DNA string from the file
DNA_string = get_string(input_filename)

# this is the easiest way but man is it ugly
rc1 = DNA_string.replace("A","t")
rc2 = rc1.replace("C","g")
rc3 = rc2.replace("G","c")
rc4 = rc3.replace("T","a")
reverse_complement = rc4.upper()[::-1] #note that the reversal part of this step comes straight from the stack overflow answer
                                       #here: https://stackoverflow.com/questions/931092/reverse-a-string-in-python I didn't
                                       #know the step part

#write reverse complement to output file
write_to_file(input_filename, reverse_complement)
