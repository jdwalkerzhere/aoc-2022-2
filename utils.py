def part1(data):
    def match_won(opponent, your_play):
        play_value = {'X':1, 'Y':2, 'Z':3}
        match_score = 0
        if opponent == 'A' and your_play == 'X' \
        or opponent == 'B' and your_play == 'Y' \
        or opponent == 'C' and your_play == 'Z': match_score = 3 
        elif your_play == 'X' and opponent == 'C' \
          or your_play == 'Y' and opponent == 'A' \
          or your_play == 'Z' and opponent == 'B': match_score = 6
        return match_score + play_value[your_play]
    
    def get_score(matches):
        score = 0
        for match in matches:
            score += match_won(*match)
        return score

    return get_score(data)


def part2(matches):
    score = 0
    for match in matches:
        o, y = match
        if o == 'A':
            if y == 'X': score += 3
            elif y == 'Y': score += 4
            else: score += 8
        elif o == 'B':
            if y == 'X': score += 1
            elif y == 'Y': score += 5
            else: score += 9
        else:
            if y == 'X': score += 2
            elif y == 'Y': score += 6
            else: score += 7
    return score