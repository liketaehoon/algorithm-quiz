#-*- encoding: utf-8 -*-
import unittest
import random
# from bf import max_after_shift as max_after_shift_bf

"""
calcurate_multiplied_sum_and_sumarray

Calcurate multipied sum of given array
Create sum_array which contain sum value from 0 to index
"""
def calcurate_multiplied_sum_and_sumarray(length,values) :
    ret = 0
    normal_sum = 0
    sum_array = []
    for index, value in enumerate(values) :
        ret = ret + value * (index+1)
        normal_sum = normal_sum + value
        sum_array.append(normal_sum)
    return ret, sum_array

"""
calcurate_diff

Calcurate diff when shift value from {from_index} to {to_index}

diff calcurate algorithm
if to_index < from_index :
    diff = sum(values[to_index:from_index]) - values[from_index] * (from_index-to_index)
elif to_index > from_index :
    diff = values[from_index] * (to_index - from_index) - sum(values[from_index+1:to_index+1])

sum(values[x:y]) has O(n) complexity.
To speed up, caclcuration executed with sumarray which has constant time

"""
def calcurate_diff(values, from_index, to_index, sum_array) :
    diff = 0
    if to_index < from_index :
        left_sum = sum_array[from_index-1]
        if to_index > 0 :
            left_sum = left_sum - sum_array[to_index-1]
        diff = left_sum - values[from_index] * (from_index-to_index)
    elif to_index > from_index :
        right_sum = sum_array[to_index]
        if from_index > -1 :
            right_sum = right_sum - sum_array[from_index]
        diff = values[from_index] * (to_index - from_index) - right_sum
    return diff

"""
max_after_shift

Find maximum sum value after shift 1 element.
"""
def max_after_shift(length, values) :
    ori_multiplied_sum,sum_array = calcurate_multiplied_sum_and_sumarray(length,values)
    diff = 0
    for index, value in enumerate(values) :
        newdiff = 0;
        left_index = 0
        right_index = length -1
        while right_index > index :
            if values[index] <=  values[right_index] :
                right_index = right_index -1
                continue
            newdiff = calcurate_diff(values, index, right_index, sum_array)
            right_index = right_index -1
            break
        if newdiff > diff :
            diff = newdiff
        while left_index < index :
            if values[index] >= values[left_index] :
                left_index = left_index +1
                continue
            newdiff = calcurate_diff(values, index, left_index, sum_array)
            left_index = left_index +1
            break
        if newdiff > diff :
            diff = newdiff
    return ori_multiplied_sum + diff

length = int(raw_input().strip())
value_str = raw_input()
values = [ int(value) for value in value_str.strip().split(' ') ]
print max_after_shift(length, values)


class shift_test(unittest.TestCase) :
    def test_ex1(self):
        self.assertEqual(max_after_shift(4,[4,3,2,5]), 39)
    def test_ex2(self):
        self.assertEqual(max_after_shift(5,[1,1,2,7,1]), 49)
    # def test_huge(self) :
        # self.huge_sample_length = 10000
        # self.huge_sample = [ random.randrange(0,1000000) for i in range(self.huge_sample_length) ]
        # self.huge_answer = max_after_shift_bf(self.huge_sample_length, self.huge_sample)
        # print('----')
        # self.assertEqual(max_after_shift(self.huge_sample_length, self.huge_sample), self.huge_answer)
        # self.assertEqual()
    def test_huge_time(self) :
        length = 200000
        values = [ str(random.randrange(0,1000000)) for i in range(length) ]
        value_str = ' '.join(values)
        values = [ int(value) for value in value_str.strip().split(' ') ]
        print(max_after_shift(length, values))
