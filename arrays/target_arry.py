"""Create Target Array in Given Order"""


nums = [0,1,2,3,4]
index = [0,1,2,2,1]
res = [nums[0]]
c = 1

for i in index[1:]:
    res = res[:i] + [nums[c],] + res[i:]
    c+= 1
    print(res)