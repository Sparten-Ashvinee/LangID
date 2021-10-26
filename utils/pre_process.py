# -*- coding: utf-8 -*-


'''
Indian language constant+vowel
'''

bn_gm = [ক,খ,গ,ঘ,ঙ,চ,ছ,জ,ঝ,ঞ,ট,ঠ,ড,ঢ,ণ,ত,থ,দ,ধ,ন,প,ফ,ব,ভ,ম,য,র,ল,শ,ষ,স,হ,য়,ড়,ঢ়]
ta_gm = [அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ,க,ங,ச,ஞ,ட,ண,த,ந,ன,ப,ம,ய,ர,ற,ல,ள,ழ,வ]
hi_gm = [क,ख,ग,घ,ङ,च,छ,ज,झ,ञ,ट,ठ,ड,ढ,ण,त,थ,द,ध,न,प,फ,ब,भ,म,य,र,ल,व,ष,स,हअ,आ,इ,ई,उ,ऊ,ए,ऐ,ओ,औ,अं,अः,ऋ,ॠ]
ur_gm = [آ,ب,,پ,ت,ٹ,ث,ج,چ,ح,خ,د,ڈ,ذ,ر,ڑ,ز,ژ,س,ش,ص,ض,ط,ظ,ع,غ,ف,ق,ک,گ,ل,م,ن,و,ہ,ی,ے]
te_gm = [అ,ఆ,ఇ,ఈ,అ,ఉ,ఊ,ఋ,ౠ,ఌ,ౡ,ఎ,ఏ,ఐ,ఒ,ఓ,ఔ,అం,అః,క,ఖ,గ,ఘ,ఙ,చ,ఛ,జ,ఝ,ఞ,ట,ఠ,డ,ఢ,ణ,త,థ,ద,ధ,న,ప,ఫ,బ,భ,మ,య,ర,ల,వ,శ,ష,స,హ,ళ,క్ష,ఱ]



"""#Text Preprocessing
#### Remove unwanted symbols, numbers
"""

# creating a list for appending the preprocessed text
data_list = []
# iterating through all the text
for text in X:
       # removing the symbols and numbers
        text = re.sub(r'[!@#$(),"%^*?:;~`0-9]', '', text)
        text = re.sub(r'[[]]', ' ', text)
        # converting the text to lower case
        text = text.lower()
        # appending to data_list
        data_list.append(text)


'''
x_val = data_list[:10000]
partial_x_train = data_list[10000:]

y_val = y[:10000]
partial_y_train = y[10000:]

# x_val= tf.convert_to_tensor(x_val)
# partial_x_train = tf.convert_to_tensor(partial_x_train)

# x_val = tfds.as_numpy(x_val)
# partial_x_train = tfds.as_numpy(partial_x_train)

x_val = np.array(x_val)
partial_x_train = np.array(partial_x_train)

y[0:10]

partial_x_train[:10]

x_val[:10]
'''
