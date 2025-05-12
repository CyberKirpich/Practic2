J = 'ab'
S = 'aabbcod'
count = 0
for char in S:
    if char in J:
        count += 1
print(count)
