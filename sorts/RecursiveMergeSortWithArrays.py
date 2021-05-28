def merge(arr):
	if(len(arr) > 1):
		middle = len(arr) // 2
		left = arr[:middle]
		right = arr[middle:]
		leftSize = len(left)
		rightSize = len(right)
		l = merge(left)
		r = merge(right)
		i = 0
		j = 0
		k = 0
		while(i < leftSize and j < rightSize):
			if(left[i] < right[j]):
				arr[k] = left[i]
				i = i + 1
			else:
				arr[k] = right[j]
				j = j + 1
			k = k + 1
		while(i < leftSize):
				arr[k] = left[i]
				i = i + 1
				k = k + 1
		while(j < rightSize):
				arr[k] = right[j]
				j = j + 1
				k = k + 1

## Test Merge Sort:

demoArray = [10,9,8,7,6,5,4,3,2,1]
print("Before Sorted")
for element in demoArray:
	print(element)
merge(demoArray)
print("After Sorted")
for element in demoArray:
	print(element)

