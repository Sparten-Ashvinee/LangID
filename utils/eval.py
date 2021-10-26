# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# ac = accuracy_score(y_test, y_pred)
# cm = confusion_matrix(y_test, y_pred)

# print("Accuracy is :",ac*100)


# Evaluation on Test set
scores = model.evaluate(X_test, Y_test, verbose=1)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# and now we will prepare data for scikit-learn confusion matrix and classification report
Y_pred = model.predict_classes(X_test)
Y_pred = keras.utils.to_categorical(Y_pred, num_classes=len(LANGUAGES_DICT))
LABELS =  list(LANGUAGES_DICT.keys())


#Confusion matrices
plt.figure(figsize=(15,10))
sns.heatmap(cm, annot = True)
plt.show()

matrix = metrics.confusion_matrix(y_test, y_pred)
print(matrix)


