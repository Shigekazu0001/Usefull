import csv
import pprint
from googletrans import Translator
import time
import pandas as pd
translator = Translator()
lists=[]
translatedlist=[]

with open('英語全単語.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        lists.append(row)

i=len(lists)

for j in range(i):
    time.sleep(1)
    Target=str(lists[j])
