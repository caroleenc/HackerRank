n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

pairs = {i: ar.count(i) for i in ar}

count = 0
for pair in pairs.values():
    counting_pairs = pair // 2
    count += counting_pairs

print(pairs)
print(count)