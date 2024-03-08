from osztaly import Tarskereso

emberek: list[Tarskereso] = []

f = open('emberek.csv', 'r', encoding='utf-8')
for sor in f:
    emberek.append(Tarskereso(sor))
f.close()

