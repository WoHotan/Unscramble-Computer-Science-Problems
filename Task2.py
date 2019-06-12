"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
spent_time = {}
for i in range(len(calls)):
    if '09-2016' in calls[i][2]:
        if (calls[i][0] in spent_time) ^ (calls[i][1] in spent_time):
            if calls[i][0] in spent_time:
                spent_time[calls[i][0]] += int(calls[i][3])
                spent_time[calls[i][1]] = int(calls[i][3])
            else:
                spent_time[calls[i][0]] = int(calls[i][3])
                spent_time[calls[i][1]] += int(calls[i][3])
        elif calls[i][0] in spent_time and calls[i][1] in spent_time:
            spent_time[calls[i][0]] += int(calls[i][3])
            spent_time[calls[i][1]] += int(calls[i][3])
        else:
            spent_time[calls[i][0]] = int(calls[i][3])
            spent_time[calls[i][1]] = int(calls[i][3])

max_time = 0
max_telephone = None
for k, v in spent_time.items():
    if v > max_time:
        max_time = v
        max_telephone = k
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_telephone, max_time))

