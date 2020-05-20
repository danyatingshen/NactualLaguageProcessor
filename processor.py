
import StemmingUtil
import os	
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random
import csv
import math
import operator
from csv import reader
import math
import string

def FiletoStringList(textfile):
    file = open(str(textfile), encoding="utf8")
    listText = []
    for line in file:
        line = line.rstrip()
        # line = line.lower()
        words = word_tokenize(line)
        for eachWord in words :
            # I allow special char [] bc it's used in doc for referance 
            newWord = eachWord.strip('!"#$%&'+'()*+,-./:;<=>?@\^_`{|}~')      
            if len(newWord) == 0 :
                continue  
            listText.append(newWord)
    print(listText)
    return listText

# def counting ():
    # algo: create dictionary for each name
    # for each words: find the first Mr, check 
    # 1. if its surrounded by [], skip
    # 2. next words after Mr, check if it's all upper or mix or lower
        # 2.1: if all upper, then take it as a name
        # 2.2: if mix, count percenatge (maybe prompt to the user and ask if it is a name or set some percentage)
        # 2.3: if lower, skip

def main(): 
    # step 1: read from command line for name of pdf(full)
    # step 2: need to combine all text file into one text and save as it's pdf name
    filepath = 'splitted/testfile.txt'
    # step 3: pass file.txt name into readin()
    listText = FiletoStringList(filepath)
    # step 4: counting words by speaker
main()


