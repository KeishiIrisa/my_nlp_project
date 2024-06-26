import re

def load_dictionary1_from_file(filename):
    """
    指定されたファイルから極性辞書を読み込み、各行をリストに格納して返す関数。
    
    Parameters:
    filename (str): 読み込む辞書ファイルのパス
    
    Returns:
    list[list]: ファイルの各行を要素とするリスト。各要素は["単語", 極性値, "カテゴリ"]の形式。
    """
    polarity_map = {"e": 0.0, "n": -1.0, "p": 1.0}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        dictionary = {}
        for line in lines:
            match = re.match(r'^(.*?)\t([enp])\t(.*)$', line.strip())
            if match:
                word = match.group(1).strip('"')
                polarity_code = match.group(2)
                polarity_value = polarity_map.get(polarity_code, 0.0)
                dictionary[word] = polarity_value
        
        return dictionary
    except FileNotFoundError:
        print(f"Error: ファイル '{filename}' が見つかりませんでした。")
        return []
    except Exception as e:
        print(f"Error: ファイル '{filename}' を読み込む際にエラーが発生しました: {str(e)}")
        return []
