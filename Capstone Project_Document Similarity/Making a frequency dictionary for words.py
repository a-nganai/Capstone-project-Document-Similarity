# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:05:47 2024

@author: hp
"""

def frequencies(words):
    """
    

    ----------
    words : list of words

    Returns: frequency dictionary for input words
    
    """
    
    freq_dict = {}
    
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
            
        else:
            freq_dict[word] = 1
       return freq_dict
   
freq_dict = frequencies(words)