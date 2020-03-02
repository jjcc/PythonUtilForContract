#!/usr/bin/python
# -*- coding: latin-1 -*-

import yaml
import pprint
import io
#import xlsxwriter
import pandas as pd
import codecs
import sys



def convert(lines):
    constant = ("    - label:\n","        en: ","        fr: ","      value: ")
    converted = []

    for l in lines:
        c = l.lower().replace(" ", "_")#.rstrip()
        converted.append(constant[0])
        converted.append(constant[1] + l)
        converted.append(constant[2] + l)
        converted.append(constant[3] + c)
    return converted

def main():
    with open("Data/lliorg.txt",'r') as fp:
        lines = fp.readlines();
    res = convert(lines)
    with open("Data/converted.txt","w") as fo:
        for i in res:
            fo.write(i)

if __name__ == '__main__':
    main()