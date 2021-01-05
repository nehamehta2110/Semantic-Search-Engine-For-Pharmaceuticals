import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import strip_multiple_whitespaces, strip_numeric, strip_punctuation
from gensim.parsing.preprocessing import strip_non_alphanum, strip_short

symptoms = pd.read_csv("C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/Symptom-severity.csv")
precautions = pd.read_csv("C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/disease_precaution.csv")
description = pd.read_csv("C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/disease_Description.csv")
dataset = pd.read_csv("C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/dataset.csv")


def get_result(word_list):
    # word_list = "tell me description of Allergy"
    rare_words = ['what', 'is', 'are', 'the', 'can', 'you', 'tell', 'me', 'of',
                  'mon', 'tue', 'wed',
                  'sat', 'sun', 'month', 'day', 'year', 'thursday', 'january',
                  'february', 'march', 'april',
                  'june', 'july', 'august', 'september', 'october', 'november',
                  'december', 'friday', 'saturday',
                  'sunday', 'thursday', 'monday', 'tuesday', 'wednesday', 'date',
                  'week', 'daily', 'feb',
                  'september', 'morning', 'evening', 'years', 'weeks', 'till', 'ago',
                  'will', 'werent',
                  'whom', 'three', 'first', 'twice']

    filtered_words = [word for word in word_list.split(" ") if
                      word not in stopwords.words('english') and word not in rare_words]

    joined = " ".join(filtered_words)
    joined = strip_punctuation(joined)
    joined = strip_short(joined)
    joined = strip_numeric(joined)
    joined = strip_non_alphanum(joined)
    joined = strip_multiple_whitespaces(joined)

    s = ''
    if any(word in ['symptoms', 'symptom', 'signs', 'sign'] for word in filtered_words):
        if "symptom" in filtered_words:
            s = joined.split("symptom", 1)[1]
        elif "symptoms" in filtered_words:
            s = joined.split("symptoms", 1)[1]
        elif "sign" in filtered_words:
            s = joined.split("sign", 1)[1]
        elif "signs" in filtered_words:
            s = joined.split("signs", 1)[1]
        # print(s.lstrip().rstrip())
    s = s.lstrip().rstrip()
    for i, ch in enumerate(list(dataset["Disease"].values)):
        if s.lower() == ch.lower():
            sympt = list(dataset.iloc[i, 1:].values)
            sympt = [x for x in sympt if str(x) != 'nan']
            return sympt

    s = ''
    if any(word in ['precaution', 'precautions'] for word in filtered_words):
        if "precaution" in filtered_words:
            s = joined.split("precaution", 1)[1]
        elif "precautions" in filtered_words:
            s = joined.split("precautions", 1)[1]
    s = s.lstrip().rstrip()
    for i, ch in enumerate(list(precautions["Disease"].values)):
        if s.lower() == ch.lower():
            preca = list(precautions.iloc[i, 1:].values)
            return preca

    s = ''
    if any(word in ['description'] for word in filtered_words):
        if "description" in filtered_words:
            s = joined.split("description", 1)[1]
    s = s.lstrip().rstrip()
    for i, ch in enumerate(list(description["Disease"].values)):
        if s.lower() == ch.lower():
            desa = list(description.iloc[i,0:].values)
            return desa

    default = ['No result found']
    return default