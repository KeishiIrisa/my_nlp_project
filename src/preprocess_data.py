import MeCab

def preprocess_to_file(filename):
    """
    指定されたファイルからテキストを読み込み、一行ずつ形態素解析を行い、一行を構成する形態素に分割し、
    僕,は,嬉しい,です のように一行ずつする。
    その次に、それを../data/processed_data.txtファイルに書き出す。
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        mecab = MeCab.Tagger("-Owakati")
        processed_lines = [mecab.parse(line).strip().replace(' ', ',') for line in lines]

        with open('../data/processed_data.txt', 'w', encoding='utf-8') as outfile:
            for line in processed_lines:
                outfile.write(line + '\n')

    except FileNotFoundError:
        print(f"Error: ファイル '{filename}' が見つかりませんでした。")
    except Exception as e:
        print(f"Error: ファイル '{filename}' を読み込む際にエラーが発生しました: {str(e)}")
