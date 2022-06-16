from pyrsistent import m, v


max_value = 0
max_weight = 0
max_n = 0
things = []

def get_info():
    global max_weight, things, max_n, bool_things
    n, weight = input().split(' ')
    max_n = int(n)
    max_weight = int(weight)
    for i in range(max_n):
        w, v = input().split(' ')
        things.append([int(w),int(v)])
    backpack(0,0,-1)
        
def backpack(weight, value, index):
    global max_value, max_n, things, max_weight
    if index >= max_n:
        return
    if index >= 0:
        weight += things[index][0]
        if weight > max_weight:
            return
        value += things[index][1]
        if value > max_value:
            max_value = value
    for i in range(index+1, max_n):
        backpack(weight, value, i)
        
    
if __name__ == '__main__':
    get_info()
    print(max_value)