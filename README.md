# Semantic-Search-Engine-For-Pharmaceuticals 


A web-based search engine where user can input queries related to diseases, its symptoms, medications, useful related links, for example,
_‘What are the symptoms of leukaemia?’ 
Results: Knee joints pain, bleeding
‘What medications are required in leukaemia?’
Results: Chemotherapy, Blood Transfusion_

<img width=160 height=100 src="https://cdn.lowgif.com/full/814b0234e680a1dd-7-types-of-medical-degrees-with-related-jobs-education-today-news.gif"/>


**Modules:**

**1.	Text based search:** 
We will implement text based search with semantic search via NLP based query processing and pattern matching from database in backend SQL.

•	Partial search: If a user types “leukae” in search bar, the search engine will suggest leukaemia in a dropdown menu. (Auto completion)

•	Suggested search: If a user queries, ‘Heptis B’ instead of ‘Hepatitis B’, it will use pattern matching to suggest ‘Did you mean Hepatitis B?’ (Auto correction)

•	Recent search: The UI interface will show option for recent search, which will show recent search queries.

**2.	Audio search:**
We will implement audio based search using Speech to Text processing and show the desired outputs if it matches in our database.

**3.	Image search:**
Suppose a user uploads a picture of medicine ‘Dextromethorphan’
We will implement OCR or Optical Character Recognition that will try to generate text from image and show the desired outputs if it matches in our database.

**_Technical requirements:_**
Frontend: Search engine website using Django 
Backend: Python, Natural Language Processing and Machine Learning, Speech to Text, OCR
DBMS: Using sqlite or Apache SOLR
Dataset can be used from Kaggle

