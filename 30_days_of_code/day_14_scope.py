class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.sorted_arr = sorted(self.__elements)
        self.maximumDifference = abs(self.sorted_arr[0] - self.sorted_arr[-1])

    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
