# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    m_dict = {}
    for i, genre in enumerate(genres):
        if genre not in m_dict:
            m_dict[genre] = plays[i]
        else:
            m_dict[genre] += plays[i]
    # m_dict = {'classic': 1450, 'pop': 3100, 'rock': 2000}

    genre_name_list = [genre for genre, value in sorted(m_dict.items(), key=lambda item: item[1], reverse=True)]
    # genre_name_list = ['pop', 'rock', 'classic']

    genre_dict = {}
    for i, genre in enumerate(genres):
        if genre not in genre_dict:
            genre_dict[genre] = [(plays[i], i)]
        else:
            genre_dict[genre].append((plays[i], i))
    # genre_dict = {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 5)], 'rock': [(2000, 4)]}

    for genre_name in genre_name_list:
        sorted_list = sorted(genre_dict[genre_name], key=lambda item: item[0], reverse=True)

        answer.append(sorted_list[0][1])
        if len(sorted_list) > 1:
            answer.append(sorted_list[1][1])

    return answer

# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
solution(['classic', 'pop', 'classic', 'classic', 'rock', 'pop'], [500, 600, 150, 800, 2000, 2500])
