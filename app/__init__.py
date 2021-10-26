
"""# Prediction"""

def predict(text, model):
     x = cv.transform([text]).toarray() # converting text to bag of words model (Vector)
     lang = model.predict(x) # predicting the language
     if (model.predict_proba(x)[0][lang][0]) < 0.99:
       print(model.predict_proba(x)[0][lang][0])
       print('Language not detected')
     else:
       lang = le.inverse_transform(lang) # finding the language corresponding the the predicted value
       print("The langauge is in",lang[0]) # printing the language

text = "लड़के"
prep_text = re.sub(r'[!@#$(),"%^*?:;~`0-9]', '', text)
prep_text = re.sub(r'[[]]', ' ', prep_text)
prep_text = prep_text.lower()
predict(prep_text, KNNclssifier)

prep_text

