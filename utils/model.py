import tensorflow as tf
import tensorflow_hub as hub


class knn:

  KNNclssifier = KNeighborsClassifier()
  KNNclssifier.fit(x_train, y_train, cv=skfold)

  y_pred = KNNclssifier.predict(x_test)

  ac = accuracy_score(y_test, y_pred)
  cm = confusion_matrix(y_test, y_pred)

  print("Accuracy is :",ac*100)

  
class svm_model:
    
    skfold = StratifiedKFold(n_splits=10, random_state=100)
    NBclassifier = svm.SVC()
    results_skfold = cross_val_score(NBclassifier, x_train, y_train, cv=skfold)
    print("Accuracy: %.2f%%" % (results_skfold.mean()*100.0))



    '''
    SVMclssifier = svm.SVC()
    SVMclssifier.fit(x_train, y_train, cv=skfold)

    y_pred = SVMclssifier.predict(x_test)

    ac = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Accuracy is :",ac*100)
    '''

class nb_model:

    NBclassifier = MultinomialNB()
    NBclassifier.fit(x_train, y_train)

    y_pred = results_skfold.predict(x_test)

    ac = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Accuracy is :",ac*100)
    
    
class tf-model:
    model = "https://tfhub.dev/google/nnlm-en-dim128-with-normalization/2" #"https://tfhub.dev/google/nnlm-en-dim50/2"
    hub_layer = hub.KerasLayer(model, input_shape=[], dtype=tf.string, trainable=True)
    hub_layer(data_list[:3])

    model = tf.keras.Sequential()
    model.add(hub_layer)
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(5))

    model.summary()
    
    
class lstm_model:    
    input_size = 152860

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(500,input_dim=input_size, kernel_initializer="glorot_uniform", activation="sigmoid"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(300, kernel_initializer="glorot_uniform", activation="sigmoid"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(100, kernel_initializer="glorot_uniform", activation="sigmoid"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(5,kernel_initializer="glorot_uniform", activation="sigmoid"))

    model.summary()

