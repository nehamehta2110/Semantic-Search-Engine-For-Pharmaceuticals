from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import json


def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')


def diseases(request):
    df = pd.read_csv("C://Users/HP/PycharmProjects/Semantic-Search-Engine-For-Pharmaceuticals/search_engine/static/csv/symptom_Description.csv")
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'diseases.html', context)