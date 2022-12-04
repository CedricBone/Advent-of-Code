'''
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. 
Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, 
while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''


def assignments_finder(pair):
    num1 = pair.split('-', 1)
    num2 = (num1[1]).split(',', 1)
    num3 = (num2[1]).split('-', 1)
    num4 = (num3[1]).split(',', 1)
    return [int(num1[0]), int(num2[0]), int(num3[0]), int(num4[0][0:-1])]


input = open("input.txt", "r")

overlap_count = 0
elf1_start = -1
elf1_end = -1
elf2_start = -1
elf2_end = -1

for pair in input:

    assignments = assignments_finder(pair)
    elf1_start = assignments[0]
    elf1_end = assignments[1]
    elf2_start = assignments[2]
    elf2_end = assignments[3]

    overlap1 = (elf1_start <= elf2_start) and (elf1_end >= elf2_start)
    overlap2 = (elf2_start <= elf1_start) and (elf2_end >= elf1_start)

    if (overlap1 or overlap2):
        overlap_count += 1

input.close()
print(
    f"\nThere were {overlap_count} assignment pairs that overlapped.\n")
