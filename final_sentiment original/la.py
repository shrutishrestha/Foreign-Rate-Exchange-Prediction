import csv
with open("afinn.csv", 'r') as file:
    afinn = list(csv.reader(file))
mapp = {}
print(afinn)
print(afinn[0])
print(afinn[0][0])
print(afinn[1][0])
print(afinn[1][1])
afinn_words=[]
for i in range(len(afinn)):
    afinn_words.append(afinn[i][0])
    mapp[afinn[i][0]] = afinn[i][1]
print(afinn_words)
print(mapp)
a="wreck"
if a in afinn_words:
    b=mapp[a]
print("b")
print(b)
