def manage_output(sentence_arrays, result):
    """
    sentence_arraysのリスト内のリストの末尾にresultをつけて、
    それを一行ごとに../data/result.fileに書き出す関数。
    """
    with open("../data/result.txt", "w", encoding="utf-8") as file:
        for i, sentence_array in enumerate(sentence_arrays):
            # 極性をリストの先頭につける
            sentence_array.insert(0, result[i])
            
            # ファイルに結果を出力する
            file.write(",".join(map(str, sentence_array)) + "\n")
