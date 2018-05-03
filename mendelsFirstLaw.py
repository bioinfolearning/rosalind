# Okay, so for this we only have to calculate the probability of the offspring either being a dominant homozygote or a
# heterozygote

# What to do:
# make a function for this
# 1. get the total number of organisms, and the total - 1 for the second organism
# 2. calcultate the probability it will be dominant homozygote or heterozygote
# 3. write this probability into a file

from helperfunctions import write_to_file, get_nums, make_output_file

input_filename = "filename.txt"

def prob_dominant_allele(k, m, n):
    #k homozygous dominant, m heterozygous, n homozygous recessive
    total_organisms = k + m + n
    prob_kk = (k/total_organisms * (k-1)/(total_organisms-1))
    prob_km = (k/total_organisms * m/(total_organisms-1)) * 2
    prob_kn = (k/total_organisms * n/(total_organisms-1)) * 2
    prob_mm = (m/total_organisms * (m-1)/(total_organisms-1) * .75)
    prob_mn = (m/total_organisms * n/(total_organisms-1) * .5) * 2
    total_prob = prob_kk + prob_km + prob_kn + prob_mm + prob_mn 
    return total_prob

organism_nums = get_nums(input_filename)
probability = prob_dominant_allele(organism_nums[0], organism_nums[1], organism_nums[2])

write_to_file(input_filename, str(probability))
