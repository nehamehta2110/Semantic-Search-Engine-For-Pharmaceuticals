from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import json
from . import text_search


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def diseases(request):
    df = pd.read_csv(
        "C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/symptom_Description.csv")
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'diseases.html', context)


def symptoms(request):
    df1 = pd.read_csv(
        "C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/Symptom-severity.csv")
    json_records1 = df1.reset_index().to_json(orient='records')
    data1 = []
    data1 = json.loads(json_records1)
    context1 = {'d': data1}

    return render(request, 'symptoms.html', context1)


def results(request):
    fulltext = request.GET['queryinput']
    print(fulltext)
    answer = text_search.get_result(fulltext)

    # answer = "This would be the answer"
    return render(request, 'results.html', {'fulltext': fulltext, 'result': answer})


def us(request):
    return render(request, 'us.html')
