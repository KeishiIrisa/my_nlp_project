import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.predict_polarity as predict_polarity
def test_predict_positive():
#ポジティブな入力に対する予測結果をテスト
    input_statistics = [1.0, 1.0, -1.0, 0]
    expected_output = 'positive'
    assert predict_polarity.predict(input_statistics) == expected_output
def test_predict_negative():
#ネガティブな入力に対する予測結果をテスト
    input_statistics = [-1.0, -1.0, -1.0, 1.0, 1.0, 0,0,-1.0]
    expected_output = 'negative'
    assert predict_polarity.predict(input_statistics) == expected_output
def test_predict_neutral(): #中立的な入力に対する予測結果をテスト
    input_statistics = [1.0,-1.0]
    expected_output = 'neutral'
    assert predict_polarity.predict(input_statistics) == expected_output
def test_predict_empty():
#空リストの入力に対する予測結果をテスト
    input_statistics = []
    expected_output = 'neutral'
    assert predict_polarity.predict(input_statistics) == expected_output
