##################################
# 2021.11.21 QuizKnock と学ぼう
# 須貝と作れるようになるLIVE「プログラミングを始めよう！」
# RSA 暗号をプログラムで解いてみる。
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

# p * q を行い n の値を求める
def calc_n(p, q):
    return p * q

# m(p -1)(q-1) = -1(mod e) となるような最小の自然数mを求める
# (m * 36 * 70) / 79 の余りが78になる最小の自然数mを求める
def calc_m(e, p, q):
    for i in range(e):
        if i * (p - 1) * (q - 1) % e == e - 1:
            m = i
            break
    return m

# d を求める
def calc_d(m, p, q, e):
    return (m * (p - 1)*(q - 1) + 1) // e

# c の d 乗を n で割る
def calc_M(c, d, n):
    return (c**d) % n

main()
