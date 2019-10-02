# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:58:54 2019

@author: Daniel Korsgaard Vinther Wolf

"""
from src import encode, decode

'''------< pytests >------'''
import pytest
def testEncoder():
    assert encode('aa') == '2a'
    assert encode('eeee') == '4e'

'''------< Fuzzing Tests >------'''
from fuzzing.fuzzer import FuzzExecutor
# Input:
# Files With Code Under Test
# Files with fuzz input :
numOfTestRuns = 20
filesWithCUT = ['src/runlengthfunctions.py']
filesWithFuzzStimuli = ['src/decoderTest.txt']

# Run fuzzinInputFiles on testFiles :
fuzzingTarget = ['python & '+filesWithCUT[0]+' -d']

# Test function, fuzzing: 
def testFuzzEncoder():
    fuzzer = FuzzExecutor(fuzzingTarget,filesWithFuzzStimuli)
    fuzzer.run_test(numOfTestRuns)
    return fuzzer.stats

'''------< Hypothesis tests >------'''
from hypothesis import given
from hypothesis.strategies import characters, text
@given(text(alphabet=characters()))
def test_decodeOnEncode(s):
    assert(decode(encode(s)) == s)

if __name__ == '__main__': 

    choice = input("Do you want to perform fuzzing tests? (y/yes or any other for no)\n")
    if choice == 'y' or choice == 'yes':
        print(testFuzzEncoder())
        print("fuzzing tests Completed")
    else:
        print("Ok no fuzzing tests!\n")    
    
    choice = input("Do you want to perform hypothesis tests? (y/yes or any other for no)\n")
    if choice == 'y' or choice == 'yes':
        test_decodeOnEncode()
        print("hypothesis tests Completed")
    else:
        print("Ok no hypothesis tests. Goodbye!\n")