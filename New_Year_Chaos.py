# t = number of cases
# n = length of list
# q = list of sequence

# t = 2, n = 5, q = [2, 1, 5, 3, 4]
# q = [2, 1, 5, 3, 4]
# print("Correct Answer: 3")

# q = [2, 5, 1, 3, 4]
# print("Correct Answer: Too Chaotic")

# q = [5, 1, 2, 3, 7, 8, 6, 4]
# print("Correct Answer: Too Chaotic")

# q = [1, 2, 5, 3, 7, 8, 6, 4]
# print("Correct Answer: 4")

# q = [1, 2, 5, 3, 4, 7, 8, 6]
# print("Correct Answer: 4")



def swap(lineorder, num):
    currentpos = lineorder.index(num)
    nextpos = currentpos - 1
    tempnextnum = lineorder[nextpos]
    lineorder[nextpos] = num
    lineorder[currentpos] = tempnextnum


def minimumbribes(q):
    lineorder = []
    count = 0
    flag = 1
    for i in range(len(q)):
        lineorder.append(i+1)

    for pos in range(len(q)):
        if lineorder[pos] != q[pos]:
            orderdifference = abs(pos - lineorder.index(q[pos]))
            if orderdifference > 2:
                print("Too chaotic")
                flag = 0
                break
            else:
                for j in range(orderdifference):
                    print(lineorder)
                    swap(lineorder, q[pos])
                    count += 1
    if flag == 1:
        print(f"Final: {lineorder}")
        print(count)


if __name__ == "__main__":
    # Test Cases

    # q = [2, 1, 5, 3, 4]
    # print("Correct Answer: 3")

    # q = [2, 5, 1, 3, 4]
    # print("Correct Answer: Too Chaotic")

    # q = [5, 1, 2, 3, 7, 8, 6, 4]
    # print("Correct Answer: Too Chaotic")

    # q = [1, 2, 5, 3, 7, 8, 6, 4]
    # print("Correct Answer: 7")

    q = [1, 2, 5, 3, 4, 7, 8, 6]
    print("Correct Answer: 4")

    # Run program
    minimumbribes(q)
