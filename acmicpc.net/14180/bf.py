#-*- encoding: utf-8 -*-
import unittest
import random

def multiplied_sum(values) :
    ret = 0
    for index, value in enumerate(values) :
        ret = ret + value * (index+1)
    return ret

def multiplied_sum_diff(values, from_index, to_index) :
    diff = 0
    if to_index < from_index :
        diff = sum(values[to_index:from_index]) - values[from_index] * (from_index-to_index)
    elif to_index > from_index :
        diff = values[from_index] * (to_index - from_index) - sum(values[from_index+1:to_index+1])
    return diff

def max_after_shift(length, values) :
    ori_multiplied_sum = multiplied_sum(values)
    diff = 0
    for index, value in enumerate(values) :
        if index > 0 : # left shift
            for left_index in range(0, index):
                newdiff = multiplied_sum_diff(values, index, left_index)
                if newdiff > diff :
                    diff = newdiff
        elif index < (length-1) : # right shift
            for right_index in range(index, length):
                newdiff = multiplied_sum_diff(values, index, right_index)
                if newdiff > diff :
                    diff = newdiff
    return ori_multiplied_sum + diff

if __name__ == '__main__' :
    length = 4
    values = [4,3,2,5]
    print(max_after_shift(length, values))


class shift_test(unittest.TestCase) :
    def setUp(self):
        self.huge_sample = [ random.randrange(0,1000000) for i in range(200000) ]
        self.huge_sample_length = 200000
    def test_multiplied_sum(self) :
        self.assertEqual(multiplied_sum([4,3,2,5]), 36)
    def test_ex1(self):
        self.assertEqual(max_after_shift(4,[4,3,2,5]), 39)
    def test_ex2(self):
        self.assertEqual(max_after_shift(5,[1,1,2,7,1]), 49)
    # def test_gen(self):
        # [ random.randrange(0,1000000) for i in range(200000) ]
    def test_huge(self) :
        max_after_shift(self.huge_sample_length, self.huge_sample )
