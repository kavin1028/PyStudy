from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open(u'Walden.txt','r',encoding='utf-8').read()
wordcloud  = WordCloud(
        background_color="white",
        width=1500,
        height=960,
        margin=10,
        ).generate(f)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('my_test2.png')