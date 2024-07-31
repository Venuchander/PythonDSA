# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1

# method 1
nums = [2,2,1]

dup = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            dup.append(nums[i])
            
set1 = set(dup)
set2 = set(nums)

unique_to_list1 = set2 - set1
unique_list = list(unique_to_list1)

for item in unique_list:
    print(int(item))
    
    
    
# method 2
nums = [2,2,1]
unique = 0
for num in nums:
    unique ^= num
print(unique)