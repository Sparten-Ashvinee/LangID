# -*- coding: utf-8 -*-


import seaborn as sns



#df_data["Lang"].value_counts()

sns.countplot(y='Lang', data=df_data)

sns.distplot(y_test-y_pred)                                  #Normal distribuation

#plt.scatter(y_test,y_pred)                                   #It shoud be linear




"""# ROC Curve"""

# y_true = []

# for i in y_pred:
#     if i==0:
#         y_true.append(1)
#     else:
#         y_true.append(0)
# y_score = []
# for i in y_test:
#     if i==0:
#         y_score.append(1)
#     else:
#         y_score.append(0)
# y_true = np.array(y_true)
# y_score = np.array(y_score)
# from sklearn.metrics import roc_curve
# from sklearn.metrics import auc
# # Compute fpr, tpr, thresholds and roc auc
# fpr, tpr, thresholds = roc_curve(y_score, y_true)
# roc_auc = auc(y_true, y_score)
# # Plot ROC curve
# plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
# plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate or (1 - Specifity)')
# plt.ylabel('True Positive Rate or (Sensitivity)')
# plt.title('Receiver Operating Characteristic')
# plt.legend(loc="lower right")


