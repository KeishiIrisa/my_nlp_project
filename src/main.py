import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

from my_library.load_input_data import load_text_from_file
from my_library.load_dictionary1 import load_dictionary1_from_file
from my_library.load_dictionary2 import load_dictionary2_from_file
from my_library.count_polarity_statistics import counter
from my_library.predict_polarity import predict
from my_library.manage_output import manage_output

from preprocess_data import preprocess_to_file

# データの形態素解析を行い、整理する
preprocess_to_file("../data/data.txt")
sentence_arrays = load_text_from_file("../data/processed_data.txt")

# 辞書をdictionary型に変換する
d1 = load_dictionary1_from_file("../data/dictionary1.txt")
d2 = load_dictionary2_from_file("../data/dictionary2.txt")

# 極性を評価する
result = []
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = counter(d1, d2, sentence)
    result.append(predict(count_statistics))

# 極性の結果をファイルに出力する
manage_output(sentence_arrays, result)
