#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:06:58 2019

@author: romain
"""

sdsd
def BoldWord(mot, texte):
 
    long = len(mot)
    for i in range(0, len(texte)):
        sel = texte[i:i+long]
        if sel.lower() == mot.lower() and texte[i-3:i]!="<b>":
            return BoldWord(mot, texte.replace(sel, "<b>%s</b>" % sel))
    return texte