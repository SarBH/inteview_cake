import unittest


def solution(A):
	"""Your solution goes here."""

	server1 = []
	server2 = []
	load1 = 0
	load2 = 0



	while A != []:	
		largest = A.pop(A.index(max(A)))
	
		if load1 <= load2:
			server1.append(largest)
			load1 += largest
		else:
			server2.append(largest)
			load2 += largest

	return abs(load1 - load2)
		


  


class Test(unittest.TestCase):
	def test_rows(self):
		list_items = [1,2,3,4,5]
		self.assertEqual(solution(list_items), 1)

	def test_all_equal(self):
		list_items = [8,1,3,7,3]
		self.assertEqual(solution(list_items), 0)

	def test_descending(self):
		list_items = [5,5,5,1,9]
		self.assertEqual(solution(list_items), 3)


unittest.main(verbosity=2)