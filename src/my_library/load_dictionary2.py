import re

def load_dictionary2_from_file(filename):
    """
    指定されたファイルから極性辞書を読み込み、各行をリストに格納して返す関数。
    
    Parameters:
    filename (str): 読み込む辞書ファイルのパス
    
    Returns:
    list[list]: ファイルの各行を要素とするリスト。各要素は["単語", 極性値, "カテゴリ"]の形式。
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        dictionary = {}
        for line in lines:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                category_and_polarity, word = parts
                match = re.match(r'^(ネガ|ポジ)（(.+?)）$', category_and_polarity)
                if match:
                    polarity_str, category = match.groups()
                    polarity_value = 1.0 if polarity_str == "ポジ" else -1.0
                    dictionary[word] = polarity_value
        
        return dictionary
    except FileNotFoundError:
        print(f"Error: ファイル '{filename}' が見つかりませんでした。")
        return []
    except Exception as e:
        print(f"Error: ファイル '{filename}' を読み込む際にエラーが発生しました: {str(e)}")
        return []
