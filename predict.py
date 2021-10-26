
"""# Prediction"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import re

cv = TfidfVectorizer(analyzer='char')  
le = LabelEncoder()

class UnetInferrer:
	def __init__(self):
		text = "लड़के"
		self.saved_path = '/home/aisummer/src/soft_eng_for_dl/saved_models/unet'
        	self.model = tf.saved_model.load(self.saved_path)
		
	def predict(text, model):
		prep_text = re.sub(r'[!@#$(),"%^*?:;~`0-9]', '', text)
		prep_text = re.sub(r'[[]]', ' ', prep_text)
		prep_text = prep_text.lower()
		predict(prep_text, KNNclssifier)
     		x = cv.transform([text]).toarray() # converting text to bag of words model (Vector)
     		lang = model.predict(x) # predicting the language
     		if (model.predict_proba(x)[0][lang][0]) < 0.99:
       		print(model.predict_proba(x)[0][lang][0])
       		return('Language not detected')
     		else:
       		lang = le.inverse_transform(lang) # finding the language corresponding the the predicted value
       		return("The langauge is in",lang[0]) # printing the language

	



