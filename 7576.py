def tomato():
    col, row = input().split(' ')
    col = int(col)
    row = int(row)
    box = [[0]*col for i in range(row)]
    for i in range(row):
        nrow = input()
        for j in range(col):
            if j == col - 1:
                num = nrow
            else:
                num, nrow = nrow.split(' ', 1)
            box[i][j] = int(num)

def ripe(box, row, col, n):

if __name__ == '__main__':
    tomato()