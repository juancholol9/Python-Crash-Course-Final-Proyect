import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

file_path = r"C:\Users\juanr\Desktop\Carpetas\PROGRAMACION\PYTHON\Crash Course on Python\Python-Crash-Course-Final-Proyect\text.txt"
with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()

stopwords = STOPWORDS

wc = WordCloud(
    background_color='white',
    height=600,
    width=400,
    stopwords=stopwords
)

dicc = {}
for word in data.split():
    word = word.lower()
    word = re.sub(r'[-.,?;—!\']', '', word)
    if word not in dicc or len(word) <= 4:
        dicc[word] = 1
    else:
        dicc[word] += 1

wc.generate_from_frequencies(dicc)

wc.to_file("myfile.jpg")

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
