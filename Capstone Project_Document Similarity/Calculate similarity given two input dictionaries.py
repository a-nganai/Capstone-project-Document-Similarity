# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:23:54 2024

@author: hp
"""

def calculate_similarity(dict1, dict2):
    """
    

    Parameters
    ----------
    dict1 : frequency dictionary for one text
    dict2 : frequency dictionary for another text

    Returns: float, representing how similar both texts are to each other
    -------

    """
    diff = 0
    total = 0
    
    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict1[word] - dict2[word])
            
        else:
            diff += dict1[word]
            
    for word in dict2.keys():
        if word mot in dict1.keys():
            diff += dict2[word]
            
    total = sum(dict1.values()) + sum(dict2.values())
    difference = diff / total
    similar = 1.0 - difference
    
    return round(similar, 2)