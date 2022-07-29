from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
from numpy import split
import pandas as pd

# plt.style.use('fivethirtyeight')
# plt.xkcd()

data=pd.read_csv('Language_known.csv')
ids=data['ResponseId']
lang_responses=data['LanguageHaveWorkedWith']
language_counter = Counter()
    # row = next(csv_reader)
    # print(row['LanguageHaveWorkedWith'].split(';'))
for response in lang_responses:
    language_counter.update(response.split(';'))



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

plt.legend()
plt.tight_layout( )
# plt.grid(True)


# print(plt.style.available)

plt.show()
