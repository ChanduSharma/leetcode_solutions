import unittest

class solution:

    def __init__(self) -> None:
        self.res = None
        self.nums = None
    # Simplest Brute force solution
    # Iterate over each element and create new list 
    # and add at the resulting position
    def build_array(self, nums: list[int]) -> list[int]:

        res = [0 for i in range(len(nums))]
        for i in range(len(res)):
            res[i] = nums[nums[i]]
    
        return res

    # Same variation of the brute force solution 
    # but in pythonic way
    def build_arrary_pythonic(self, nums: list[int]) -> list[int]:
        
        res = [ nums[i] for i in nums]
        return res

    # Optimized solution in terms of space
    # By storing two values at each index we can
    # rearrange the values in place
    def build_array_op(self, nums: list[int]) -> list[int]:

        # Using Euclid's division lemma
        # and hint from question that every value is less than length of list
        # a = bq + r
        # a is what we want to store at each point 
        # b is what we want to get after we calculated a for each positions

        q = len(nums)

        for i in range(len(nums)):
            r = nums[nums[i]] % q # to get the original value that was there before mutation
            nums[i] = r * q + nums[i]

        for i in range(len(nums)):
            nums[i] = nums[i] // q

        return nums
 

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.test_class = solution()
        self.input = [0,2,1,5,3,4]
        self.res = [0, 1, 2, 4, 5, 3]

    def test_brute_test(self):

        self.assertListEqual( self.res, self.test_class.build_array(self.input))

    def test_brute_pythonic(self):

        self.assertListEqual( self.res, self.test_class.build_arrary_pythonic(self.input))

    def test_brute_op(self):

        self.assertListEqual( self.res, self.test_class.build_array_op(self.input))

        

if __name__ == "__main__":

    unittest.main()