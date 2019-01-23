# Walden文件
import wordcloud

f = open('Walden.txt', 'r')
text = f.read()
f.close()
text = text.lower()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.replace("/", " ")
text = text.replace("?", " ")
text = text.replace(";", " ")
text = text.replace("\n", " ")
text = text.replace(" ", " ")
li = text.split()
dt = {}
for i in li:
    print(i)