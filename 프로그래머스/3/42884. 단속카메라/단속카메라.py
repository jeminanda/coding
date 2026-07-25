def solution(routes):
    routes.sort(key=lambda x: x[1])
    last_camera = -30001
    count = 0
    for start, end in routes:
        # 현재 차량의 진입 지점이 마지막 카메라 위치보다 뒤에 있으면
        if start > last_camera:
            count += 1
            last_camera = end   #이 차량 나가는 지점에 새 카메라
    return count