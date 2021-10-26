

column = ['Data', 'Lang']
df_data = pd.DataFrame({'Data':data, 'Lang':lang})

X = df_data["Data"]
y = df_data["Lang"]

# Label Encoder"""

le = LabelEncoder()
y = le.fit_transform(y)


'''
PRE_PROCESSING.PY
'''


# Steaming and Lemmatization
### Root words
#Bag of Words (Count Vectorizer)"""

cv = CountVectorizer(analyzer='char')                            #analyzer='char',ngram_range=(2, 2), min_df=1
X = cv.fit_transform(data_list) #.toarray()
X.shape # (10337, 39419)

# TF-IDF"""

tfidfv = TfidfVectorizer(analyzer='char')                            #analyzer='char',ngram_range=(2, 2), min_df=1
X = cv.fit_transform(data_list) #.toarray()
X.shape # (10337, 39419)

# Word2Vec

