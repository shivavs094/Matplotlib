from matplotlib import pyplot as plt
import  matplotlib
import numpy as np
import csv
from collections import Counter
from numpy import split

plt.style.use('fivethirtyeight')
# plt.xkcd()

with open ('Language_known.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    language_counter = Counter()
    # row = next(csv_reader)
    # print(row['LanguageHaveWorkedWith'].split(';'))


    for row in csv_reader:
        language_counter.update(row ['LanguageHaveWorkedWith'].split(';'))

language=[]
popularuty=[]

for item in language_counter.most_common(15):
    language.append(item[0])
    popularuty.append(item[1])


# print(language)
# print(popularuty)

language.reverse()
popularuty.reverse()

plt.barh(language,popularuty)

plt.xlabel('Number of people known')
plt.ylabel('programming language')
plt.title('Most popular language')

plt.savefig('Mat_1.png')

matplotlib.pyplot.legend()
plt.tight_layout()
# plt.grid(True)


# print(plt.style.available)

plt.show()
