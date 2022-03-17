def solution(s):
    words_numbs = ['zero', 'one', 'two', 'three',
                   'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for idx, num in enumerate(words_numbs):
        if num in s:
            s = s.replace(num, str(idx))
            answer = s
        elif num not in s:
            answer = s
    return int(answer)
