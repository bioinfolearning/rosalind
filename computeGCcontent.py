#We're now using BioPython to work with fasta files
#installed with anaconda to use in jupyter notebook. Info: http://biopython.org/wiki/Download

#What to do:
#1. use biopython to make a generator of the sequences.
#2. set a maximum GC content standard to which we can compare each sequence's GC content to
#4. write the winner sequence to a file

from helperfunctions import write_to_file, make_output_filename, make_iterator

from Bio import SeqIO
from Bio.SeqUtils import GC

input_filename = "filename.txt"
format_type = "fasta"

def max_GC_content(input_file, format_type):
    
    max_GC_content = 0.00
    max_GC_content_id = ""
    generator = make_iterator(input_filename, format_type)
    
    for sequence in generator:
        GC_content = GC(sequence.seq) #BioPython has a built in way to calculate the GC content of a sequence
        if GC_content > max_GC_content:
            max_GC_content = GC_content
            max_GC_content_id = sequence.id
        
    winner = max_GC_content_id + "\n" + str(max_GC_content)
    return winner

answer = max_GC_content(input_filename)

write_to_file(input_filename, answer)
