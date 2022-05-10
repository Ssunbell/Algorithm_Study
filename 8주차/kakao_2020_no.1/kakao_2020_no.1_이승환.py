def solution(numbers, hand):
    answer = ''
    keypad = [[0,4,3,4,3,2,3,2,1,2],
              [4,0,1,2,1,2,3,2,3,4],
              [3,1,0,1,2,1,2,3,2,3],
              [4,2,1,0,3,2,1,4,3,2],
              [3,1,2,3,0,1,2,1,2,3],
              [2,2,1,2,1,0,1,2,1,2],
              [3,3,2,1,2,1,0,3,2,1],
              [2,2,3,4,1,2,3,0,1,2],
              [1,3,2,3,2,1,2,1,0,1],
              [2,4,3,2,3,2,1,2,1,0],
              [1,3,4,5,2,3,4,1,2,3],
              [1,5,4,3,4,3,2,3,2,1]]
    left_loc = 10
    right_loc = 11
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer+="L"
            left_loc = number
        elif number == 3 or number == 6 or number == 9:
            answer+="R"   
            right_loc = number
        elif number == 2 or number == 5 or number == 8 or number == 0:
            dist_left = keypad[left_loc][number]
            dist_right = keypad[right_loc][number]
            if dist_left < dist_right:
                answer+="L"
                left_loc = number
            if dist_left > dist_right:
                answer+="R"
                right_loc = number
            if dist_left == dist_right:
                if hand == "left":
                    answer+="L"
                    left_loc = number
                elif hand == "right":
                    answer+="R"
                    right_loc = number
    return answer