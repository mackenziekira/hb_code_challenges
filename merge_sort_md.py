def merge(lst1, lst2):
	len1 = len(lst1)
	len2 = len(lst2)

	i = 0
	j = 0
	new_lst = []

	while i < len1 and j < len2:
		if lst1[i] < lst2[j]:
			new_lst.append(lst1[i])
			i += 1

		else:
			new_lst.append(lst2[j])
			j += 1

	new_lst.extend(lst1[i:])
	new_lst.extend(lst2[j:])

	return new_lst

def merge_sort(lst):
	"""
	>>> merge_sort([4, 1, 2, 3, 5])
	[1, 2, 3, 4, 5]
	"""

	if len(lst) < 2:
		return [lst[0]]

	midpoint = len(lst) / 2

	left = merge_sort(lst[:midpoint])
	right = merge_sort(lst[midpoint:])

	return merge(left, right)


print merge_sort([5, 3, 2, 1, 4])

if __name__=='__main___':
	import doctest
	doctest.testmod()

