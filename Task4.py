"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
numbers = {}
for num in texts:
    numbers[num[0]] = True
    numbers[num[1]] = True
for num in calls:
    numbers[num[0]] = False
    numbers[num[1]] = True

telemarketers_numbers = []
print("These numbers could be telemarketers: \n")
for k, v in numbers.items():
    if not v:
        telemarketers_numbers.append(k)
telemarketers_numbers = sorted(telemarketers_numbers)
for number in telemarketers_numbers:
    print(number)


