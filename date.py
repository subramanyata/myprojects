#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:50:11 2017

@author: hfn
"""



import datefinder

def date_extract(input_string):
    """ exracts date from a given input string """
    matches = list(datefinder.find_dates(input_string))
    date = {}
    date["year"] = matches[0].year
    date["day"]  = matches[0].day
    date["minutes"]  = matches[0].minute
    date["hour"]  = matches[0].hour
    date["month"] = matches[0].month
    date["second"] = matches[0].second
    return date
        