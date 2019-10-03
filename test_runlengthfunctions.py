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
    assert encode('') == ''

def testDecoder():
    assert decode('2a') == 'aa'
    assert decode('2a3b4n') == 'aabbbnnnn'
    assert encode('') == ''
    
'''------< Fuzzing Tests >------'''
from fuzzing.fuzzer import FuzzExecutor
# Input:
# Files With Code Under Test
# Files with fuzz input :
numOfTestRuns = 3
filesWithCUT = ['src/runlengthfunctions.py']
filesWithFuzzStimuli = ['src/decoderTest.txt']

# Run fuzzinInputFiles on testFiles :
fuzzingTarget = ['python & '+filesWithCUT[0]+' -d']

# Test function, fuzzing: 
@pytest.mark.skip(reason="Do not pytest fuzzTest")
def testFuzzEncoder():
    fuzzer = FuzzExecutor(fuzzingTarget,filesWithFuzzStimuli)
    fuzzer.run_test(numOfTestRuns)
    return fuzzer.stats

'''------< Hypothesis tests >------'''
from hypothesis import given, example
from hypothesis.strategies import characters, text
@given(s = text(alphabet=characters()))
@example(s = '')
@pytest.mark.skip(reason="Do not pytest hypoTest")
def test_decodeOnEncode(s):
    assert(decode(encode(s)) == s)

if __name__ == '__main__': 
    import sys

    def fuzzTest():
        print("Running fuzzing tests")
        print(testFuzzEncoder())
        print("fuzzing tests Completed")
    
    def hypoTest():
        print("Running hypothesis tests")
        test_decodeOnEncode()
        print("hypothesis tests Completed")

    if len(sys.argv) == 1: # if not using CLI but user input
        choice = input("Do you want to perform fuzzing tests? (y/yes or any other for no)\n")
        if choice == 'y' or choice == 'yes':
            fuzzTest()
        else:
            print("Ok no fuzzing tests!\n")    
        
        choice = input("Do you want to perform hypothesis tests? (y/yes or any other for no)\n")
        if choice == 'y' or choice == 'yes':
            hypoTest()
        else:
            print("Ok no hypothesis tests. Goodbye!\n")
    else:
        argv = sys.argv
        if '-fuzztest' in argv or '-ft' in argv:
            fuzzTest()
        elif '-hypotest' in argv or '-ht' in argv:
            hypoTest()
        else:
            Exception("No Tests selected!. Usage is '-ft' or '-ht'")