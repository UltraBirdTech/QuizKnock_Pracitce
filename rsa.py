##################################
# 2021.11.21 QuizKnock と学ぼう
# 須貝と作れるようになるLIVE「プログラミングを始めよう！」
# RSA 暗号をプログラムで解いてみる。
##################################
import re

def main():
    p = 37
    q = 71
    e = 79
    c = 904 # 暗号文

    n = calc_n(p, q)
    print("n: " + str(n))

    m = calc_m(e, p, q)
    print("m: " + str(m))

    d = calc_d(m, p, q, e)
    print("d: " + str(d))

    M = calc_M(c, d, n)
    print("M: " + str(M))

    exchange_M_to_str(M)

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

def exchange_M_to_str(m):
    alphabet_dict = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
    }
    result_str = ''
    for s in  list(filter(None, re.split('(..)', str(m)))):
        result_str += alphabet_dict.get(int(s))
    print('RESULT: ' + result_str)

main()
