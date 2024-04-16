def shortest_word(sentence: str) -> str:
    arr = sentence.split()
    result = arr[0]
    for i in arr:
        if len(i) < len(result):
            result = i
    return len(result)

print(shortest_word("Call 911"))