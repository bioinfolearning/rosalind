#What to do:
#1. make a little hammy distance function to compare two DNA sequences
#2. Extract both sequences from a single file
#3. write total point mutations to file

from helperfunctions import get_strings, write_to_file, make_output_filename

input_filename = "filename.txt"

def hamming_distance(DNA_seq1, DNA_seq2):
    Dh = 0
    for i in range(0, len(DNA_seq1)):
        if DNA_seq1[i] != DNA_seq2[i]:
            Dh += 1
    return Dh
        
sequences = get_strings(input_filename)
point_mutations = hamming_distance(sequences[0], sequences[1])

write_to_file(input_filename, str(point_mutations))
