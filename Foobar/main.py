
import math
def solution(area):
    area_list = []
    while area > 0:
        side = int(math.sqrt(area))
        square_side = side ** 2
        area_list.append(square_side)
        area = area - square_side
    return area_list

print(solution(12))

