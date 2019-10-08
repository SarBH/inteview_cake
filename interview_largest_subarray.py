import unittest

def solution(N, K):
    """ Input: zero-indexed array N consisting of n integers and an integer K
        Returns the largest contiguous subarray of length K from all the contiguous subarrays of length K.
        """
    # initialize sub-array of zeros for comparison
    larget_sub_arr = [0] * K
    # intialize indeces for splitting
    start = 0
    end = start + K

    while end <= len(N):
        sub_arr = N[start:end]

        start += 1
        end = start + K

        if sub_arr > larget_sub_arr:
            larget_sub_arr = sub_arr
    
    return larget_sub_arr

    

    






class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1,4,3,2,5],4), [4,3,2,5])

    def test_2(self):
        self.assertEqual(solution([1,1,1,2,3], 3), [1,2,3])
    
    def test_3(self):
        self.assertEqual(solution([6,7,5,2,1,1], 2), [7,5])

    # def test_4(self):
    #     self.assertEqual(solution([1,4,3,2,5]), 4)



unittest.main(verbosity=2)