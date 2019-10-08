import unittest

def solution(T):
    # Your solution goes here.

    # create list from immutable string
    output = [char for char in T]

    # check minute chars
    if output[4] == '?':
        output[4] = '9'

    if output[3] == '?':
        output[3] = '5'

    # check hour chars and apply rules
    if output[1] == '?':
        if output[0] == '?':
            output[1] = '3'
            output[0] = '2'

        elif output[0] == '2':
            output[1] = '3'

        elif output[0] == '1':
            output[1] = '9'
    
    if output[0] == '?':
        if output[1] > '3':
            output[0] = '1'
        else:
            output[0] = '2'
    
    # convert output back to a string
    ans = "".join(output)

    return ans








class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("2?:?8"), "23:58")

    def test_2(self):
        self.assertEqual(solution("06:34"), "06:34")
    
    def test_3(self):
        self.assertEqual(solution("?8:4?"), "18:49")

    def test_4(self):
        self.assertEqual(solution("??:??"), "23:59")
    def test_5(self):
        self.assertEqual(solution("1?:??"), "19:59")



unittest.main(verbosity=2)