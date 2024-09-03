# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:27:55 2024

@author: hp
"""

import string

def find_words(text):
    """
    

    Parameters
    ----------
    text : string
        
    Returns: list of words from input text
    -------

    """

    
    text = text.replace("\n", " ")
    for char in string.punctuation:
        text = text.replace(char, "")
        
    words = text.split(" ")
    return words

words = find_words(text)
print(find_words(text))
