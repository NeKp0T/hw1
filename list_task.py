# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    if not lst:
        return lst

    ans = [lst[0]]
    for i in lst[1:]:
        if ans[-1] != i:
            ans.append(i)

    return ans

# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    lst = [lst1, lst2]
    ans = []
    ind = [0] * 2

    while ind[0] < len(lst[0]) and ind[1] < len(lst[1]):
        if lst[ind[0]] > lst[ind[1]]:
            add_from = 1
        else:
            add_from = 0

        ans.append(lst[add_from])
        ind[add_from] += 1

    for i in [0, 1]:
        for j in lst[i][ind[i]:]:
            ans.append(j)
            
    return ans
