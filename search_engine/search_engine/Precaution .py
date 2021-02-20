import numpy as np
import pandas as pd
from nltk.corpus import stopwords


symptoms = pd.read_csv("dataset/Symptom-severity.csv")
precautions = pd.read_csv("dataset/disease_precaution.csv")
description = pd.read_csv("dataset/disease_Description.csv")
dataset = pd.read_csv("dataset/dataset.csv")


word_list = "tell me description of Allergy"
filtered_words = [word for word in word_list.split(" ") if word not in stopwords.words('english')]

joined = " ".join(filtered_words)

s = ''
if any(word in ['symptoms', 'symptom'] for word in filtered_words):
    if "symptom" in filtered_words:
        s = joined.split("symptom", 1)[1]
    elif "symptoms" in filtered_words:
        s = joined.split("symptoms", 1)[1]
    # print(s.lstrip().rstrip())
s = s.lstrip().rstrip()
for i, ch in enumerate(list(dataset["Disease"].values)):
    #     print(i.lower())
    if s == ch.lower():
        print(i)
        sympt = list(dataset.iloc[0, 1:].values)
        print(sympt)
        break

s = ''
if any(word in ['precaution', 'precautions'] for word in filtered_words):
    if "precaution" in filtered_words:
        s = joined.split("precaution", 1)[1]
    elif "precautions" in filtered_words:
        s = joined.split("precautions", 1)[1]
s = s.lstrip().rstrip()
for i, ch in enumerate(list(precautions["Disease"].values)):
    if s == ch.lower():
        print(i)
        preca = list(precautions.iloc[0, 1:].values)
        print(preca)
        break

s = ''
if any(word in ['description'] for word in filtered_words):
    if "description" in filtered_words:
        s = joined.split("description", 1)[1]
s = s.lstrip().rstrip()
for i, ch in enumerate(list(description["Disease"].values)):
    if s == ch.lower():
        print(i)
        desa = list(description.iloc[0, 1:].values)
        print(desa)
        break
print(desa)