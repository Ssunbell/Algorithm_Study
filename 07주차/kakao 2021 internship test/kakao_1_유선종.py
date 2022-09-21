def solution(s):
    character = ['zero','one', 'two', 'three',
                'four', 'five', 'six',
                'seven', 'eight', 'nine']
    for i, char in enumerate(character):
        s = s.replace(f'{char}', f'{i}')
    
    return int(s)