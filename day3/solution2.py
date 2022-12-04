'''
--- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group.
For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack,
and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges.
All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges.
The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type.
So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is lowercase r;
this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts:
here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''


def find_badge(elf1_rucksack, elf2_rucksack, elf3_rucksack):
    for item1 in elf1_rucksack:
        for item2 in elf2_rucksack:
            if item1 == item2:
                for item3 in elf3_rucksack:
                    if item2 == item3:
                        return item3


def priority(item):
    item_ascii = ord(item)
    if item_ascii <= 90:
        return 26 + (item_ascii - (ord("A") - 1))
    else:
        return item_ascii - (ord("a") - 1)


input = open("input.txt", "r")
priority_sum = 0
current_elf = 0
elf_team = 0
badge = '*'
elf1_rucksack = '*'
elf2_rucksack = '*'
elf3_rucksack = '*'

for contents in input:

    match current_elf:
        case 0:
            elf1_rucksack = contents
            current_elf += 1
        case 1:
            elf2_rucksack = contents
            current_elf += 1
        case 2:
            elf3_rucksack = contents
            current_elf += 1
        case 3:
            badge = find_badge(elf1_rucksack, elf2_rucksack, elf3_rucksack)
            priority_sum += priority(badge)
            print(
                f"elf team {elf_team} had {badge} as a badge, with a priority of {priority(badge)}")
            elf_team += 1
            elf1_rucksack = contents
            current_elf = 1

input.close()
badge = find_badge(elf1_rucksack, elf2_rucksack, elf3_rucksack)
priority_sum += priority(badge)
print(
    f"elf team {elf_team} had {badge} as a badge, with a priority of {priority(badge)}")
print(f"\nThe priority sum of the badges is {priority_sum}.")
