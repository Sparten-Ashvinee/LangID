# Indian Multilanguage classification

We are developing a web inference system for testing, available at [Ashvinee.xyz](https://www.ashvinee.xyz/coming-soon-01)
This work is part of the research project titled “An Architecture of Machine Translation for Text Analysis and Speech to Sign Language”.

The objective was to build a machine learning classifier capable of categorizing text into various categories across multiple languages spoken in India. Given India’s linguistic diversity, this task involves handling several Indian languages, each with distinct scripts, grammar, vocabulary, and cultural contexts.

### Dataset
The data was collected from the ground up.
The dataset includes text in the following languages:
  - Hindi
  - Bengali
  - Tamil
  - Telugu
  - Urdu

Indian multilanguage classification presents unique challenges due to the variety of scripts used by different languages (e.g., Devanagari for Hindi and Tamil script for Tamil).

### Model
Experimented with different models
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Naive Bayes (NB)

An LSTM model was also explored but was not included in the comparison.

### Results
The table below compares the performance of different models in classifying Indian multilingual text:

| Model  | Accuracy |
| ------------- | ------------- |
| Naive Bayes (NB)   | 87.18%  |
| Support Vector Machine (SVM)  | 78.03%  |
| K-Nearest Neighbors (KNN)  | 78.65%  |


### Resources
- Ashvinee, Narendra Bhusakhare, Jitesh Singh, Mausumi Goswami, “An architecture of machine
  translation from speech to sign language based on machine learning”, 2018 International Conference on
  Economics, Business Management and Business Analytic.
- [TEXT ANALYSIS AND SPEECH TO SIGN LANGUAGE TRANSLATION](https://drive.google.com/file/d/12FUb7YFmwyA0-Hqw8OcGQX9YRdjgRv4h/view)
- [Understand Short Texts by Harvesting and Analyzing Semantic Knowledge](https://ieeexplore.ieee.org/document/7476863)

