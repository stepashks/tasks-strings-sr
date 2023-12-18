a = input()
words = []
while a != "стоп":
    words.append(a)
    a = input()
max, min = max(words, key=Len), min(words, key=Len)
if set(ma).issuperset(set(mi)):
    print("ДА")
else
    print("Нет")
