# given a list of heights, find the average student height. round it up to the next integer. can't use len() or sum()

def one(heights):
    avg = 0.0
    count = 0

    for height in heights:
        avg += height
        count += 1

    return round((avg / count))


heights = [180, 124, 165, 173, 189, 169, 146]
print(one(heights))
