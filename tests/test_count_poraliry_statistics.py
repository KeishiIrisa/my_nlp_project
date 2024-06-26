import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.count_polarity_statistics as counter
import my_library.load_dictionary2 as dictionary_loader
d1 = dictionary_loader.load("../extlib/dictionary1.txt")  
d2 = dictionary_loader.load("../extlib/dictionary2.txt")  
def test_count_1():
    input_sentence = ["僕", "は", "嬉しい"] #普通の文でテスト
    expected_output = [0.0, 0.0, 1.0]
    assert counter.count(d1, d2, input_sentence) == expected_output
def test_count_2():
    input_sentence = ["aslziusrgqadf"] #辞書にない単語でテスト
    expected_output = [0.0]
    assert counter.count(d1, d2, input_sentence) == expected_output
