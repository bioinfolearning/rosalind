#What to do:
# 1. get the DNA string from the file
# 2. make the string into a Seq object with Biopython and specify RNA alphabet
# 3. use translate() from BioPython
# 4. write protein sequence to file

from helperfunctions import write_to_file, make_output_filename, get_string

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

input_filename = "filename.txt"

rna_string = get_string(input_filename)
rna_sequence = Seq(rna_string, IUPAC.unambiguous_rna)
protein_sequence = rna_sequence.translate(to_stop = True)

write_to_file(input_filename, protein_sequence)
