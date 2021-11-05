def jeremy_minimumbribes(q):
    lineorder = list(range(1, len(q)+1))
    count = 0
    flag = 1

    for pos in range(len(q)):
        temporder = lineorder[:]
        if lineorder[pos] != q[pos]:
            orderdifference = abs(pos - lineorder.index(q[pos]))
            if orderdifference > 2:
                print("Too chaotic")
                flag = 0
                break
            elif orderdifference == 2:
                lineorder[pos] = q[pos]
                lineorder[pos + 1] = temporder[pos]
                lineorder[pos + 2] = temporder[pos + 1]
                count += 2
            elif orderdifference == 1:
                lineorder[pos] = q[pos]
                lineorder[pos + 1] = temporder[pos]
                count += 1

    if flag == 1:
        print(f"Final: {lineorder}")
        print(count)

def caroleen_minimumbribes(q):
    if len(q) == 0 or len(q) == 1:
        return 0
    bribes = 0
    print(q)
    for num in range(len(q)):
        print("i: ", num, "q[i] ", q[num])
        if q[num] - (num+1) > 2:
            return "Too chaotic"
        print(range(max(0,q[num]-2), num))
        for num2 in range(max(0,q[num]-2), num):
            print(q[num], "<", q[num2])
            if q[num] < q[num2]:
                bribes += 1
    return bribes

if __name__ == "__main__":
    # Test Cases
    #q = [1,2,3,4,5,6,7]
    #q = [3, 1, 2, 5, 4, 6]

    #q = [2, 1, 5, 3, 4]
    #print("Correct Answer: 3")

    #q = [2, 5, 1, 3, 4]
    #print("Correct Answer: Too Chaotic")

    # q = [5, 1, 2, 3, 7, 8, 6, 4]
    # print("Correct Answer: Too Chaotic")

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    # print("Correct Answer: 7")

    #q = [1, 2, 5, 3, 4, 7, 8, 6]
    # print("Correct Answer: 4")

    # Run program
    #jeremy_minimumbribes(q)

    print(caroleen_minimumbribes(q))
