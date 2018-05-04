#What to do:
#1. go through all the sequences and store them in a list
#2. go through each sequence, for each you have to find a match for the suffix and its prefix
#3. once you find a match, then place it in a list
#4. write all pairs into a file

from helperfunctions import make_iterator, write_to_file, make_list, make_output_filename

from Bio import SeqIO

input_filename = "filename.txt"

def directed_edges(input_filename):
    sequences = []
    iterator = make_iterator(input_filename, "fasta")
    for sequence in iterator:
        sequences.append(sequence)
    
    matches = []
    k = 3
    for seq1 in sequences:
        seq1_prefix = seq1.seq[:k]
        seq1_suffix = seq1.seq[-k:]
        for seq2 in sequences:
            seq2_prefix = seq2.seq[:k]
            seq2_suffix = seq2.seq[-k:]
            if seq1.id != seq2.id:
                if seq1_prefix == seq2_suffix and [seq2.id, seq1.id] not in matches:
                    matches.append([seq2.id, seq1.id])
                if seq1_suffix == seq2_prefix and [seq1.id, seq2.id] not in matches:
                    matches.append([seq1.id, seq2.id])
        
    overlap_graph = ""
    for match in matches:
        directed_edge = " ".join(match) + "\n"
        overlap_graph += directed_edge
    return overlap_graph.strip()


answer = directed_edges(input_filename)
write_to_file(input_filename, answer)
