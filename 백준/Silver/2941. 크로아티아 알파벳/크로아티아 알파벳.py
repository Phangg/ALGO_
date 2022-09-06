cro_alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for ap in cro_alp:
    if ap in word:
        word = word.replace(ap, '*')

print(len(word))