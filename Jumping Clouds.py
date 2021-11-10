# Write your code here
n = 7
c = [0, 0, 1, 0, 0, 1, 0]

# n = 6
# c = [0, 0, 0, 1, 0, 0]

count = 0
clouds = list(range(0, n))
temp_clouds = clouds[:]
for index, thunder in enumerate(temp_clouds):
    if c[index] == 1:
        clouds.remove(thunder)
print(clouds)

for index, cloud in enumerate(clouds):
    if

[0, 1, 3, 4, 6]
[1, 2, 1, 2, 0]