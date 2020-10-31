import pandas as pd
df = pd.read_csv("search_engine/static/csv/symptom_Description.csv")
print(df)
'''
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'diseases.html', context)'''

