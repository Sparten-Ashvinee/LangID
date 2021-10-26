# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

dir_path = '/content/drive/MyDrive/LID/data/'
file1 = dir_path+'data-bn.txt'
file2 = dir_path+'data-hi.txt'
file3 = dir_path+'data-ta.txt'
file4 = dir_path+'data-te.txt'
file5 = dir_path+'data-ur.txt'

fin1 = open(file1, 'r', encoding='utf8')
fin2 = open(file2, 'r', encoding='utf8')
fin3 = open(file3, 'r', encoding='utf8')
fin4 = open(file4, 'r', encoding='utf8')
fin5 = open(file5, 'r', encoding='utf8')

data=[]
lang=[]

for count,line in enumerate(fin1.readlines()):
  if count == 40165:
    break
  data.append(line.split('\t')[0])
  lang.append('bn')
fin1.close()
for count,line in enumerate(fin2.readlines()):
  if count == 40165:
    break
  data.append(line.split('\t')[0])
  lang.append('hi')
fin2.close()
for count,line in enumerate(fin3.readlines()):
  if count == 40165:
    break
  data.append(line.split('\t')[0])
  lang.append('ta')
fin3.close()
for count,line in enumerate(fin4.readlines()):
  if count == 40165:
    break
  data.append(line.split('\t')[0])
  lang.append('te')
fin4.close()
for count,line in enumerate(fin5.readlines()):
  if count == 40165:
    break
  data.append(line.split('\t')[0])
  lang.append('ur')
fin5.close()

len(data), len(lang)

data[50000]

lang[50000]


column = ['Data', 'Lang']
df_data = pd.DataFrame({'Data':data, 'Lang':lang})


#Generate CSV file


'''
file = open('modelp.pkl', 'wb')
pickle.dump(model, file)
file.close()

"""# Load model"""

file2 = open('modelp.pkl', 'rb')
new_model = pickle.load(file2)
file2.close
'''

