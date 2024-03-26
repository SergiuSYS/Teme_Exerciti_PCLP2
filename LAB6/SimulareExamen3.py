'''
nums = [1, 3, 4, 6, 6, 7]

hashSet = set()
duplicates = set()

for n in nums:
    if n not in hashSet:
        pass
    else:
        duplicates.add(n)
    hashSet.add(n)
hashSet -= duplicates

print(hashSet)
'''
