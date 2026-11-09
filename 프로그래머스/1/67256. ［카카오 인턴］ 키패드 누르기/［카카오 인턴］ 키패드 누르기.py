def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]

    left_r, left_c = 3, 0
    right_r, right_c = 3, 2

    for num in numbers:

        if num == 0:
            r, c = 3, 1
        else:
            r, c = divmod(num - 1, 3)

        if num in left:
            left_r, left_c = r, c
            answer += 'L'

        elif num in right:
            right_r, right_c = r, c
            answer += 'R'

        else:
            left_dist = abs(left_r - r) + abs(left_c - c)
            right_dist = abs(right_r - r) + abs(right_c - c)

            if left_dist < right_dist:
                answer += 'L'
                left_r, left_c = r, c

            elif left_dist > right_dist:
                answer += 'R'
                right_r, right_c = r, c

            else:
                if hand == 'right':
                    answer += 'R'
                    right_r, right_c = r, c
                else:
                    answer += 'L'
                    left_r, left_c = r, c

    return answer