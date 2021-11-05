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
    
    current = 0
    next = 1
    total_bribes = 0
    return compare_values(q, current, next, total_bribes)
        
def compare_values(q, current, next, total_bribes):
    print(current, next)
    if next == len(q):
        return total_bribes
    elif current == next:
        return compare_values(q, current, next+1, total_bribes)
    else:
        print(q[current], q[next], total_bribes)
        if q[next] - q[current] == 1:
            print("Sequential", q[current], q[next], total_bribes)
            return compare_values(q, current+1, next+1, total_bribes+0)
        elif q[next] - q[current] == -1:
            print("Partner number", q[current], q[next], total_bribes)
            return compare_values(q, current+1, next, total_bribes+1)
        elif q[next] - q[current] < 0:
            print("Current is greater", q[current], q[next], total_bribes)
            return compare_values(q, current, next+1, total_bribes+1)
        elif q[next] - q[current] > 0:
            print("Current is less", q[current], q[next], total_bribes)
            return compare_values(q, current+1, next+1, total_bribes+0)

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

    # q = [1, 2, 5, 3, 4, 7, 8, 6]
    # print("Correct Answer: 4")

    # Run program
    #jeremy_minimumbribes(q)

    print(caroleen_minimumbribes(q))
