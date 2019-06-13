"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A:
list_of_codes = set()
area_pattern = re.compile(r"\((.*?)\)")
mobile_pattern = re.compile(r"([0-9]{4})")
telemarketers_pattern = re.compile(r"(140)")
count = 0
call_from_fixed_lines = 0
made_to_fixed_lines = 0
for i in range(len(calls)):
  area_code = area_pattern.match(calls[i][0])
  if area_code is not None and area_code.group() == "(080)":
    call_from_fixed_lines += 1
    area_called = area_pattern.match(calls[i][1])
    if area_called:
      list_of_codes.add(area_called.group())
      if area_called.group() == "(080)":
        made_to_fixed_lines += 1
    mobile_called = mobile_pattern.match(calls[i][1])
    if mobile_called:
      list_of_codes.add(mobile_called.group())
    telemarketers_called = telemarketers_pattern.match(calls[i][1])
    if telemarketers_called:
      list_of_codes.add(telemarketers_called.group())

print("The numbers called by people in Bangalore have codes:\n")
list_of_codes = sorted(list_of_codes)
for code in list_of_codes:
  print(code, '\n')

#Part B:
percent_of_calls = made_to_fixed_lines / call_from_fixed_lines * 100
print("%2.3f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % percent_of_calls)