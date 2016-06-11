# 必要な格子点を出力するためのプログラム
def fwrite(f, a, b):
    f.write("{0} {1}\n".format(a, b))

p = 11
q = 7

f = open('eisenstein-1.table', 'w')
for i in range(1, (p-1) // 2 + 1):
    for j in range(1, q):
        if j < 2*i*q / p:
            fwrite(f, 2*i, j)
f.close()

f = open('eisenstein-2.table', 'w')
for i in range(1, (p-1) // 2 + 1):
    if 2*i > p / 2:
        for j in range(1, q):
            if j > 2*i*q / p:
                fwrite(f, 2*i, j)
f.close()

f = open('eisenstein-3.table', 'w')
for i in range (0, (p-1) // 2):
    if 2*i + 1 < p / 2:
        for j in range(1, q):
            if j < (2*i + 1)*q / p:
                fwrite(f,2*i + 1, j)
f.close()
