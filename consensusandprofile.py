#What to do
#1. make a matrix with the width specified, length will always be 4
#2. use an iterator to go through all the sequences in fasta format
#3. use for loop to go through every nucleotide in each sequence, and keep tally in the matrix of the nucleotide at that pos.
#4. make consensus sequence... how? well for each column get the max by using a combination of max() and find(). Maybe
# we can make a dictionary to keep track of the nucleotides associated with an index
#5. write the consensus sequence and the matrix into a file

from helperfunctions import write_to_file, make_output_filename, make_iterator, make_matrix

from Bio import SeqIO

input_filename = "filename.txt"

#so this will store the tally of nucleotides at each position
profile = []
#this is just the dictionary we will use to figure out what nucleotide had the most instances per position.
nucleotides = { "A":0, "C":1, "G":2, "T":3}

#this chunk keeps tally of the nucleotides at each position by adding to profile as it tranverses each sequence
iterator =  make_iterator(input_filename, "fasta")
for sequence in iterator:
    length = len(sequence.seq)
    if profile == []:
        profile = make_matrix(length, 4)
    for i in range (0, length):
        nucleotide = sequence.seq[i]
        profile[i][nucleotides[nucleotide]] += 1
                   
consensus_sequence = ""
                   
#this chunk finds what nucleotide had the most instances per position and adds it to the consensus sequence
for i in range(0, length):
    most_nucleotides = max(profile[i])
    nucleotide_index = profile[i].index(most_nucleotides)
    for key in nucleotides:
        if nucleotides[key] == nucleotide_index:
            consensus_sequence += key
    
#this chunk changes profile to a nice string that includes the consensus sequence and the final profile
final_profile = consensus_sequence + "\n"
for nucleotide in ["A", "C", "G", "T"]:
    row = []
    for i in range(0, length):
        row.append(str(profile[i][nucleotides[nucleotide]]))
    final_row = nucleotide + ": " + " ".join(row) + "\n"
    final_profile += final_row
        
write_to_file(input_filename, final_profile)
    
