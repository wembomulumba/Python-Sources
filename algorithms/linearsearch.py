data = [2,4,1,5,10,8,9,22,251,25,33,37]
target = 5

# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False        
print(linear_search(data, target))
