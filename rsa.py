##################################
# 2021.11.21 QuizKnock と学ぼう
# 須貝と作れるようになるLIVE「プログラミングを始めよう！」
##################################
def main():
    p = 37
    q = 71
    e = 79
    c = 904 # 暗号文

    n = calc_n(p, q)
    print(n)

    m = calc_m(e, p, q)
    print(m)

    d = calc_d(m, p, q, e)
    print(d)

    M = calc_M(c, d, n)
    print(M)

def calc_n(p, q):
    return p * q

def calc_m(e, p, q):
    for i in range(e):
        if i * (p - 1) * (q - 1) % e == e - 1:
            m = i
            break
    return m

def calc_d(m, p, q, e):
    return (m * (p - 1)*(q - 1) + 1) // e

def calc_M(c, d, n):
    return (c**d) % n

main()
