def counting_valleys(steps: int, path: str):
    """
    steps: the number of steps on the hike
    path: a string describing the path
    """
    height = 0
    change = 0

    for i in path:
        if i == "U":
            height += 1
        else:
            height -= 1

        if height == 0 and i == "U":
            change += 1
    # print(change)
    return change
