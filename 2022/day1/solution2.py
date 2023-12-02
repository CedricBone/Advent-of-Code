"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, 
they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. 
That way, even if one of those Elves runs out of snacks, they still have two backups.

In the previous example, the top three Elves are:
 the fourth Elf (with 24000 Calories), 
 then the third Elf (with 11000 Calories), 
 then the fifth Elf (with 10000 Calories). 

The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

input = open("input.txt", "r")

elf_1 = 0
elf_2 = 0
elf_3 = 0
calories_1 = 0
calories_2 = 0
calories_3 = 0

current_elf_number = 0
current_calories = 0

for food in input:
    if food == "\n":
        if current_calories > calories_1:
            calories_3 = calories_2
            calories_2 = calories_1
            calories_1 = current_calories
            elf_3 = elf_2
            elf_2 = elf_1
            elf_1 = current_elf_number
        elif current_calories > calories_2:
            calories_3 = calories_2
            calories_2 = current_calories
            elf_3 = elf_2
            elf_2 = current_elf_number
        elif current_calories > calories_3:
            calories_3 = current_calories
            elf_3 = current_elf_number

        print(
            f"Elf number {current_elf_number} has {current_calories} calories.")
        current_elf_number += 1
        current_calories = 0
    else:
        current_calories += int(food)

input.close()
output = calories_1 + calories_2 + calories_3

print(f"Elf number {current_elf_number} has {current_calories} calories.\n")
print(f"\n1st: Elf number {elf_1} with {calories_1} calories")
print(f"2nd: Elf number {elf_2} with {calories_2} calories")
print(f"3rd: Elf number {elf_3} with {calories_3} calories")
print(f"\nThe top three elves are carrying {output} calories.\n")
