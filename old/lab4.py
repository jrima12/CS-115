items = [[2,100],[3,112],[4,125]]

def knapsack(capacity, itemList):
    ''' returns a list of the maximum value of itemList without going over the capacity '''
    if capacity == 0 or itemList ==[]:
        return [0, []]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        total = itemList[0][1] + use[0]
        if total > lose[0]:
            return [total, [itemList[0]]+use[1]]
        return lose
