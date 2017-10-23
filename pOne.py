class POne(object):
	def findPeakAndValley(self, arr):
		arr_len = len(arr)
		# Since you can always build a castle at the start of the array, set ans to 1 at beginning
		ans = 1
		prev = arr[0]
		for i in range(1, len(arr) - 1):
			if arr[i] == arr[i + 1] and arr[i] != arr[i-1]:
				prev = arr[i - 1]
				continue
			else:
				#compare the middle value with prev value and next adjacent value, if find peak or valley, update prev
				if (arr[i] > prev and arr[i] > arr[i + 1]) or (arr[i] < prev and arr[i] < arr[i + 1]):
					ans += 1
					prev = arr[i]
		return ans
