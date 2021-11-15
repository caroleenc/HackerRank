# Write your code here
#n = 7
#c = [0, 0, 1, 1, 1, 1, 0]
n = 100
c = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

# n = 6
# c = [0, 0, 0, 1, 0, 0]

count = 0
flag = 0
clouds = list(range(0, n))
temp_clouds = clouds[:]
for index, thunder in enumerate(temp_clouds):
    if c[index] == 1:
        clouds.remove(thunder)
print(clouds)

if len(clouds) <= 2:
    count += 1
else:
    for index, cloud in enumerate(clouds):
        print(index, len(clouds), cloud, count)
        if index == (len(clouds) - 2):
            count += 1
            break
        else:
            if flag == 1:
                flag = 0
                continue
            else:
                count += 1
                diff_current = clouds[(index + 1)] - clouds[index]
                diff_next = clouds[(index + 2)] - clouds[(index + 1)]
                print(diff_next, diff_current)
                if diff_current == 1 and diff_next == 1:
                    flag = 1

print(count)


#[0, 1, 3, 4, 6]
#[1, 2, 1, 2, 0]