from math import sqrt
def prime_num(m, n):
    prime_bool = [True for i in range(n+1)]

    for i in range(2, int(sqrt(n)) + 1):
        if prime_bool[i] == True:
            j = 2
            while i * j <= n:
                prime_bool[i*j] = False
                j += 1
    for i in range(m, n+1):
        if i == 1:
            continue
        if prime_bool[i]:
            print(i)

if __name__ == '__main__':
    numbers = input()
    M, N = numbers.split(' ')
    prime_num(int(M), int(N))