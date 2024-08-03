import numpy as np
import pandas as pd
import hazm
import math
from hazm.utils import stopwords_list
stopwords_list = hazm.stopwords_list()
BoW = {"کلیات اسلام":{}, "مدیریت و کسب و کار":{}, "داستان کودک و نوجوانان":{}, "رمان":{}, "داستان کوتاه":{}, "جامعه‌شناسی":{}}
cats = ["کلیات اسلام", "مدیریت و کسب و کار", "داستان کودک و نوجوانان", "رمان", "داستان کوتاه", "جامعه‌شناسی"]
PersianPuncs = ['،' , '؛' , 'ـ' , '-' , '٫' , '٬' , ',', '.', ')', '(', '٪' '«', '،', '»' , '«'  , '…'  , '!' , '؟']
Numbers = ['۵' ,'۶' , '۷' , '۸' ,'۹' , '۰' , '۱' , '۲' , '۳' , '۴']

lem = hazm.Lemmatizer().lemmatize
def lemmetize(Array):
  for word in Array:
    word = lem(word)
  return Array
def delete_stop_words(Array):
  temp = []
  for word in Array:
    if word not in stopwords_list:
      temp.append(word)
  return temp
def delete_chars(Array):
  temp = []
  for word in Array:
    if word not in PersianPuncs:
      temp.append(word)
  return temp
def delete_numbers(Array):
  temp = ''
  for word in Array:
    if word not in Numbers:
      temp = temp + word
  return temp

def pre_process(column):
  column = column.apply(hazm.Normalizer().normalize)
  column = column.apply(delete_numbers)
  column = column.apply(hazm.WordTokenizer().tokenize)
  column = column.apply(delete_chars)
  column = column.apply(delete_stop_words)
  column = column.apply(lemmetize)
  return column

def create_bow(words, cats):
  for w in words:
    if w not in BoW[cats].keys():
      BoW[cats][w] = 0.01
    else:
      BoW[cats][w] +=1

train = pd.read_csv('books_train.csv')
test = pd.read_csv('books_test.csv')

train['all_words'] = train['title'] + train['description']
train["all_words"] = pre_process(train["all_words"])
test['all_words'] = test['title'] + test['description']
test["all_words"] = pre_process(test["all_words"])

for _, row in train.iterrows():
  create_bow(row['all_words'], row['categories'])

BoW_words_count = 0
for word in BoW:
  BoW_words_count +=1

def index_to_category(index):
  if index == 0 : return "کلیات اسلام"
  elif index == 1 : return "مدیریت و کسب و کار"
  elif index == 2 : return "داستان کودک و نوجوانان"
  elif index == 3 : return "رمان"
  elif index == 4 : return "مدیریت و کسب و کار" 
  elif index == 5 : return "جامعه‌شناسی"

def count_words_in_cat(cat):
  sum = 0
  for item in cat.keys():
    sum = sum + cat[item]
  return sum

def calculate_probability():
  count = 0
  for item, row in test.iterrows():
    best_index = 0
    best = -99999999999999999999999999999999999
    for i in range(6):
      result = 0
      bow_cat_keys = BoW[cats[i]].keys()
      index_catgory = index_to_category(i)
      full_in_cat = count_words_in_cat(BoW[index_catgory])
      for word in row['all_words']:
        if word in bow_cat_keys:
          result = result + math.log(BoW[cats[i]][word] / full_in_cat)
        else:
          result = result + math.log(0.01 / full_in_cat)
      if best < result:
        best = result
        best_index = i
    if(row['categories'] == index_to_category(best_index)):
          count = count + 1
  print(count/len(test)*100)
calculate_probability()