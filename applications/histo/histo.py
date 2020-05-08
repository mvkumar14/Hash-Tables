import os
import sys

# Implement me.

with open('robin.txt','r') as f:
    words = f.read()

words = words.split()

storage = {}
max_length = 0
for i in words:
    try:
        storage[i] += 1
    except KeyError:
        storage[i] = 1
    if len(i) > max_length:
        max_length = len(i)

# order the dictionary:
ordered_storage = {}
for i in storage:
    num = storage[i]
    try:
        ordered_storage[num].append(i.lower())
    except KeyError:
        ordered_storage[num] = []
        ordered_storage[num].append(i.lower())

# print(ordered_storage)
for i in ordered_storage:
    ordered_storage[i] = sorted(ordered_storage[i])

# print(max(ordered_storage))
# print(ordered_storage[48])

# try this eventually.
# max_char_len = 0
# for i in storage:
#     if max_char_len < len(i):
#         max_char_len = len(i)

i = max(ordered_storage)
# print(i)
while i > 0 :
    try:
        for item in ordered_storage[i]:
            num_chars = len(item)
            num_spaces = max_length - num_chars
            print(item,' '*num_spaces,'#'*i)
    except KeyError:
        pass
    i -= 1

# loop through words
# stick words in dictionary
# order dictionary. 