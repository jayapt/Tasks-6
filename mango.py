def man(n, m):
    res = 1

    if m > n - m:
        m = n - m

    for i in range(0, m):
        res *= (n - i)
        res /= (i + 1)

    return res

def calculate(n, m):

    if n<m:
        return 0

    ways = man(n + m-1, n-1)
    return int(ways)

if __name__ == "__main__":

    m = 7 ;n = 5

    result = calculate(m,n)
    print(result)

