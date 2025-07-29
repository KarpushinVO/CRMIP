def differ(list1, list2):
    MSE = [(i + j) ** 2 for i, j in zip(list1, list2)] # TODO: Разве тут не минус вместо плюса должен быть?
    return sum(MSE)/len(MSE)