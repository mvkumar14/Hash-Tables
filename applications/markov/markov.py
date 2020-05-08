import random
from string import ascii_uppercase
import random
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(os.getcwd())
sys.path.append(dir_path)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()
# class Storage():
# singleton pattern of this class? , or rather one per instance
# where I want to try markov?

storage = {} # keys are strings values are pointers to Markov chain objects

class Markov():
    def __init__(self, value):
        self.value = value 
        self.possible_next = [] # list of pointers to markov chains
    

    def add(self, value):
        if self._is_in(value):
            # print('that value is already inside')
            return None
        try:
            # try to use a value from storage
            self.possible_next.append(storage[value])
        except KeyError:
            # else create the Markov value and 
            # add that value to internal list
            storage[value] = Markov(value)
            self.possible_next.append(storage[value])

    def _is_in(self, value):
        for i in self.possible_next:
            if i.value == value:
                return True
            else:
                return False


# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences

# for every item in list add the item to the previous 
# item's markov object. 

prev = None

for i in words:
    # print(i)
    if prev == None:
        storage[i] = Markov(i)
        prev = storage[i]
        continue
    prev.add(i)
    prev = storage[i]

# for i in storage['the'].possible_next:
#     print(i.value)

start_words = []
stop_words = []
end_punct = ".?!"
for i in storage:
    # print(i)
    if len(i) == 1:
        if i in ascii_uppercase:
            start_words.append(i)
        else:
            continue
    if i[0] in ascii_uppercase or i[0] == '"': #startword
        start_words.append(i)
    elif i[-1] in end_punct or (i[-2] in end_punct and i[-1]== '"'):# stopword
        stop_words.append(i)
    else:
        continue

# print("start words:", start_words)
# print("stop words:", stop_words)

output = random.choice(start_words)
current = storage[output]

# if it starts with a quote 
# end it with a quote too
# if you create a new quote inbetween 
# then make sure to close quote 
# if it starts getting too long then 
# have it choose directly from the stop_words_quotes list

while current.value not in stop_words:
    current = random.choice(current.possible_next)
    output += " " + current.value

print(output)
    


# while word isn't stop word:
    # next_word = randomly sample
    # output += next_word
    # word = next_word