def solution(words, queries):
    answer = []

    for query in queries:
        answ = 0
        temp_words = words.copy()
        index_ary = []
        for i in range(0, len(query)):
            if query[i] == '?':
                index_ary.append(i)

        for j, word in enumerate(temp_words):
            if len(query) == len(word):
                s = list(word)
                for index in index_ary:
                    s[index] = '?'
                temp_words[j] = ''.join(s)
        
        for word in temp_words:
            if query == word:
                answ += 1
        
        answer.append(answ)

    return answer
