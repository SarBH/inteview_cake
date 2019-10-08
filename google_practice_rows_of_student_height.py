import sys
import unittest
from collections import defaultdict

def solution(A):
	"""Your solution goes here."""

	row_counter = 1

	rows_dict = defaultdict(list)


	for item in A:
		for row_num in range(row_counter):
			if rows_dict["row"+str(row_num)] == []:
				rows_dict["row"+str(row_num)].append(item)
				break
			elif item < rows_dict["row"+str(row_num)][-1]: # if student is shorter than the shortest student in the row, everyone else is taller than him
				rows_dict["row"+str(row_num)].append(item)
				break
		else:
			rows_dict["row"+str(row_counter)].append(item)
			row_counter += 1

	return row_counter





class Test(unittest.TestCase):
	def test_rows(self):
		list_items = [5,4,3,6,1]
		self.assertEqual(solution(list_items), 2)

	def test_all_equal(self):
		list_items = [1,1,1,1]
		self.assertEqual(solution(list_items), 4)

	def test_descending(self):
		list_items = [1,2,3,4,5]
		self.assertEqual(solution(list_items), 5)

	def test_equal_and_smaller(self):
		list_items = [17,17,17,5,5]
		self.assertEqual(solution(list_items), 3)


unittest.main(verbosity=2)