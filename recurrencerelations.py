#Recurrence relation is defined as Fn = Fn-1 + Fn-2 where Fn-1 are the rabbits that were alive one month ago and Fn-2
# is not only the number ofrabbits that were alive two months ago, but also happens to be the number of offspring for the
# n month.
# What to do:
#1. function must take n and k, where n is the month we're interested in and k is the number of offspring per pair of raabits.
#2. Get the month and litter size from specified file
#3. write the result from the how_many_bunnies functions into a new file

from helperfunctions import write_to_file, make_output_filename, get_nums

input_filename = "filename.txt"

def how_many_bunnies(month, litter_size):
    total_buns = 0
    if month == 1 or month == 2:
        total_buns += 1
    else:
        total_buns += how_many_bunnies(month-1, litter_size) + how_many_bunnies(month-2, litter_size)*litter_size
    return total_buns

nums = get_nums(input_filename)
bunnies = how_many_bunnies(nums[0], nums[1])

write_to_file(input_filename, str(bunnies))
