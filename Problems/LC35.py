# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4


nums = [1, 3, 5, 6]
target = 7

for i in range(len(nums)):
    if nums[i] == target:
        print(i)
        break
    elif nums[i] > target:
        print(i)
        break
else:
    print(len(nums))
