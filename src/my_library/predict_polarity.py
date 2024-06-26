def predict(count_statistics):
    if len(count_statistics) == 0:
        return "neutral"
    positiveness = sum(count_statistics) / len(count_statistics)
    if positiveness > 0:
        return "positive"
    elif positiveness == 0:
        return "neutral"
    else:
        return "negative"
