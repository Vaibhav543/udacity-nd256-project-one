import csv

import utils

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

callers = []
whitelist = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        sending, receiving, timestamp = text
        whitelist.extend([sending, receiving])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        calling, receiving, timestamp, seconds = call
        callers.append(calling)
        whitelist.append(receiving)

# Deduplicate the lists
callers = utils.dedupe_list(callers)
whitelist = utils.dedupe_list(whitelist)

# The list of suspicious numbers is those that appear in the callers list, but not in the whitelist
suspicious = set(callers).difference(whitelist)

print('These numbers could be telemarketers:')
for phone_number in sorted(suspicious):
    print(phone_number)
