#!/usr/bin/python

import glob

import functions.person_counter as pc

path = 'pictures'

file_list = glob.glob(f"{path}/*")
for file in file_list:
    pc.person_counter(file)
