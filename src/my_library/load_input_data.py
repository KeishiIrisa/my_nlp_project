"""
# 入力データを読み込むモジュール load_input_data.py
* input
    * .txtファイル
* process
    * 一行ごとにinput()処理
    * 1行ごとにリストに変換
* output
    * list{str}
"""

def load_text_from_file(filename):
  """
  指定されたファイルからテキストを読み込み、各行をリストに格納して返す関数。
   
  Parameters:
  filename (str): 読み込むテキストファイルのパス
   
  Returns:
  list[list[str]]: ファイルの各行を要素とするリスト内リスト
  """
  try:
      with open(filename, 'r', encoding='utf-8') as file:
          lines = file.readlines()
      # 改行文字を除去し、空白文字を削除した後、カンマで分割して各行をリストに格納する
      lines = [line.strip().split(",") for line in lines]
      return lines
  except FileNotFoundError:
      print(f"Error: ファイル '{filename}' が見つかりませんでした。")
      return []
  except Exception as e:
      print(f"Error: ファイル '{filename}' を読み込む際にエラーが発生しました: {str(e)}")
      return []

# テスト用のコード
if __name__ == "__main__":
  filename = 'input.txt' # 実際のファイル名に置き換えてください
  lines = load_text_from_file(filename)
  if lines:
    print(f"ファイル '{filename}' から読み込んだテキスト:")
    for line in lines:
      print(line)
  else:
    print("テキストの読み込みに失敗しました。")
