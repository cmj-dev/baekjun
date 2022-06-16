def sugar(n):
    max = int(n/5)
    left = n%5
    while left%3 != 0:
        if max == 0:
            return -1
        max -= 1
        left += 5
    return int(max + left/3)

if __name__ == '__main__':
    num = input()
    print(sugar(int(num)))