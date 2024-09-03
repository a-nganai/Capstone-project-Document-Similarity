# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:36:41 2024

@author: hp
"""

text_1 = read_text("sonnet18.txt")
text_2 = read_text("sonnet19.txt")
words_1 = find_words(text_1)
words_2 = find_words(text_2)
freq_dict_1 = frequencies(words_1)
freq_dict_2 = frequencies(word_2)
print(calculate_similarity(freq_dict_1, freq_dict_2))