##################################
# 2021.11.21 QuizKnock と学ぼう
# 須貝と作れるようになるLIVE「プログラミングを始めよう！」
# RSA 暗号をプログラムで解いてみる。
##################################
import re
import string

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

    result_str = exchange_M_to_str(M)
    print('RESULT: ' + result_str)

# p * q を行い n の値を求める
def calc_n(p, q):
    return p * q

# m(p -1)(q-1) = -1(mod e) となるような最小の自然数mを求める
# (m * 36 * 70) / 79 の余りが78になる最小の自然数mを求める
def calc_m(e, p, q):
    for i in range(e):
        if i * (p - 1) * (q - 1) % e == e - 1:
            return i

# d を求める
def calc_d(m, p, q, e):
    return (m * (p - 1)*(q - 1) + 1) // e

# c の d 乗を n で割る
def calc_M(c, d, n):
    return (c**d) % n

def exchange_M_to_str(m):
    alphabet_list = list(string.ascii_uppercase) # Python の string を使い、大文字のアルファベットのリストを作る
    result_str = ''
    for s in list(filter(None, re.split('(..)', str(m)))): # m を2文字ずつlistに入れる。''をfilter()で取り除く。
        result_str += alphabet_list[int(s) - 1]
    return result_str

main()
