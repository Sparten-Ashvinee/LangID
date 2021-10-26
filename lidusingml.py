# -*- coding: utf-8 -*-


!pip install mlflow --quiet

import pandas as pd
import numpy as np
import re
import pickle
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

from sklearn import metrics
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import mlflow
import mlflow.sklearn

mlflow.set_experiment(experiment_name='MLflow on Colab')


# Train Test Splitting

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

"""# K-Fold"""

"""# Model Training and Prediction

### NB
"""



"""### SVC"""


"""## KNN"""


"""# Model Evaluation"""


"""# Tensorflow model"""


model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=[tf.metrics.BinaryAccuracy(threshold=0.0, name='accuracy')])


history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=10,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)

"""# Keras model"""


"""# MLFlow"""

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

with mlflow.start_run():
  SVMclssifier = svm.SVC()
  SVMclssifier.fit(x_train, y_train)
  y_pred = SVMclssifier.predict(x_test)
  (rmse, mae, r2) = eval_metrics(y_test, y_pred)

  #print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
  print("  RMSE: %s" % rmse)
  print("  MAE: %s" % mae)
  print("  R2: %s" % r2)

  #mlflow.log_param("alpha", alpha)
  #mlflow.log_param("l1_ratio", l1_ratio)
  mlflow.log_metric("rmse", rmse)
  mlflow.log_metric("r2", r2)
  mlflow.log_metric("mae", mae)

  mlflow.sklearn.log_model(SVMclssifier, "model")

"""# Confusion matrix"""

"""# Save model in pickel"""


"""# Visualization"""



"""# MLFlow Visualization"""



print(mlflow.__version__)


'''
# run tracking UI in the background
get_ipython().system_raw("mlflow ui --port 5000 &")# run tracking UI in the background

# create remote tunnel using ngrok.com to allow local port access
# borrowed from https://colab.research.google.com/github/alfozan/MLflow-GBRT-demo/blob/master/MLflow-GBRT-demo.ipynb#scrollTo=4h3bKHMYUIG6
!pip install pyngrok --quiet
from pyngrok import ngrok
from getpass import getpass
# Terminate open tunnels if exist
ngrok.kill()

# Setting the authtoken (optional)
# Get your authtoken from https://dashboard.ngrok.com/auth
NGROK_AUTH_TOKEN = ''
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Open an HTTPs tunnel on port 5000 for http://localhost:5000
public_url = ngrok.connect(port="5000", proto="http", options={"bind_tls": True})
print("MLflow Tracking UI:", public_url)

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/mlruns/
!mlflow ui
'''
