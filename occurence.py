# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:05:25 2021

@author: mehdi
"""

import csv
import string

translator = str.maketrans('', '', string.punctuation)

word_count = {}
text = open('Data.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])
    
